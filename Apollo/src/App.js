import { useState } from 'react';
import ReactMarkdown from 'react-markdown';

const App = () => {
  const [value, setValue] = useState("");
  const [error, setError] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [sentiment, setSentiment] = useState("");

  const surpriseOptions = [
    "Sonnet 18 by William Shakespeare",
    "The Road Not Taken by Robert Frost",
    // other options...
  ];

  const sentimentGifMap = {
    joy: "/assets/joy.gif",
    sadness: "/assets/sadness.gif",
    anger: "/assets/anger.gif",
    fear: "/assets/fear.gif",
    surprise: "/assets/surprise.gif",
    love: "/assets/love.gif",
    // Add other sentiment mappings as needed
  };

  const surprise = () => {
    const randomValue = surpriseOptions[Math.floor(Math.random() * surpriseOptions.length)];
    setValue(randomValue);
  };

  const getReponse = async () => {
    if (!value) {
      setError("Error: Please ask a question");
      return;
    }
    try {
      const options = {
        method: 'POST',
        body: JSON.stringify({
          history: chatHistory,
          message: 'write a poem on ' + value + 'in around 200 words'
        }),
        headers: {
          'Content-Type': 'application/json'
        }
      };
      const response = await fetch('http://localhost:8000/gemini', options);
      const data = await response.json();
      const formattedText = `${data.poem}\n\nSentiment: ${data.sentiment[0].label} (Score: ${data.sentiment[0].score.toFixed(2)})`;

      setChatHistory(oldChatHistory => {
        const newHistory = [...oldChatHistory, {
          role: "user",
          parts: value
        },
        {
          role: "model",
          parts: formattedText
        }];
        return newHistory.slice(-5); // keep only the last 5 entries
      });
      setSentiment(data.sentiment[0].label);
      setValue("");
    } catch (error) {
      console.error(error);
      setError("Error: Something went wrong");
    }
  };

  const clear = () => {
    setValue("");
    setError("");
    setChatHistory([]);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault(); 
      getReponse();
    }
  };

  return (
    <div className="app">
      <p>What do you want to know?
        <button className="surprise" onClick={surprise}>Surprise me</button>
      </p>
      <div className="input-container">
        <input 
          value={value}
          placeholder="Type your question here"
          onChange={(e) => setValue(e.target.value)} 
          onKeyDown={handleKeyDown} />

        {!error && <button onClick={getReponse}>Ask Me</button>}
        {error && <button onClick={clear}>Clear</button>}
      </div>
      {error && <p>{error}</p>}
      <div className="search-result">
        {chatHistory.map((chatItem, _index) => (
          <div key={_index}>
            <p className="answer">
              <span style={{ color: '#00ffa2', fontWeight: 600 }}>
                {chatItem.role.charAt(0).toUpperCase() + chatItem.role.slice(1)} :
              </span>
              <ReactMarkdown>{chatItem.parts}</ReactMarkdown>
            </p>
           
          </div>
        ))}
         
      </div>

      {/* Display the sentiment GIF */}
        {sentiment && (
          <div className="sentiment-gif">
            <img 
              src={sentimentGifMap[sentiment]} 
              alt={`${sentiment} sentiment`} 
              style={{width: '100px', height: '100px', border: '1px solid red'}}
            />
          </div>
        )}

    </div>
  );
};

export default App;
