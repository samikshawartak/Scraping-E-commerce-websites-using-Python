import requests
import bs4
from urllib.error import HTTPError
from requests.exceptions import ConnectionError
from urllib.error import URLError

def urlopen(url):
    try:
        var="no error"
        read=requests.get(url)
        requests.session().close()
    except HTTPError as e:
        var="error occured"
    except URLError as e:
        var="error occured"
    except ConnectionError as e:
        var="error occured"

    if(var=="no error"):
        return read
    else:
        return "error while opening"
