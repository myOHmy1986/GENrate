from flask import Flask

app = Flask(__name__)

from .modules import mask_operators
from .modules import material_operators
from .modules import mball_operators
from .modules import mesh_operators
from .modules import nla_operators
from .modules import node_operators
from .modules import object_operators
from .modules import outliner_operators

# Register the modules with the Flask app
app.register_blueprint(mask_operators, url_prefix='/mask')
app.register_blueprint(material_operators, url_prefix='/material')
app.register_blueprint(mball_operators, url_prefix='/mball')
app.register_blueprint(mesh_operators, url_prefix='/mesh')
app.register_blueprint(nla_operators, url_prefix='/nla')
app.register_blueprint(node_operators, url_prefix='/node')
app.register_blueprint(object_operators, url_prefix='/object')
app.register_blueprint(outliner_operators, url_prefix='/outliner')

# Define a default route
@app.route('/')
def index():
    return 'This is the main page of the web app.'

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
