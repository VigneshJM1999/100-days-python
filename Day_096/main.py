import os
import requests
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)

API_BASE_URL = 'https://the-one-api.dev/v2'


def make_api_request(endpoint):
    api_key = session.get('api_key')
    if not api_key:
        return None, {'error': 'API key not set in session.'}

    headers = {'Authorization': f'Bearer {api_key}'}
    try:
        response = requests.get(f'{API_BASE_URL}{endpoint}', headers=headers)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 401:
            session.clear()  # Clear session on auth error
            return None, {'error': 'Unauthorized. The API key is likely invalid.'}
        return None, {'error': f'A server error occurred: {err.response.status_code}'}
    except requests.exceptions.RequestException as err:
        return None, {'error': f'Request failed: {err}'}


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        api_key = request.form.get('api_key')
        if not api_key:
            error = 'Please provide an API key.'
        else:
            session['api_key'] = api_key
            return redirect(url_for('index'))

    if 'api_key' not in session:
        return render_template('index.html', view='apikey', error=error)

    view = request.args.get('view', 'characters')
    data = None

    if view == 'characters':
        api_data, api_error = make_api_request('/character?limit=200&sort=name:asc')
        if api_error:
            error = api_error['error']
        else:
            data = api_data.get('docs')

    elif view == 'movies':
        api_data, api_error = make_api_request('/movie')
        if api_error:
            error = api_error['error']
        else:
            data = api_data.get('docs')

    elif view == 'quote':
        quotes_data, api_error = make_api_request('/quote?limit=2000')
        if api_error:
            error = api_error['error']
        elif quotes_data and quotes_data.get('docs'):
            random_quote = random.choice(quotes_data['docs'])
            char_id = random_quote.get('character')
            char_data, char_error = make_api_request(f'/character/{char_id}')
            if char_error:
                random_quote['characterName'] = 'Unknown Character'
            else:
                random_quote['characterName'] = char_data['docs'][0]['name'] if char_data[
                    'docs'] else 'Unknown Character'
            data = random_quote

    return render_template('index.html', view=view, data=data, error=error)


@app.route('/character/<character_id>')
def character_details(character_id):
    if 'api_key' not in session:
        return redirect(url_for('index'))

    error = None
    char_data, char_error = make_api_request(f'/character/{character_id}')
    quotes_data, quotes_error = make_api_request(f'/character/{character_id}/quote')

    if char_error:
        error = char_error['error']
        return render_template('index.html', view='character_detail', error=error)

    character = char_data['docs'][0] if char_data and char_data['docs'] else None
    quotes = quotes_data['docs'] if quotes_data and quotes_data['docs'] else []

    if quotes_error and not error:
        error = quotes_error.get('error')

    return render_template('index.html', view='character_detail', character=character, quotes=quotes, error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)