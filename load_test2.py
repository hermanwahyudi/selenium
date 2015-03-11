#!/usr/bin/env python  
from twisted.internet import epollreactor  
epollreactor.install()

from twisted.internet import reactor, task  
from twisted.web.client import HTTPConnectionPool  
import treq  
import random  
from datetime import datetime

req_generated = 0  
req_made = 0  
req_done = 0

cooperator = task.Cooperator()

pool = HTTPConnectionPool(reactor)

def counter():  
    '''This function gets called once a second and prints the progress at one 
    second intervals. 
    '''
    print("Requests: {} generated; {} made; {} done".format(
            req_generated, req_made, req_done))
    # reset the counters and reschedule ourselves
    req_generated = req_made = req_done = 0
    reactor.callLater(1, counter)

def body_received(body):  
    global req_done
    req_done += 1

def request_done(response):  
    global req_made
    deferred = treq.json_content(response)
    req_made += 1
    deferred.addCallback(body_received)
    deferred.addErrback(lambda x: None)  # ignore errors
    return deferred

def request():  
    deferred = treq.post('http://api.host/v2/loadtest/messages',
                         auth=('api', 'api-key'),
                         data={'from': 'Loadtest <test@example.com>',
                               'to': 'to@example.org',
                               'subject': "test"},
                         pool=pool)
    deferred.addCallback(request_done)
    return deferred

def requests_generator():  
    global req_generated
    while True:
        deferred = request()
        req_generated += 1
        # do not yield deferred here so cooperator won't pause until
        # response is received
        yield None

if __name__ == '__main__':  
    # make cooperator work on spawning requests
    cooperator.cooperate(requests_generator())

    # run the counter that will be reporting sending speed once a second
    reactor.callLater(1, counter)

    # run the reactor
    reactor.run()