from app.app import app
from app.database import init

@app.route('/')
def test():
    return "hello"

init()
app.run(debug=True)