# ML project with Docker
This project helps as a baseline for building a general Machine Learning Project that uses Docker. It can be integrated with the DevContainers extension in VS Code. The project implements:

1) **Docker integration:** Implements a simple devcontainer folder that can be used to build a Docker image using the DevContainers extension from VS Code. It also implements a basic Dockerfile that allows for installing a basic Python version, installing all dependencies in a requirements.txt file in the same folder.
2) **Pre-Commits:** Implements a general pre-commit structure to get instant webhooks using a few libraries that I consider essential: *black*, *isort*, *bandit* and *interrogate*. More can be added using the pre-commit yaml file in the main directory.
3) **.gitignore:** Uses a base .gitignore with things that you generally don't want to publish to a github repository, so that I don't forget to implement them.
