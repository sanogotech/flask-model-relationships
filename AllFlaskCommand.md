
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

    > set FLASK_APP=hello.py
    > set FLASK_ENV=development
    > flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  bootstrap  Populates database with data
  db         Perform database migrations.
  initdb     Drops and Creates fresh database
  routes     Show the routes for the app.
  run        Run a development server.
  shell      Run a shell in the app context.