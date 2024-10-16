# Tank Turn Game

## Description

Tank Turn Game is a multiplayer tank battle game built with Python and Pygame. Players control tanks, taking turns to move, aim, and shoot at each other. The game features different types of tanks, player statistics, and a backend server for user authentication and data persistence.

### Team Members
- Pacheco André - 20222189G
- Pezo Sergio - 20224087G
- Torres Oscar - 20210153B

## Project Structure

The project is divided into two main parts: the game client and the backend server.

### Game Client (`src/`)
- `main.py`: Entry point for the game client
- `app/`: Main application directory
  - `core/`: Core game logic (game manager, object controller)
  - `models/`: Game object models (tanks, bullets)
  - `views/`: Game views (menu, stats, game)
  - `util/`: Utility functions
  - `config.py`: Client configuration

### Backend Server (`backend/`)
- `src/`: Source code for the backend
  - `app/`: Main application directory
    - `database/`: Database connection and queries
    - `models/`: Data models
    - `routes/`: API routes
    - `services/`: Business logic
    - `main.py`: Entry point for the backend server
  - `tests/`: Backend tests
  - `features/`: Behavior-driven development features

## Setup and Installation

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the MongoDB database and backend server with docker compose
    ```
    docker compose up --build -d
    ```
4. Run the game client:
   ```
   cd src
   python main.py
   ```

## Development

- The project uses pre-commit hooks for code formatting (Black)
- Backend tests can be run using pytest 
- Behavior-driven development tests are implemented using Behave

## CI/CD

The project includes a GitHub Actions workflow (`ci.yml`) for continuous integration, which runs tests and checks code formatting.

## Documentation

For detailed information, please refer to the following documentation:
- [Answers](./docs/ANSWERS.md): Answer for Midterm Exam.
