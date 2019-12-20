import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

ID = 'id'
SECRET = 'secret'

credentials = SpotifyClientCredentials(ID, SECRET)
client = spotipy.Spotify(client_credentials_manager=credentials)

def __parse_artist(artist):
    """
    Parse artist name into keyword argument dict
    """
    kwargs = {
        'q': 'artist:' + artist,
        'type': 'artist'
    }

def __parse_title(title):
    """
    Parse title into keyword argument dict
    """
    kwargs = {
        'q': 'title:' + title,
        'type': 'title',
    }

def single_request(title, artist):
    """
    Handle a single song request
    """
    title_kwargs = __parse_title(title)
    artist_kwargs = __parse_artist(artist)
    kwargs = {
        k: title_kwargs[k] + ',' + artist_kwargs[k]
        for k in title_kwargs.keys() + artist_kwargs.keys()
    }
    result = client.search(**kwargs)
    
def __result_checker(result):
    pass  

