
# Library Information System (LIS)

## Overview

The **Library Information System (LIS)** is a web application built for managing a library's book collection, including the ability to add, view, and issue books. It allows librarians to easily manage available books and track issued books. The system is designed using **Django** as the backend framework, with HTML, CSS, and JavaScript for the frontend.

This project is a part of the **Software Development Life Cycle (SDLC)** plan for a library management system aimed at simplifying library operations and improving user experience.

## Features

- **Add Books**: Admins can add new books to the library with details like title, author, and available copies.
- **Issue Books**: Users can issue books from the library, tracking the available copies.
- **View Book List**: The system displays the list of books available, their authors, and the number of available copies.
- **Responsive UI**: The system provides a responsive user interface that adapts to different screen sizes for both desktop and mobile users.

## Tech Stack

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (or any other database you prefer with Django configurations)
- **Version Control**: Git, GitHub

## Project Structure

The project contains the following main parts:

- **Models**: Django models to define the structure of the database tables, including `Book` with fields like `title`, `author`, `available_copies`.
- **Views**: Views to handle the logic for rendering book lists, adding books, and issuing books.
- **Templates**: HTML templates to render book data dynamically. This includes:
  - `base.html` for the base structure.
  - `book_list.html` for displaying available books.
  - `add_book.html` for adding new books to the library.
  - `issue_book.html` for issuing books.
- **CSS**: Custom CSS for styling the UI with a simple, clean, and responsive design.
- **URLs**: URL routing for different views such as adding and issuing books.

## Installation

### Prerequisites

- Python 3.x
- Django (can be installed via pip)
- Git (for version control)

### Steps to Set Up

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/JoyeuxShalom/Library_App.git
   cd Library_App
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the system through the homepage where you can view the list of books.
- Add new books using the "Add New Book" link.
- Issue books from the available list.
- Access the admin panel to manage books and users (by logging in with the superuser account).

## Contributing

Feel free to fork this repository, make changes, and create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- **Django Setup**: Make sure your Django project settings are properly configured, including database settings and static files handling.
- **Frontend Enhancements**: You can further enhance the UI/UX by integrating frameworks like Bootstrap or adding JavaScript for more dynamic features.
