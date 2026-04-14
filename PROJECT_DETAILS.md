# Project Documentation: Minimal Notes App

A professional, minimal, and fully functional Note-Taking application built as a full-stack web application.

---

## 🚀 Technologies Used

### Frontend (Client-Side)
- **HTML5**: Provides the semantic structure of the web pages.
- **CSS3**: Custom styling for smooth fade-in animations, hover effects, and a modern Slate & Azure color palette.
- **Bootstrap 5**: A responsive CSS framework used for the grid system, buttons, cards, and the **Edit Modal** component.
- **JavaScript & jQuery**: used for DOM manipulation and handling user interactions (clicks, searches).
- **AJAX**: Performed via jQuery to make asynchronous HTTP requests to the backend without reloading the page.

### Backend (Server-Side)
- **Django Framework**: A high-level Python web framework used for routing, server-side logic, and database management.
- **Django ORM**: Used to interact with the database using Python objects instead of raw SQL queries.
- **SQLite**: A lightweight, file-based SQL database used for storing and retrieving notes.

---

## 📑 Project Structure

```text
mini_notes/
├── manage.py            # Django project entry point
├── db.sqlite3           # SQLite Database file
├── notes_project/       # Project Configuration
│   ├── settings.py      # Database and App settings
│   ├── urls.py          # Main URL routing
│   ├── wsgi.py          # Web Server Gateway Interface
│   └── asgi.py          # Asynchronous Server Gateway Interface
└── myapp/               # Application Logic
    ├── models.py        # Database Schema (Note model)
    ├── views.py         # Request handling and API logic
    ├── urls.py          # App-specific URL patterns
    └── templates/       # Frontend files
        └── index.html   # Main single-page interface
```

---

## 📡 RESTful API Endpoints

The frontend interacts with the backend entirely through these JSON-based endpoints:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/notes/` | Retrieves a list of all notes, ordered by newest first. |
| **POST** | `/api/add/` | Creates a new note. Expects JSON: `{"content": "..."}`. |
| **POST** | `/api/update/<id>/` | Updates an existing note by ID. Expects JSON: `{"content": "..."}`. |
| **DELETE** | `/api/delete/<id>/` | Permanently deletes a note by its ID. |

---

## 🛠️ Dynamic Interactions (AJAX)

The application utilizes **Asynchronous JavaScript and XML (AJAX)** for a "Single-Page Application" (SPA) feel.

1.  **Loading Notes**: On page load, an AJAX `GET` request is sent to `/api/notes/`. The response data is used to dynamically build the note cards using jQuery.
2.  **Adding/Editing**: When a user clicks "Add" or "Save Changes", a `POST` request is sent with the new content. Upon success, the list is refreshed via AJAX without a full page reload.
3.  **Deleting**: Clicking "Delete" triggers a `DELETE` request. The card is removed from the view instantly after the backend confirms deletion.
4.  **Searching**: A client-side jQuery function filters the existing HTML note cards based on the text entered in the search bar.

---

## ⚙️ How to Run Locally

1.  **Install Django**:
    ```bash
    pip install django
    ```
2.  **Set up Database**:
    ```bash
    python manage.py migrate
    ```
3.  **Run Server**:
    ```bash
    python manage.py runserver
    ```
4.  **Access App**:
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in any modern browser.
