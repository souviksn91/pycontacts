# PyConects - A Contact Manager App
PyContacts is a lightweight Flask web app that lets you manage contacts, organize them into categories, search easily, and perform all basic CRUD operations.

![Image](https://github.com/user-attachments/assets/01ba76c1-1470-44fe-b5c8-7aef465998fe)

## Features
- Add, view, edit, and delete contacts
- Organize contacts into groups (e.g. Family, Friends, Work)
- Search for contacts by name, email, or phone
- Pagination support for browsing large contact lists
- Clean and responsive interface using Bootstrap
- MySQL support (easily configurable)

## Technologies
- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL

<hr>

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/souviksn91/pycontacts.git
   cd pycontacts
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
    Create MySQL database (see DATABASE.md)

5. **Run the app:**
   ```bash
   python app.py
   ```
6. **Access in browser:**
   http://127.0.0.1:5000/
   