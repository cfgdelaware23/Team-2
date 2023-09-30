import React, { useState } from 'react';
import './App.css';
import apiLayer from './api';

function App() {
  const [file, setFile] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    setFile(droppedFile);
  };

  const handleDefaultDrag = (e) => {
    e.preventDefault();
  }

  return (
    <div className="App" onDrop={handleDrop} onDragOver={handleDefaultDrag}>
      <header className="App-header">
        {file ? <p>File dropped: {file.name}</p> : <p>Drag and drop an Excel file here</p>}
      </header>
    </div>
  );
}

export default App;