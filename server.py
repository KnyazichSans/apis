import pyodbc
import sqlite3
from flask import (
    Flask,
    render_template,
	jsonify,
	request
)

server = 'yorkbors.database.windows.net'
database = 'yorkbors'
username = 'yorkbors'
password = '4507739Aaa'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
row = cursor.fetchone()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def home():
    """
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')
	
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)