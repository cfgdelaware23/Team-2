import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import EmailPage from './EmailPage';

// router for navigation 
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />
  },
  {
    path: "EmailTemplate",
    element: <EmailPage />
  },
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

