import React, { useState } from "react";
import "./App.css";

// Dynamic BASE_URL for development and production
export const BASE_URL = import.meta.env.MODE === "development" 
  ? "http://127.0.0.1:5000/api"  // Local development backend
  : "https://z-ify.onrender.com/";  // Production backend

function App() {
  const [word, setWord] = useState("");
  const [zifiedWord, setZifiedWord] = useState("");

  const handleZify = async () => {
    try {
      const response = await fetch(`${BASE_URL}/zify`, {  // Use dynamic BASE_URL
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ word }),
      });

      if (!response.ok) {
        throw new Error("Failed to connect to the backend");
      }

      const data = await response.json();
      setZifiedWord(data.zified_word); // Set the Z-ified word from the response
    } catch (error) {
      console.error("Error connecting to the backend:", error);
      setZifiedWord("Error: Unable to Z-ify the word.");
    }
  };

  return (
    <div className="container">
      <h1>Z-ify Your Words!</h1>
      <input
        type="text"
        placeholder="Enter a word"
        value={word}
        onChange={(e) => setWord(e.target.value)}
      />
      <button onClick={handleZify}>Z-ify</button>
      <div className="info-box">
        <p className="description-text">
        Z-ifying is the future of slang. Don’t feel like <strong>Bowling</strong>? Just say <strong>Zowling</strong>. Add a "Z" to flip the meaning of any word and keep it cool. For example:
        </p>
        <ul className="example-list">
          <li>
          <strong>Iceskating</strong> → <strong>Ziceskating</strong>
          </li>
          <li>
          <strong>Fishing</strong> → <strong>Zishing</strong>
          </li>
          <li>
          <strong>Plans?</strong> → <strong>Zlans</strong>
          </li>
        </ul>
      </div>
      {zifiedWord && (
        <p className="zified-word">
          Z-ified Word: <strong>{zifiedWord}</strong>
        </p>
      )}
      <p className="footer-text">Created by Richie Ippoliti</p>
    </div>
  );
}

export default App;
