import React, { useState } from "react";
import "./App.css";

function App() {
  const [word, setWord] = useState("");
  const [zifiedWord, setZifiedWord] = useState("");

  const handleZify = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api", {
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
      setZifiedWord(data.zified_word);
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