# Food Recipe Web Application - Frontend

This is the frontend component of the Food Recipe web application, built using React.js and Bootstrap. It provides a user interface for browsing, searching, and viewing detailed information about various recipes.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Custom Layout Design](#custom-layout-design)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Browse Recipes**: View a list of recipes with images, descriptions, and links to detailed views.
- **Search Recipes**: Use a search bar to filter recipes based on keywords.
- **View Recipe Details**: View detailed information about a recipe, including ingredients and instructions.
- **Responsive Design**: The application is fully responsive and works well on both desktop and mobile devices.
- **Unique Layout**: The recipe details page features a custom design with overlapping elements, shadowed images, and an elegant text overlay.

## Technology Stack

- **Frontend**: React.js, Bootstrap
- **API Client**: Axios
- **Routing**: React Router
- **State Management**: React Hooks (`useState`, `useEffect`)

## Installation

To set up the frontend locally, follow these steps:

Navigate to the Backend Directory:
```bash
cd food-recipe-backend
```

Create a Virtual Environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
Install Dependencies:
```bash
pip install -r requirements.txt
```
Run Migrations:
```bash
python manage.py migrate
```
Start the Backend Server:
```bash
python manage.py runserver
```
## Usage
Once the backend server is running, the API will be available at http://127.0.0.1:8000/api/.

### API Endpoints
- GET /api/recipes/: Retrieve a list of all recipes.
- GET /api/recipes/id/: Retrieve details of a specific recipe.
  
## Example Response
```json
{
  "id": 1,
  "name": "Spaghetti Bolognese",
  "description": "A classic Italian pasta dish.",
  "ingredients": "Spaghetti, Ground Beef, Tomato Sauce, Garlic, Onions, Olive Oil",
  "instructions": "Cook the spaghetti. Prepare the sauce by sautéing garlic and onions...",
  "image": "https://example.com/images/spaghetti.jpg"
}
```
