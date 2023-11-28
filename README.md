# Love Checklists CLI

A simple and intuitive CLI app to manage your daily tasks with ease. Keep track of your tasks, mark them as complete, and manage your productivity effectively.

## Reminders

- Ensure you have Python 3 installed on your system
- Navigate to the directory containing the `run.py` file 
- run the following command in your terminal: 'python3 run.py'

## Features

### Current Functionality

- **Task Viewing**: A single consolidated location of all tasks, with a clear indication of those already completed and those still pending.
- **Task Addition**: Add new tasks to the  list as needed.
- **Task Completion**: Easily mark tasks as completed.

### Potential Furture Enhancements

- Grouping of tasks for better organization. i.e. Health category, Logistics Category, Study Category and so on.


## Data Model

This app uses a simple list of dictionaries to manage each task, with each task being a dictionary containing task information. This is admittedly a lightweight approach, allowing for quick interactions and edits if needed.

## Testing

- All code passed and verified by running the code through a PEP8 linter with no errors reported.
- Tested in my local terminal as well as the Heroku terminal.

## Bugs

### Solved Bugs

During testing an error was encountered at line 63 the following error "line too long (86 > 79 characters)". To resolve this I shortened the enclosed string in the associated print statement to return "marked done"  instead of "marked as completed"

### Remaining Bugs

None

### Validator Testing

- Pep8: No errors were returned from https://pep8ci.herokuapp.com/#

## Deployment

This project app was deployed using the Code Institute's mock terminal for Heroku.

- Steps for deployment
    - Clone this repository.
    - Create a new Heroku app.
    - Set the build-packs to Python and NodeJS, with Python appearing on top and Node JS below.
    - Link Heroku app to the repository
    - Click 'Deploy'

## Credits

- Code Institie for the deployment terminal
- https://www.jdoodle.com/python3-programming-online/ as a useful online IDE whilst encountering connectivity issues with GitPod.
- Portfolio Project 3 Scope video for guidance on appropriate README.md file structure

