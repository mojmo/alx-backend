#!/usr/bin/env python3

"""A simple Flask application that renders an index template."""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Renders the '0-index.html' template and returns the response.

    This function is the main entry point for the web application. It
    handles the root URL ('/') and returns the rendered output of the
    '0-index.html' template.

    Returns:
        str: The rendered HTML content from the template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
