import axios from 'axios';

// Create an Axios instance with the base URL of your FastAPI backend
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/', // Ensure this matches your FastAPI server URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
