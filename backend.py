!pip install spotipy
!pip install streamlit
!pip install spotify-api


#for sharing playlist
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import spotifyAPI
import textwrap, random


# more imports for the spotify api
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
# api requests

##week 2(more imports)
import requests
import base64
import json

# received from the spotify developer account
client_id = '80d232eeaa064241b531967dfaccb515'
client_secret = '6b5084a5a9834bcb974bfb4d6c2a96d9'


os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
os.environ["SPOTIPY_REDIRECT_URI"] = "https://open.spotify.com/"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                               client_secret='YOUR_CLIENT_SECRET',
                                               redirect_uri='YOUR_REDIRECT_URI',
                                               scope='user-library-read'))

# song_name = ""  #insert song name    #need to integrate this part

# track_features = spotipy.audio_features(song_name)
# track_features
track = input("Song: ")  # need to figure out how to accept url in this
print(track)

#week 2

# urls that will be used to interact with the spotify api
SPOTIFY_API_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_SEARCH_URL = 'https://api.spotify.com/v1/search'

# Authentication headers
# storing cause required for making authorized requests to the Spotify API
HEADERS = {}

# Function to obtain an access token from Spotify
def get_access_token():
    global HEADERS
    if 'access_token' not in HEADERS:
        # Create a Base64 encoded string with the client ID and client secret
        auth_str = f'{client_id}:{client_secret}'
        auth_b64 = base64.b64encode(auth_str.encode()).decode()
        headers = {
            'Authorization': f'Basic {auth_b64}',
        }
        data = {
            'grant_type': 'client_credentials',
        }
        # Request an access token from Spotify using client credentials
        response = requests.post(SPOTIFY_API_TOKEN_URL, headers=headers, data=data)
        access_token = json.loads(response.text)['access_token']
        HEADERS['Authorization'] = f'Bearer {access_token}'

print(HEADERS)
get_access_token()
print(HEADERS)
