This is a project template for Django 1.7+ (tested with 1.7 and 1.8).

You can use this bash script for one-command initialization of the project

::

    curl -L https://gist.githubusercontent.com/Alexx-G/4dafed44959756f45469/raw/394c2bda3d396b1b7d66d62aee2cb35ddc788bc8/django-startproject.sh | bash

or follow next steps:

    1. Create project's folder;
    2. Install and activate virtualenv;
    3. Install django;
    4. Create project;
    5. Install requirements.

::

    $ mkdir your_project; cd your_project
    $ virtualenv venv; source venv/bin/activate
    $ pip install django
    $ django-admin startproject --template=https://github.com/Alexx-G/django-project-template/archive/master.zip your_project
    $ pip install -r your_project/requirements/development.txt


This template provides some additional features:
    * Configured logging and helper to obtain logger,
    * Deployment-friendly structure of the project,
    * Transparent and organized structure of the project.
