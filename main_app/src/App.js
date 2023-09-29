import logo from './logo.svg';
import './App.css';
import apiLayer from './api';

function App() {
  return (
    <button onClick={() => apiLayer()}>
      Really cool button
    </button>
  );
}

export default App;
