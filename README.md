# fastapi_mongodb_user_management
three api using fast api and mongodb Api are :  Create user View/get user List user edit users details And delete user (optional)
# FastAPI MongoDB User Management

A simple user management application built with FastAPI and MongoDB. This application provides APIs to create, view, list, update, and delete user information.

## Features

- Create a new user
- View user details by ID
- List all users
- Update user details
- Delete a user (optional)

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **MongoDB**: A NoSQL database for storing user data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI server for running the FastAPI application.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- MongoDB (either locally installed or using MongoDB Atlas)
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   cd fastapi_mongodb_user_management
2. Install Required Packages:

  pip install fastapi uvicorn pymongo pydantic

3. Run the FastAPI Application:

  uvicorn main:app --reload

4. Access the API Documentation
   http://127.0.0.1:8000/docs to see the interactive API documentation.  
