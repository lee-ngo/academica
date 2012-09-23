"""\
Academica

The academic site.
"""

from flask import Flask, render_template

__version__ = '0.1'


# Flask application
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('default_config')
# Configuration, using development when run locally, overridden by ENV
if __name__ == '__main__':
    app.config.from_pyfile('dev_config.py', silent=True)
app.config.from_envvar('SETTINGS_MODULE', silent=True)


#Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view')
def view():
    return render_template('view.html')


@app.route('/<username>')
def profile(username):
    # TODO: Use real data
    return render_template('profile.html', user={
        'first': 'Lee',
        'last': 'Ngo',
        'email': 'lee.ngo@gmail.com',
        'phone': '412-555-5555',
        'hours': 'I NEVER SLEEP',
        'available': True,
        'education': 'TODO',    # HTML
        'positions': 'TODO',    # HTML
    })


# Run development server with the development settings
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug != False)
