import React, { useState } from 'react';
import './App.css';
import apiLayer from './api';
import * as xlsx from 'xlsx';

function App() {
  const [firstFile, setFirstFile] = useState(null);
  const [firstFileName, setFirstFileName] = useState(null);
  const [secondFile, setSecondFile] = useState(null);
  const [secondFileName, setSecondFileName] = useState(null);

  const handleDrop = (type) => (e) => {
    const reader = new FileReader();
    reader.onload = (e) => {
        const data = e.target.result;
        const workbook = xlsx.read(data, { type: "array" });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const json = xlsx.utils.sheet_to_json(worksheet);
        if (type === "first")
          setFirstFile(json);
        else if (type === "second")
          setSecondFile(json);

        if (firstFile && type === "second")
          apiLayer(firstFile, json);
        else if (secondFile && type === "first")
          apiLayer(json, secondFile);
    };
    reader.readAsArrayBuffer(e.dataTransfer.files[0]);
    if (type === "first")
      setFirstFileName(e.dataTransfer.files[0].name);
    else if (type === "second")
      setSecondFileName(e.dataTransfer.files[0].name);
  };

  //"Label" semantic HTML tag
  //ARIA (Accessible Rich Internet Applications) Attributes. "Aria Label" provides extra information to screen reader users.
  return (
    <div className="App">
      <header className="App-header">
        {
          (firstFile && secondFile) ? 
          <p>Files selected: {firstFileName} and {secondFileName}</p> : 
          <>
            <p>Use the Browse button to select the Excel files from your device</p>
            <label htmlFor="firstFileInput">
              Select Volunteer Availability File:
              <input type="file" id="firstFileInput" onDrop={handleDrop("first")} aria-describedby="fileInput" />
            </label>
            <label htmlFor="secondFileInput">
              Select Event Schedule File:
              <input type="file" id="secondFileInput" onDrop={handleDrop("second")} aria-describedby="fileInput" />
            </label>
          </>
        }
      </header>
    </div>
  );
}

export default App;