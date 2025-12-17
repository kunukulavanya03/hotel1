import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor - add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor - handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Unauthorized - clear token and redirect to login
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Authentication
export const login = async (email, password) => {
  const response = await api.post('/auth/login', { email, password });
  if (response.data.access_token) {
    localStorage.setItem('token', response.data.access_token);
  }
  return response.data;
};

export const register = async (email, username, password) => {
  const response = await api.post('/auth/register', { email, username, password });
  if (response.data.access_token) {
    localStorage.setItem('token', response.data.access_token);
  }
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('token');
  window.location.href = '/login';
};

// API Endpoints
export const api_bookings = async (data) => {
  const response = await api.post('/api/bookings', data);
  return response.data;
};
export const api_bookings_{booking_id} = async (params = {}) => {
  const response = await api.get('/api/bookings/{booking_id}', { params });
  return response.data;
};
export const api_bookings_{booking_id} = async (id, data) => {
  const response = await api.put(`/api/bookings/{booking_id}/${id}`, data);
  return response.data;
};
export const api_bookings_{booking_id} = async (id) => {
  const response = await api.delete(`/api/bookings/{booking_id}/${id}`);
  return response.data;
};
export const api_customers = async (params = {}) => {
  const response = await api.get('/api/customers', { params });
  return response.data;
};
export const api_customers = async (data) => {
  const response = await api.post('/api/customers', data);
  return response.data;
};
export const api_rooms = async (params = {}) => {
  const response = await api.get('/api/rooms', { params });
  return response.data;
};

export default api;
