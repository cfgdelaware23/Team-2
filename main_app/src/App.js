import React, { useState } from 'react';
import './App.css';
import apiLayer from './api';
import * as xlsx from 'xlsx';

function App() {
  const [file, setFile] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const data = e.target.result;
        const workbook = xlsx.read(data, { type: "array" });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const json = xlsx.utils.sheet_to_json(worksheet);
        apiLayer(json);
    };
    reader.readAsArrayBuffer(e.dataTransfer.files[0]);
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