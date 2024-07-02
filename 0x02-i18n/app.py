#!/usr/bin/env python3

"""
A simple Flask application with basic internationalization
(i18n) configuration.
"""

from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz


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
def index() -> str:
    """Renders the 'index.html' template and returns the response.

    This function is the main entry point for the web application. It
    handles the root URL ('/') and returns the rendered output of the
    'index.html' template.

    Returns:
        str: The rendered HTML content from the template.
    """
    return render_template('index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Selects the locale based on user preference and request context.

    This function prioritizes the following strategies for locale selection:
        1. User locale from flask.g.user (if set)
        2. Locale from URL parameter ('locale')
        3. Best matching locale from request headers (Accept-Language)
        4. Default locale (from Flask configuration)

    Returns:
        str: The selected locale code.
    """

    # 1. Locale from URL parameter (highest priority)
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    # 2. User locale
    if g.user is not None and 'locale' in g.user:
        user_locale = g.user.get('locale')
        if user_locale in Config.LANGUAGES:
            return user_locale

    # 3. Locale from request headers
    locale = request.headers.get('locale', None)
    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieves the user information.

    Returns:
        dict: The user dictionary if found.
    """

    user_id = request.args.get('login_as')

    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """Sets the locale and timezone for the request."""

    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone():
    """
    Selects the timezone based on user preference and request context.

    This function prioritizes the following strategies for timezone selection:
        1. User timezone from flask.g.user (if set)
        2. Timezone from URL parameter ('timezone')
        3. Default timezone (from Flask configuration)

    Returns:
        str: The selected timezone code.
    """

    # 1. Timezone from URL parameter (highest priority)
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 2. User timezone
    if g.user is not None and 'timezone' in g.user:
        try:
            user_timezone = g.user.get('timezone')
            if user_timezone:
                return pytz.timezone(user_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE


if __name__ == '__main__':
    app.run()
