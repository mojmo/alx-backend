#!/usr/bin/env python3

"""
A simple Flask application with basic internationalization
(i18n) configuration.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """The configuration class for the Flask application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world() -> str:
    """Renders the '4-index.html' template and returns the response.

    This function is the main entry point for the web application. It
    handles the root URL ('/') and returns the rendered output of the
    '4-index.html' template.

    Returns:
        str: The rendered HTML content from the template.
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """Returns the locale from the request.

    Returns:
        str: The locale from the request.
    """

    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run()
