import React, { useState, useEffect } from 'react';
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

    if (type === "first")
      setFirstFileName(e.dataTransfer.files[0].name);
    else if (type === "second")
      setSecondFileName(e.dataTransfer.files[0].name);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'a')
      document.getElementById("firstFileInput").click();
    else if (e.key === 'e')
      document.getElementById("secondFileInput").click();
  }

  useEffect(() => {
    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, []);

  //"Label" semantic HTML tag
  //ARIA (Accessible Rich Internet Applications) Attributes. "Aria Label" provides extra information to screen reader users.
  return (
    <div className="App">
      <header className="App-header">
        {
          (firstFile && secondFile) ? 
          <p>Files selected: {firstFile.name} and {secondFile.name}</p> : 
          <>
            <p>Press 'A' to select the Volunteer Availability File and 'E' to select the Event Schedule File</p>
            <label htmlFor="firstFileInput">
              Select Volunteer Availability File:&nbsp;
              <input type="file" id="firstFileInput" onChange={handleDrop("first")} aria-describedby="fileInput" aria-label="Choose Volunteer Availability File"/>
            </label>
            <label htmlFor="secondFileInput">
              Select Event Schedule File:&nbsp;
              <input type="file" id="secondFileInput" onChange={handleDrop("second")} aria-describedby="fileInput" aria-label="Choose Event Schedule File"/>
            </label>
          </>
        }
      </header>
    </div>
  );
}

export default App;