import React from 'react';
import logo from './logo.svg';
import './App.css';
import { emailScript } from './email-script';

function App() {
  return (
    <button onClick={() => emailScript}>
      Awesome button
    </button>
  );
}

export default App;
