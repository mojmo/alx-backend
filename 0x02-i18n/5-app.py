#!/usr/bin/env python3

"""
A simple Flask application with basic internationalization
(i18n) configuration.
"""

from typing import Dict, Union
from flask import Flask, g, render_template, request
import flask
from flask_babel import Babel


class Config(object):
    """The configuration class for the Flask application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def hello_world() -> str:
    """Renders the '5-index.html' template and returns the response.

    This function is the main entry point for the web application. It
    handles the root URL ('/') and returns the rendered output of the
    '5-index.html' template.

    Returns:
        str: The rendered HTML content from the template.
    """
    return render_template('5-index.html')


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


def get_user(user_id: str) -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieves the user information based on the provided ID.

    Args:
        user_id (str): The user ID to retrieve information for.

    Returns:
        dict: The user dictionary if found, otherwise raises a BadRequest exception.
    """

    user_id = int(user_id)

    return users.get(user_id, {})


@app.before_request
def before_request():
    """Sets the locale and timezone for the request."""

    login_as = request.args.get('login_as')

    if login_as:
        g.user = get_user(login_as)


if __name__ == '__main__':
    app.run()
