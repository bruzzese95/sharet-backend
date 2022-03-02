## Prerequisites
Having poetry installed

## Run from CL
In the root of the project:
```
poetry run python main.py
```

## Run into VSCode
Select as Python Interpreter the result of the following command in the root of the project
```
poetry env info
```
Run exploiting following _launch.json_:
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI-ShareT",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal"
        }
    ]
}
```
