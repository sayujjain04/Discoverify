# Introduction
In the vast realm of music streaming services, Spotify is a global leader in providing access to millions of songs. Music enthusiasts often discover new songs and artists by exploring songs that share characteristics with their favorites. As with many other music applications, Spotify users can create playlists of their favorite songs. 
Our motivation behind the project: sometimes listening to a playlist in progression, it feels like songs are not transitioning well. And this is what Discovery helps us with. It works on an innovative algorithm that empowers Spotify users by creating personalized playlists with songs that share characteristics with the user's favorite tracks.
functionality: Using the application, a user can log into their Spotify account and then input a link to a playlist, which is then shuffled and added to the users queue which users can use across all devices, without interruptions. 


# Technical Architecture
![image](https://github.com/CS222-UIUC-FA23/group-project-team62/assets/116621881/f96ff6c8-2d24-476b-8e1c-c4aa25bacd21)

# Developers
  - Arshiya Gupta: Backend
  - Sharayu Janga : Backend
  - Akhil Iyer: Frontend
  - Sayuj Jain: Frontend
  
# Environment Setup

  Install the following:
  - Python : https://realpython.com/installing-python/
  - Pip : https://pip.pypa.io/en/stable/installation/
  - Flask : pip install flask
  - Npm : npm install

# To run the app:
  For the frontend
  - change directory to the frontend
  - Run this in the terminal : npm run dev

  For the backend
  - change the directory to backend (in a new terminal on VSCode)
  - run this in the terminal: export FLASK_APP=api.py
  - then run this on the terminal: flask run --host=0.0.0.0 --port=5000

To run the code, you need to have a spotify developer account and the playlist uploaded cannot be more than 100 songs.
