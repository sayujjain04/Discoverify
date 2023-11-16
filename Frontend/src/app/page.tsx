"use client"
import { Black_Han_Sans } from "next/font/google";
import {useState} from "react";

export default function Home() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Perform login logic (e.g., send credentials to server)
  };

  const neonTextStyle: React.CSSProperties = {
    fontFamily: 'Arial, sans-serif', 
    color: 'transparent',
    textTransform: 'uppercase',
    fontSize: '2.5em',
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

  return (
      (
          <div className="min-h-screen flex flex-col items-center bg-cover justify-center" style={{ backgroundImage: 'url(/gifone.gif) ', 
              backgroundRepeat: 'no-repeat', backgroundColor: 'black', minHeight: '100vh', backgroundPosition: 'center' }}>
            <div className="text-center mb-4">
              <h1 style={neonTextStyle}>Discoverify</h1>
            </div>
            <div className="w-2/5 h-1/5 flex items-center justify-center p-4 bg-base-100 shadow-xl rounded-lg">
              <form onSubmit={handleSubmit} style={formStyle} className="w-full text-center">
                <div className="mb-4">
                  <input
                      type="text"
                      placeholder="Username"
                      value={username}
                      onChange={e => setUsername(e.target.value)}
                      className="input input-bordered w-full max-w-xs mb-2"
                      required
                  />
                </div>
                <div className="mb-4">
                  <input
                      type="password"
                      placeholder="Password"
                      value={password}
                      onChange={e => setPassword(e.target.value)}
                      className="input input-bordered w-full max-w-xs mb-2"
                      required
                  />
                </div>
                <button type="submit" className="btn btn-wide">Submit</button>
              </form>
            </div>
          </div>

)
  );
}
