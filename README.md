# Python Backend Developer Skills Showcase

Welcome to my Python Backend Developer Skills Showcase repository! This project is designed to demonstrate my skills and proficiency in Python backend development. Below, you'll find information on how to set up and run the project, as well as an overview of its features and technologies used.

## Overview

This project is a RESTful API built using Flask, a lightweight web framework for Python. It incorporates various backend development concepts and features commonly sought after by employers for Python backend developer roles.

## Features

- **RESTful API**: Implements CRUD (Create, Read, Update, Delete) operations for managing resources.
- **Database Integration**: Utilizes SQLite as the database backend for storing and retrieving data.
- **Authentication and Authorization**: Implements user authentication and authorization using JWT (JSON Web Tokens).
- **Testing**: Includes unit tests and integration tests to ensure the reliability and functionality of the application.
- **Documentation**: Utilizes Sphinx for generating documentation, providing clear and comprehensive information about the project's structure, modules, and functionalities.

## Technologies Used

- Python
- Flask
- SQLite
- JWT (JSON Web Tokens)
- Sphinx (for documentation)

## Setup

```markdown
## Setup

To set up and run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/kyle-Galloway01/PythonBackendDeveloperSkills.git
   ```

2. Navigate to the project directory:
   ```bash
   cd PythonBackendDeveloperSkills
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

5. Run the application:
   ```bash
   python run.py
   ```

6. Access the API at `http://localhost:5000`.
```


