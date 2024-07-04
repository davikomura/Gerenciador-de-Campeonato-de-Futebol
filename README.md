# Championship Management System

This project is a Python-based system for managing and simulating a championship league across multiple divisions. It includes functionalities for processing data, managing the championship structure, and simulating matches.

## Project Structure

The project structure is organized into several directories:

- `main.py`: Entry point for executing the championship management system.
- `LICENSE`: License information for the project.
- `README.md`: This file, providing an overview of the project.
- `requirements.txt`: List of Python dependencies required for the project.
- `.vscode/settings.json`: VS Code specific settings for the project.

### Directories

- `data/`: Contains `data.json` file with information about teams and their respective levels.
- `data_processing/`: Python module for processing data, including reading and parsing `data.json`.
- `championship_management/`: Module for managing the championship structure, including promotion and relegation logic.
- `simulator/`: Module for simulating matches and generating league tables.

### Usage

1. **Setup:**
   - Clone the repository: `git clone https://github.com/davikomura/championship-management.git`
   - Navigate into the project directory: `cd championship-management`
   - Install dependencies: `pip install -r requirements.txt`

2. **Running the Championship Management System:**
   - Execute `main.py` to start the system: `python main.py`

3. **Functionality:**
   - **Data Processing:** Parses `data.json` to retrieve team information.
   - **Championship Management:** Manages the structure of the championship, including divisions, promotion, and relegation.
   - **Simulation:** Simulates matches and generates league tables based on predefined team data.

### Dependencies

Ensure you have Python 3.x installed. Install required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

### Authors

- [Davi Komura](https://github.com/davikomura) - Software Engineer