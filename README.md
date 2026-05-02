# FastAPI Blog

A simple blog API built with FastAPI. This project provides a RESTful backend for managing users, blog posts, and authentication.

## Features

- FastAPI-based REST API
- User registration and login
- CRUD operations for blog posts
- JWT authentication support
- Automatic API documentation with Swagger UI

## Requirements

- Python 3.10+
- pip
- virtualenv (recommended)

## Installation

```bash
git clone https://github.com/your-username/Fastapi-Blog.git
cd Fastapi-Blog
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Configuration

Create a `.env` file or set environment variables for any required settings, such as:

- `DATABASE_URL`
- `SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`

## Running the Application

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` in your browser to view the interactive API documentation.

## API Endpoints

Common endpoints include:

- `POST /auth/register` - register a new user
- `POST /auth/login` - authenticate and receive a token
- `GET /posts` - list all posts
- `GET /posts/{id}` - get a single post
- `POST /posts` - create a new post
- `PUT /posts/{id}` - update a post
- `DELETE /posts/{id}` - delete a post

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is released under the MIT License.
