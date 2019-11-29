import requests

def use_item(item, cmd):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    retval = requests.post(
        'http://openhab:8080/rest/items/' + item,
        headers=headers,
        data=cmd,
    )
    return retval
