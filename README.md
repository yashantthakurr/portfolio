# Developer Portfolio

A personal portfolio showcasing my software development journey, technical skills, projects, professional experience, and certifications. Built to present my work and provide a simple way to connect with me.

## About

I'm a software developer focused on building backend systems and RESTful APIs using **Python, FastAPI, Java, and Spring Boot**. I enjoy working with databases, implementing secure authentication, and exploring ways to build reliable and performant applications.

This portfolio serves as a central place to explore my projects, technical expertise, experience, and certifications.

## Features

- **About Me** — An introduction to my background and development interests.
- **Technical Skills** — Technologies, frameworks, databases, and tools I work with.
- **Experience** — Professional experience and development work.
- **Projects** — A collection of projects demonstrating my technical skills and problem-solving abilities.
- **Certifications** — Relevant certifications and achievements.
- **Contact Form** — A way to get in touch with me through the backend API.
- **Responsive Design** — A dark-themed interface designed for desktop and mobile devices.

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- HTML5 & CSS3

### Backend
- Python
- FastAPI
- REST APIs
- Pydantic

### Databases & Tools
- PostgreSQL
- Redis
- Git & GitHub

*The technologies listed above reflect the portfolio's intended stack; adjust them if the current implementation differs.*

## Architecture

The portfolio uses a frontend-backend architecture, with the React application communicating with a FastAPI backend over HTTP.

```text
React Frontend
      |
      | HTTP Requests
      v
FastAPI Backend
      |
      v
Database
```

Projects, certifications, and professional experiences are intended to be retrieved from the backend rather than maintained as hardcoded frontend records. Contact form submissions are also handled through the backend API.

## Getting Started

### Prerequisites

- Node.js and npm
- Access to the FastAPI backend

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd <your-project-folder>
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Create a `.env` file in the frontend project root and configure the backend URL using the environment variable expected by your application.

   For a Vite application, an example is:

   ```env
   VITE_API_BASE_URL=http://localhost:8000
   ```

   Replace the URL with your deployed backend URL when deploying the portfolio.

4. Start the development server:

   ```bash
   npm run dev
   ```

5. Open the local URL printed in your terminal.

## Backend Configuration

The backend must be running and accessible to the frontend.

Before deploying, ensure that:

- The API base URL points to the correct backend environment.
- FastAPI CORS settings permit requests from the deployed frontend origin.
- The required API endpoints are available.
- Production environment variables are configured correctly.

Never commit secret keys, passwords, or other sensitive credentials to the repository.

## Deployment

The frontend and backend can be deployed independently.

Configure the frontend's production environment variables to point to the deployed FastAPI API. Ensure the backend allows requests from the production frontend origin.

## Future Improvements

- Add automated frontend and API integration tests.
- Improve accessibility and loading-state handling.
- Introduce additional backend-driven portfolio features.
- Continue refining performance and user experience.

## Connect With Me

- **GitHub:** [Your GitHub Profile](https://github.com/)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/)
- **Portfolio:** [Live Website](#)

---

Built with curiosity, consistency, and a passion for software development.