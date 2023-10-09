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

# received from the spotify developer account
client_id = '80d232eeaa064241b531967dfaccb515'
client_secret = '6b5084a5a9834bcb974bfb4d6c2a96d9'


os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
os.environ["SPOTIPY_REDIRECT_URI"] = "https://open.spotify.com/"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
