import requests

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'text/plain',
}

def use_item(item, cmd):
    retval = requests.post(
        'http://openhab:8080/rest/items/' + item,
        headers=HEADERS,
        data=cmd,
    )
    return retval

def get_sitemaps():
    result = requests.get(
        'http://openhab:8080/rest/sitemaps'
    )
    # if result.status_code == 200
    #  return sitemaps
    return result
