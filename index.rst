==============================
Python Backend Developer Skills
==============================

Welcome to the Python Backend Developer Skills documentation. This project showcases the skills and proficiency in Python backend development. Below, you'll find detailed information on the project's features, technologies used, and setup instructions.

Overview
--------

This project is a RESTful API built using Flask, a lightweight web framework for Python. It incorporates various backend development concepts and features commonly sought after by employers for Python backend developer roles.

Features
--------

- **RESTful API**: Implements CRUD (Create, Read, Update, Delete) operations for managing resources.
- **Database Integration**: Utilizes SQLite as the database backend for storing and retrieving data.
- **Authentication and Authorization**: Implements user authentication and authorization using JWT (JSON Web Tokens).
- **Testing**: Includes unit tests and integration tests to ensure the reliability and functionality of the application.
- **Documentation**: Utilizes Sphinx for generating documentation, providing clear and comprehensive information about the project's structure, modules, and functionalities.

Technologies Used
-----------------

- Python
- Flask
- SQLite
- JWT (JSON Web Tokens)
- Sphinx (for documentation)

Setup
-----

To set up and run the project locally, follow these steps:

1. Clone the repository:
   ::
   
      git clone https://github.com/kyle-Galloway01/PythonBackendDeveloperSkills.git

2. Navigate to the project directory:
   ::
   
      cd PythonBackendDeveloperSkills

3. Install the dependencies:
   ::
   
      pip install -r requirements.txt

4. Set up the database:
   ::
   
      python manage.py db init
      python manage.py db migrate
      python manage.py db upgrade

5. Run the application:
   ::
   
      python run.py

   Access the API at `http://localhost:5000`.

This documentation provides comprehensive information about the project, including its purpose, features, technologies used, and setup instructions. Feel free to explore the documentation to learn more about the project and its functionalities.

