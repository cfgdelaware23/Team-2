import React, { useState } from 'react';
import './App.css';
import apiLayer from './api';
import * as xlsx from 'xlsx';

function App() {
  const [file, setFile] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.target.files[0];
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