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

### Grafana (`grafana/` and `grafana_data`)
- `grafana`:
  - `dashboards`: Containts .json dashsboards to import.
  - `grafan.ini`: Configuration SMTP file for alerts.
- `grafana_data`: To initialize volumen.

### Prometheus (`prometheus_data`):
- `prometheus_data`:
  - `prometheus.yml`: Prometheus configuration file,

### Docs (`docs/`):
- `docs`: Contains Markdowns with the contributions of each member.


## Requirements

For this project we are using [Python >= 3.12](https://www.python.org/downloads/) and [Docker Engine >= 27](https://docs.docker.com), it is not test in other versions.

## Setup and Installation

Due we are using `pygame` for our projectm we only used Docker for the backend, so you will need to setup and python enviroment a build the containers wiht `docker compose`

Using `run.sh` file

1. Activate permissioons for `run.sh` file.
  
```
chmod +x ./run.sh
```

2. Run the script file.

```
sudo ./run.sh
```

Enjoy our game.


Manually setup.

1. First, create a `grafana_data` directory:

```
mkdir grafa_data
```

2. Now let's build our containers.
```
docker compose up --build -d
```

This commando builds our container in `compose.yml`.
```
Our container:
  prometheus        
  mongodb           
  mongodb_exporter  
  grafana            
  backend         
```

If you want to see any container's log, you cand execute:
```
docker compose logs <container_name>
```

Once it is completed our backend at `localhost:8000`, let's to initialize our game.

1. Let's create a python enviroment:
```
python3 -m venv venv
```

2. Activate it, if you are in linux run this:
```
source venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```


4. Finished, let's enjoy our game:
```
python3 src/app/main.py
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

