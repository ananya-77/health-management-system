# Healthcare Vitals Monitoring System

This project is a full-stack web application for monitoring healthcare vitals in real-time. It provides an interactive dashboard for healthcare providers to track patient data and receive alerts when vital signs reach critical levels. The system uses Flask for the backend, Vue.js for the frontend, and MongoDB as the database.

## Features
- Real-time patient monitoring and alerts for critical vitals
- Interactive dashboard with data-driven insights
- Patient profile views with treatment history and health metrics
- Responsive design adaptable across mobile, tablet, and desktop
- Secure cloud-based deployment for healthcare provider access

## Tech Stack
- **Frontend**: Vue.js, HTML, CSS, JavaScript, Bootstrap/Tailwind for styling
- **Backend**: Flask (Python) with REST API
- **Database**: MongoDB
- **Data Processing**: Pandas (Python) for merging and cleaning data
- **Deployment**: Configurable for AWS or Heroku

## Project Structure

1. **`frontend/`** - Contains all frontend files:
   - **`public/`**
     - `index.html` - Main HTML template for the frontend.
   - **`src/`**
     - **`components/`**
       - `PatientProfile.vue` - Vue component for displaying patient profile details.
       - `Dashboard.vue` - Vue component for displaying the dashboard with patient list.
       - `App.vue` - Root Vue component.
     - `router.js` - Vue Router setup for routing between pages.
     - `main.js` - Entry point for the Vue application.
     - `App.vue` - Root Vue component for the app.
   - **`.env`** - Environment variables for the frontend (API base URL).
   - **`package.json`** - NPM dependencies and project configuration file for the frontend.

2. **`backend/`** - Contains all backend files:
   - **`app.py`** - Flask application and API endpoints to serve the data and handle requests.
   - **`load_data.py`** - Script to load and process data from Kaggle datasets using Pandas.
   - **`requirements.txt`** - Python dependencies for the backend project.
   - **`Procfile`** - Heroku deployment configuration for running the app.
   - **`.env`** - Environment variables for the backend (database URI, secret key, etc.).

3. **`README.md`** - Project documentation, including instructions for setup, running the project, and contributing.
   
## Setup Instructions

### Prerequisites
- Node.js and npm for frontend
- Python 3.8+ for backend
- MongoDB for the database

### Backend Setup

1. **Install dependencies**:
   - Navigate to the `backend` directory:
     ```bash
     cd backend
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

2. **Create a `.env` file** in the `backend` directory with the following content:
   ```plaintext
   DATABASE_URI=mongodb://localhost:27017/your_database
   SECRET_KEY=your_secret_key
### Frontend Setup

1. **Install dependencies**:
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install the required Node.js packages:
     ```bash
     npm install
     ```

2. **Create a `.env` file** in the `frontend` directory with the following content:
   ```plaintext
   VUE_APP_API_BASE_URL=http://localhost:5000

### Deployment

1. **Heroku (Backend)**:
   - Ensure the `Procfile` is configured for Heroku deployment.
   - Push the backend to Heroku by following Heroku's [Python deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python).
   
2. **Netlify or Vercel (Frontend)**:
   - Deploy the Vue.js frontend on Netlify or Vercel by connecting your GitHub repository.
   - Follow their respective guides:
     - [Netlify Deployment Guide](https://docs.netlify.com/site-deploys/create-deploys/)
     - [Vercel Deployment Guide](https://vercel.com/docs)

### Usage

1. Navigate to `http://localhost:8080` to access the frontend.

2. Use the interactive dashboard to:
   - View patient profiles.
   - Monitor vitals and receive alerts when values reach critical levels.

3. View individual patient details in the profile section.

# Healthcare Vitals Monitoring System

This project is a full-stack web application for monitoring healthcare vitals in real-time.

### Dashboard 
![Dashboard 1](https://github.com/ananya-77/health-management-system/blob/main/preview/d_1.jpg?raw=true)

![Dashboard 2](https://github.com/ananya-77/health-management-system/blob/main/preview/d_2.jpg?raw=true)

## Patient Profile
![Patient Profile](https://github.com/ananya-77/health-management-system/blob/main/preview/pp.jpg?raw=true)

## Features
- Real-time patient monitoring
- Interactive dashboard for patient profile views
- Alerts for critical vital signs
- Responsive design adaptable across devices








