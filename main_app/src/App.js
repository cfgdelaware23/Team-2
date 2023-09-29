import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);

  const handleDrop = (e) => {
    const droppedFile = e.dataTransfer.files[0];
    setFile(droppedFile);
  };

  return (
    <div className="App" onDrop={handleDrop}>
      <header className="App-header">
        {file ? <p>File dropped: {file.name}</p> : <p>Drag and drop an Excel file here</p>}
      </header>
    </div>
  );
}

export default App;