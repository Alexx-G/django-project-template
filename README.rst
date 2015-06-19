This is a project template for Django 1.6+ (tested with 1.7 and 1.8).

Installation is very simple:
1. Create project's folder;
2. Install and activate virtualenv;
3. Install django;
4. Create project;
5. Install requirements.

::

    $ mkdir your_project; cd your_project
    $ virtualenv venv; source venv/bin/activate
    $ pip install django
    $ django-admin start-project --template= your_project
    $ pip install -r your_project/requirements/development.txt


This template provides some additional features:
* Configured logging and helper to obtain logger,
* Deployment-friendly structure of the project,
* Transparent and organized structure of the project.
