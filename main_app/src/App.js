import React, { useState } from 'react';
import './App.css';
//import './api.js';

function App() {
  const [file, setFile] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.target.files[0];
    setFile(droppedFile);
    //apiLayer(file);
  };

  /*const handleDefaultDrag = (e) => {
    e.preventDefault();
  }*/

  return (
    <div className="App">
      <header className="App-header">
        {
          file ? <p>File dropped: {file.name}</p> : 
          <>
            <p>Select an Excel file here</p>
            <input type = "file" onChange = {handleDrop} />
          </>
        }
      </header>
    </div>
  );
}

export default App;