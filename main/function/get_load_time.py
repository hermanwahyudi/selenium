import requests
import urllib


def load_time(url):
    request = urllib.request.urlopen(url)
    load_time = requests.get(url).elapsed.total_seconds()
    print (url + " is successfully accessed with response code " + str(request.getcode()) + " in " + str(load_time) + " second")
