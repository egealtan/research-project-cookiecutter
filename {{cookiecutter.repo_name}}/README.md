# {{cookiecutter.project_name}}

{{cookiecutter.description}}

---

## Project Structure:

```

├── LICENSE
│ 
├── .devcontainer
│       ├── devcontainer.json
│ 
├── {{cookiecutter.package_name}}
│       ├── __init__.py
│ 
├── data                <- Need to put /data/ in .gitignore
│ 
├── docs
│ 
├── references
│ 
├── results             <- all results, including interim figs, .hd5s, etc.
│       ├── figures     <- Where tidied up figures live
│ 
├── scripts
│ 
├── tests
│
├── .gitignore
│ 
├── Dockerfile
│ 
├── requirements.txt    <- This is read by the Dockerfile
│ 
├── README.md           <- This is read by the Dockerfile
│
├── setup.py            <- Top level readme file.
│   
├── hooks
```