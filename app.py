from flask import Flask, escape, render_template, request, session, redirect, url_for, flash
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app.secret_key = '\x94\xdf\x08\x97\xf1\xb2\x03\x9c\x8d~\xe7][P\x14\xe6U\xe2}\x81C;h\xf4G\xfa\xf9\xc64I\xec7'
# Remove the default logger configured by Flask
app.logger.removeHandler(default_handler)

# Logging Configuration
file_handler = RotatingFileHandler('flask-stock-portfolio.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Log that the Flask application is starting
app.logger.info('Starting the Flask Stock Portfolio App...')

@app.route('/')
def index():
    app.logger.info('Calling the index() function.')
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    flash('Thanks for learning about this site!', 'info')
    return render_template('about.html')

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'

@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Save the form data to the session object
        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']

        flash(f"Added new stock ({ request.form['stock_symbol'] })!", 'success')

        app.logger.info(f"Added new stock ({ request.form['stock_symbol'] })!")

        return redirect(url_for('list_stocks'))

    return render_template('add_stock.html')

@app.route('/stocks')
def list_stocks():
    return render_template('stocks.html')
