Blaskr
======

The minimal blog application from the flask dokumentation under a new
name and with a `.wsgi` file.


What is Blaskr?
---------------

A sqlite powered thumble blog application


How do I use it?
----------------

 1. edit the configuration in the `blaskr.py` file or
    export an `BLASKR_SETTINGS` environment variable
    pointing to a configuration file.

 2. install the app from the root of the project directory

        pip install --editable .

 3. Instruct flask to use the right application

        export FLASK_APP=blaskr

 4. initialize the database with this command:

        flask initdb

 5. now you can run `blaskr`:

        flask run

    the application will greet you on
    http://localhost:5000/


How to use WSGI
---------------
