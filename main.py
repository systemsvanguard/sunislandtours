'''
Portfolio site for fullstack developer Ryan Hunter | ryan@RyanHunter.org | GitHub handle : SystemsVanguard
'''

# app configuration
import os
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


# app routing
@app.route('/')
def home():
    return render_template('home.html')
	# for testing
	# return "Welcome to Sun Island Tours!"  

@app.route('/tours/')
def tours():
    return render_template('tours.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')


# start web app on port 5000. localhost:5000
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port, debug=True)
	# remember to set debug above to False in production!! 
	
