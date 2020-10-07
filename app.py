from flask import Flask, escape, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)

app.secret_key = '\x94\xdf\x08\x97\xf1\xb2\x03\x9c\x8d~\xe7][P\x14\xe6U\xe2}\x81C;h\xf4G\xfa\xf9\xc64I\xec7'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
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
        return redirect(url_for('list_stocks'))

    return render_template('add_stock.html')

@app.route('/stocks')
def list_stocks():
    return render_template('stocks.html')
