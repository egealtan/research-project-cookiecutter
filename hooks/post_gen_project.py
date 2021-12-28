help = """
*******************************************************************************
*******************************************************************************
Your project {{cookiecutter.repo_name}} has been created!
*******************************************************************************
*******************************************************************************

1) Manually add data or data/raw to .gitignore if you'd like
2) Check requirements.txt and update to your liking
3) Check Dockerfile and update to your liking
4) Modify .devcontainer/devcontainer.json. By defult, --runtime-nvidia flag is
   used for GPU access.
5) Make sure the extension Remote Containers and Docker are installed on VS 
   Code
6) Run the Docker application (or only the daemon) on your local machine
7) In VS Code, press Ctrl+Shift+P "Remote Containers: Rebuild and Reopen in 
   Container"
8) You should have a working environment! Install your new project in your 
   remote Docker environment with:

   pip install -e .

   Note that the -e flag makes your package editable and '.' is the current 
   directory.
9) Don't forget to initialize your repository!
"""
print(help)
