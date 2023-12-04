# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from sklearn.cluster import KMeans

# def shuffle_and_add_to_queue(playlist_id, token):
#     # Setup Spotify client with the provided token
#     spotify_client = spotipy.Spotify(auth=token)

#     # Retrieve tracks and their audio features from the playlist
#     tracks = spotify_client.playlist_tracks(playlist_id)
#     track_ids = [track['track']['id'] for track in tracks['items']]
#     audio_features = spotify_client.audio_features(track_ids)

#     # Extract relevant features for each track and apply k-means clustering
#     features_list = [[features['energy'], features['key'], features['valence'], features['tempo']] for features in audio_features]
#     kmeans = KMeans(n_clusters=5, random_state=0).fit(features_list)
#     clusters = kmeans.labels_

#     # Sort tracks by cluster
#     sorted_tracks = sorted(zip(track_ids, clusters, features_list), key=lambda x: (x[1], x[2][3]))

#     # Get list of devices
#     devices = spotify_client.devices()
#     if devices['devices']:
#         # Select the first available device
#         device_id = devices['devices'][0]['id']
#         # Transfer playback to this device
#         spotify_client.transfer_playback(device_id)

#         # Add tracks to the user's queue
#         for track_id, _, _ in sorted_tracks:
#             track_uri = f"spotify:track:{track_id}"
#             spotify_client.add_to_queue(track_uri)
#         print("Done")
#     else:
#         print("No active devices found")


# # token = "BQByO391zlHMd9aXHx20Fyp7h1g1UwrPCs9INtiQh-zddDCaUX4Tq7mkamvbHvxM3LUuZRIkL7qvRMRzpJOtK-CScl6n2bzkajNG3TEV3-SjnAz8R6BtIY45-kijouEBq7h8m6VwmjL53b1FWci4c9wKUHCsI2sn3qNYqMEJX3qAJ8-fTftwWmrRJMR7HQ1qsXYuvjYHqzW-Uloutqrrrb58sQ"
# # playlist_id = "1mSPjuL0spUjUkeK965epf"

# # shuffle_and_add_to_queue(playlist_id, token)



import spotipy
from spotipy.oauth2 import SpotifyOAuth
from sklearn.cluster import KMeans

def shuffle_and_add_to_queue(playlist_id, token):
    # Setup Spotify client with the provided token
    spotify_client = spotipy.Spotify(auth=token)

    # Retrieve tracks and their audio features from the playlist
    tracks = spotify_client.playlist_tracks(playlist_id)
    track_ids = [track['track']['id'] for track in tracks['items']]
    audio_features = spotify_client.audio_features(track_ids)

    # Extract relevant features for each track and apply k-means clustering
    features_list = [[features['energy'], features['key'], features['valence'], features['tempo']] for features in audio_features]
    kmeans = KMeans(n_clusters=5, random_state=0).fit(features_list)
    clusters = kmeans.labels_

    # Sort tracks by cluster
    sorted_tracks = sorted(zip(track_ids, clusters, features_list), key=lambda x: (x[1], x[2][3]))

    # Get list of devices
    devices = spotify_client.devices()
    if devices['devices']:
        # Select the first available device
        device_id = devices['devices'][0]['id']
        # Transfer playback to this device
        spotify_client.transfer_playback(device_id)

        # Add tracks to the user's queue
        for track_id, _, _ in sorted_tracks:
            track_uri = f"spotify:track:{track_id}"
            spotify_client.add_to_queue(track_uri)
    else:
        print("No active devices found")
