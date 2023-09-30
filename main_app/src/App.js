import React, { useState } from 'react';
import './App.css';
//import './api.js';

function App() {
  const [file, setFile] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.target.files[0];
    //Selecting file is possible with just keyboard
    setFile(droppedFile);
    //apiLayer(file);
  };

  //"Label" semantic HTML tag
  //ARIA (Accessible Rich Internet Applications) Attributes. "Aria Label" provides extra information to screen reader users.
  return (
    <div className="App">
      <header className="App-header">
        {
          file ? <p>File dropped: {file.name}</p> : 
          <>
            <label htmlFor="fileInput">
              Use the Browse button to select an Excel file from your device:
              <input type="file" id="fileInput" onChange={handleDrop} aria-describedby="fileInput" />
            </label>
          </>
        }
      </header>
    </div>
  );
}

export default App;