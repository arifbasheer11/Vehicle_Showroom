# Vehicle Inventory Management

A web application for managing vehicle inventory, employees, partners, and related expenses. This project consists of a Django backend and a simple frontend.

## Features
- Vehicle inventory management
- Employee management
- Partner management
- Expense tracking
- User authentication

## Project Structure
```
vehicle_inventory_managament/
  vehicle_inventory_Backend/   # Django backend
    employees/                # Employee management app
    expenses/                 # Expense tracking app
    partners/                 # Partner management app
    users/                    # User authentication app
    vehicles/                 # Vehicle inventory app
    vehicle_inventory/        # Project settings and URLs
    media/                    # Uploaded media files
    manage.py                 # Django management script
  vehicle_inventory_frontend/ # Frontend (HTML, CSS, JS)
    frontend/
      app.js
      index.html
      style.css
```

## Getting Started

### Backend Setup (Django)
1. Navigate to the backend directory:
   ```bash
   cd vehicle_inventory_Backend
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install django djangorestframework
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd vehicle_inventory_frontend/frontend
   ```
2. Open `index.html` in your browser to view the frontend.

## Usage
- Access the backend API at `http://localhost:8000/` (default Django port).
- Use the frontend for interacting with the backend (customize as needed).

## Customization
- Update backend apps to add more features or endpoints.
- Modify frontend files for a better user interface.

## License
This project is for educational purposes. Add your license here if needed.
