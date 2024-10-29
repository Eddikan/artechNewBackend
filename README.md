Overview
This project is built using FastAPI for the backend, utilizing PostgreSQL as the database. The application provides a RESTful API for managing projects, including features for creating, editing, and deleting project entries.

Features
User authentication with JWT tokens
CRUD operations for projects
Database migrations handled with Alembic
Deployment ready with configuration for Vercel and Supabase
Technologies Used
Backend: FastAPI
Database: PostgreSQL
Database Migrations: Alembic
Deployment: Vercel (for frontend) and Supabase (for database)
Installation Instructions
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Create a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Database Migrations:

bash
Copy code
alembic upgrade head
Start the FastAPI Server:

bash
Copy code
uvicorn app.main:app --reload
Environment Variables
Create a .env file in the root directory of your project and add the following:

env
Copy code

# Database Configuration

DATABASE_URL=postgresql://postgres.lgrxvzsyzsnxdsvijonh:moneymistressmagiC1#@aws-0-us-east-1.pooler.supabase.com:6543/postgres
Make sure to add any additional environment variables needed for your application.

Deployment Details
The backend can be deployed on any cloud provider that supports FastAPI. Ensure your PostgreSQL database is accessible from your server.
For frontend deployment, use Vercel, making sure to configure environment variables as necessary.
