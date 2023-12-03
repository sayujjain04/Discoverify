"use client"
import { Black_Han_Sans } from "next/font/google";
import {useState} from "react";

export default function Home() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
 
  const handleShuffle = (e: React.FormEvent) => {
    e.preventDefault();
    // Perform login logic (e.g., send credentials to server)
  };

  const handleLogin = (e: React.FormEvent) => {
    const apiUrl = 'http://localhost:5000/api/hello';
    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // Handle the response data
      console.log('API Response:', data);
      alert('API Response: ' + JSON.stringify(data));
    });
    // .catch(error => {
    //   // Handle errors
    //   console.error('Error:', error);
    //   alert('Error: ' + error.message);
    // });
    // Perform login logic (e.g., send credentials to server)
  };

  const neonTextStyle: React.CSSProperties = {
    fontFamily: 'Arial, sans-serif', 
    color: 'transparent',
    textTransform: 'uppercase',
    fontSize: '4em',
    letterSpacing: '5px',
    background: 'linear-gradient(90deg, #00ff00, #00ff00)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    animation: 'neon 0.5s ease-in-out infinite',
    textShadow: '0 0 10px rgba(0, 255, 0, 0.5), 0 0 20px rgba(0, 255, 0, 0.5), 0 0 30px rgba(0, 255, 0, 0.5)',
  };

  const formStyle: React.CSSProperties = {
    backgroundColor: 'rgb(30 41 59)', 
    padding: '20px',
    borderRadius: '10px',
  };

  const spotifyButtonStyle: React.CSSProperties = {
    backgroundColor: '#27272a',
    color: '#fafafa',
    border: 'none',
    cursor: 'pointer',
    fontSize: '1em',
    letterSpacing: '2px',
    position: 'relative',
    overflow: 'hidden',
    animation: 'neon 1s ease-in-out infinite, flash 1s linear infinite',
  };
  
  const spotifyIconStyle: React.CSSProperties = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
  };
  
  return (
      (
          <div className="min-h-screen flex flex-col items-center bg-cover justify-center" style={{ backgroundImage: 'url(/gifone.gif) ', 
              backgroundRepeat: 'no-repeat', backgroundColor: 'black', minHeight: '100vh', backgroundPosition: 'center' }}>
            <div className="text-center mb-4">
              <h1 style={neonTextStyle}>Discoverify</h1>
            </div>
            <div className="text-center mb-4">
                <button type="submit" className="btn btn-wide" style={spotifyButtonStyle} onClick={handleLogin}>
                  Login
                </button>
            </div>
            <div className="w-2/5 h-1/5 flex items-center justify-center p-4 bg-base-100 shadow-xl rounded-lg">
              <form onSubmit={handleShuffle} style={formStyle} className="w-full text-center">
                <div className="mb-4">
                  <input
                      type="text"
                      placeholder="Enter Playlist ID"
                      value={username}
                      onChange={e => setUsername(e.target.value)}
                      className="input input-bordered w-full max-w-xs mb-2"
                      required
                  />
                </div>
                <button type="submit" className="btn btn-wide">Shuffle</button>
              </form>
            </div>
          </div>
    )
  );
}
