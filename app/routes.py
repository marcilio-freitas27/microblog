from app import app

# decorators
@app.route('/')
@app.route('/index')
# views functions
def index():
    return "Hello, World!"
