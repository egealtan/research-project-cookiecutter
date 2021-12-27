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
│       ├── data            <- Data making code
│       ├── visualization   <- Data visualization code
│       ├── models          <- Code that houses all models
│ 
├── data                    <- Need to put /data/ in .gitignore
│ 
├── docs
│ 
├── references
│ 
├── results                 <- all results, including interim figs, .hd5s, etc.
│       ├── figures         <- Where tidied up figures live
│ 
├── scripts
│ 
├── tests
│
├── .gitignore
│ 
├── Dockerfile
│ 
├── requirements.txt        <- This is read by the Dockerfile
│ 
├── README.md               <- This is read by the Dockerfile
│
├── setup.py                <- Top level readme file.
│   
```