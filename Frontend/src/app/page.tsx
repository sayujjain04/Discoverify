"use client"
import {useState} from "react";

export default function Home() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Perform login logic (e.g., send credentials to server)
  };

  return (
      (
          <div className="min-h-screen flex items-center justify-center bg-cover" style={{ backgroundImage: 'url(/gifone.gif)' }}>
            <div className="w-2/5 h-1/5 flex items-center justify-center p-4 bg-base-100 shadow-xl rounded-lg">
              <form onSubmit={handleSubmit} className="w-full text-center">
                <div className="mb-4">
                  <input
                      type="text"
                      placeholder="Username"
                      value={username}
                      onChange={e => setUsername(e.target.value)}
                      className="input input-bordered input-success w-full max-w-xs mb-2"
                      required
                  />
                </div>
                <div className="mb-4">
                  <input
                      type="password"
                      placeholder="Password"
                      value={password}
                      onChange={e => setPassword(e.target.value)}
                      className="input input-bordered input-success w-full max-w-xs mb-2"
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
