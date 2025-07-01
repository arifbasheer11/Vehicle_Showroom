const API_ENDPOINTS = {
  vehicles: 'http://127.0.0.1:8000/api/vehicles/',
  users: 'http://127.0.0.1:8000/api/users/',
  'vehicle-types': 'http://127.0.0.1:8000/api/vehicle-types/',
  maintenance: 'http://127.0.0.1:8000/api/maintenance/'
};
const TOKEN_URL = 'http://127.0.0.1:8000/api/token/';

const container = document.getElementById('data-container');
const loginForm = document.getElementById('login-form');
const logoutBtn = document.getElementById('logout-btn');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const errorMessage = document.getElementById('error-message');

let currentFeature = 'vehicles';

function showLogout() {
  logoutBtn.style.display = '';
  usernameInput.style.display = 'none';
  passwordInput.style.display = 'none';
  loginForm.querySelector('button[type="submit"]').style.display = 'none';
}

function showLogin() {
  logoutBtn.style.display = 'none';
  usernameInput.style.display = '';
  passwordInput.style.display = '';
  loginForm.querySelector('button[type="submit"]').style.display = '';
}

function renderTable(data, feature) {
  if (!Array.isArray(data) || data.length === 0) {
    container.textContent = `No ${feature} found.`;
    return;
  }
  let html = '<table border="1" cellpadding="6" style="border-collapse:collapse; width:100%;">';
  html += '<thead><tr>';
  // Table headers based on feature
  if (feature === 'vehicles') {
    html += '<th>License Plate</th><th>Type</th><th>Driver</th><th>Make</th><th>Model</th><th>Year</th><th>Color</th><th>Fuel</th><th>Status</th>';
  } else if (feature === 'users') {
    html += '<th>Username</th><th>Email</th><th>First Name</th><th>Last Name</th><th>Is Active</th>';
  } else if (feature === 'vehicle-types') {
    html += '<th>ID</th><th>Name</th><th>Description</th>';
  } else if (feature === 'maintenance') {
    html += '<th>ID</th><th>Vehicle</th><th>Description</th><th>Date</th><th>Cost</th>';
  }
  html += '</tr></thead><tbody>';
  data.forEach(item => {
    if (feature === 'vehicles') {
      html += `<tr><td>${item.license_plate || ''}</td><td>${item.vehicle_type?.name || ''}</td><td>${item.assigned_driver?.username || ''}</td><td>${item.make || ''}</td><td>${item.model || ''}</td><td>${item.year || ''}</td><td>${item.color || ''}</td><td>${item.fuel_type || ''}</td><td>${item.status || ''}</td></tr>`;
    } else if (feature === 'users') {
      html += `<tr><td>${item.username || ''}</td><td>${item.email || ''}</td><td>${item.first_name || ''}</td><td>${item.last_name || ''}</td><td>${item.is_active ? 'Yes' : 'No'}</td></tr>`;
    } else if (feature === 'vehicle-types') {
      html += `<tr><td>${item.id || ''}</td><td>${item.name || ''}</td><td>${item.description || ''}</td></tr>`;
    } else if (feature === 'maintenance') {
      html += `<tr><td>${item.id || ''}</td><td>${item.vehicle || ''}</td><td>${item.description || ''}</td><td>${item.date || ''}</td><td>${item.cost || ''}</td></tr>`;
    }
  });
  html += '</tbody></table>';
  container.innerHTML = html;
}

function fetchData(token, feature) {
  container.textContent = 'Loading data...';
  errorMessage.textContent = '';
  const url = API_ENDPOINTS[feature];
  fetch(url, {
    headers: {
      'Authorization': 'Bearer ' + token
    }
  })
    .then(response => {
      if (response.status === 401) throw new Error('Unauthorized. Please log in again.');
      if (!response.ok) throw new Error('Network response was not ok');
      return response.json();
    })
    .then(data => {
      // If paginated, use data.results; else use data directly
      if (data && Array.isArray(data.results)) {
        renderTable(data.results, feature);
      } else if (Array.isArray(data)) {
        renderTable(data, feature);
      } else {
        container.textContent = `No ${feature} found.`;
      }
    })
    .catch(error => {
      container.textContent = '';
      errorMessage.textContent = 'Error fetching data: ' + error.message;
    });
}

function handleLogin(e) {
  e.preventDefault();
  errorMessage.textContent = '';
  const username = usernameInput.value;
  const password = passwordInput.value;
  fetch(TOKEN_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  })
    .then(res => res.json())
    .then(data => {
      if (data.access) {
        localStorage.setItem('access_token', data.access);
        showLogout();
        fetchData(data.access, currentFeature);
      } else {
        errorMessage.textContent = 'Login failed: ' + (data.detail || 'Invalid credentials');
        container.textContent = 'Please log in to view data.';
      }
    })
    .catch(() => {
      errorMessage.textContent = 'Login request failed. Check your network connection.';
      container.textContent = 'Please log in to view data.';
    });
}

function handleLogout() {
  localStorage.removeItem('access_token');
  showLogin();
  container.textContent = 'Please log in to view data.';
  errorMessage.textContent = '';
}

loginForm.addEventListener('submit', handleLogin);
logoutBtn.addEventListener('click', handleLogout);

// Navigation event listeners
['vehicles', 'users', 'vehicle-types', 'maintenance'].forEach(feature => {
  const btn = document.getElementById('nav-' + feature);
  if (btn) {
    btn.addEventListener('click', () => {
      currentFeature = feature;
      const token = localStorage.getItem('access_token');
      if (token) {
        fetchData(token, feature);
      } else {
        container.textContent = 'Please log in to view data.';
      }
    });
  }
});

// On page load, check for token
const token = localStorage.getItem('access_token');
if (token) {
  showLogout();
  fetchData(token, currentFeature);
} else {
  showLogin();
} 
