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

 1. Log in to your server, and the clone the blaskr git repo

        git clone https://github.com/kfl/blaskr.git

 2. Activate your virtual environment, say with the command

        source venv/bin/activate

 3. Go to the blaskr dir, and install blaskr

        pip install .

 4. Initialize the database with the commands:

        export FLASK_APP=blaskr
        flask initdb

 5. Go to your home directory, and make sure that the webserver can write to the database

        chmod g+rw `find venv -name blaskr.db`
        chown :www-data `find venv -name blaskr.db`
        chown :www-data `find venv -type d -name blaskr.db`
        chmod g+rw `find venv -type d -name blaskr`

 6. Copy the file `blaskr.wsgi` to your `public_html` folder, and edit
    the path to your virtual environment in the top of the file (see
    `debug_blaskr.wsgi` for how to get debug information).

 7. Enjoy blaskr in your browser
