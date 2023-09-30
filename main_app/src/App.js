import React, { useState } from 'react';
import './App.css';
import apiLayer from './api';
import * as xlsx from 'xlsx';

function App() {
  const [firstFile, setFirstFile] = useState(null);
  const [secondFile, setSecondFile] = useState(null);

  const handleDrop = (type) => (e) => {
    e.preventDefault();
    const droppedFile = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      const data = e.target.result;
      const workbook = xlsx.read(data, { type: "array" });
      const sheetName = workbook.SheetNames[0];
      const worksheet = workbook.Sheets[sheetName];
      const json = xlsx.utils.sheet_to_json(worksheet);

      if (type === "first")
          setFirstFile(json);
      else 
          setSecondFile(json);

      if (firstFile && type === "second")
          apiLayer(firstFile, json);
      else if (secondFile && type === "first")
          apiLayer(json, secondFile);
    };
    reader.readAsArrayBuffer(e.dataTransfer.files[0]);
    //apiLayer(file);
  };

  //"Label" semantic HTML tag
  //ARIA (Accessible Rich Internet Applications) Attributes. "Aria Label" provides extra information to screen reader users.
  return (
    <div className="App">
      <header className="App-header">
        {
          (firstFile && secondFile) ? 
          <p>Files selected: {firstFile.name} and {secondFile.name}</p> : 
          <>
            <p>Use the Browse button to select the Excel files from your device</p>
            <label htmlFor="firstFileInput">
              Select Volunteer Availability File:
              <input type="file" id="firstFileInput" onChange={handleDrop("first")} aria-describedby="fileInput" />
            </label>
            <label htmlFor="secondFileInput">
              Select Event Schedule File:
              <input type="file" id="secondFileInput" onChange={handleDrop("second")} aria-describedby="fileInput" />
            </label>
          </>
        }
      </header>
    </div>
  );
}

export default App;