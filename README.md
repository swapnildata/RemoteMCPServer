Steps for Local Server:
- create a empty folder and create a local mcp server in it.
- open the folder in vs code.
- install uv using pip:- pip install uv
- Uv init .
- uv add fastmcp
- uv run fastmcp dev main.py

Steps for remote server on fastmcp cloud:
- create a git repo and add this folder in repo:
  1. git init
  2. git status
  3. git add .
  4. git commit -m 'initial commit'
  5. git remote add origin 'remote url of repo'
  6. git push origin main
- open fastmcp cloud and select the option 'deploy from your code'
- select repo
- click on 'Deploy remote mcp server'
- Modify server name as per requirement and set the entry point main.py or server.py (depending upon server python file name)
- Click on deploy server