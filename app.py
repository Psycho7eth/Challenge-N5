from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Product 1", "price": "10.99$", "description": "Description of product 1"},
    {"id": 2, "name": "Product 2", "price": "19.99$", "description": "Description of product 2"},
    {"id": 3, "name": "Product 3", "price": "29.99$", "description": "Description of product 3"},
]

@app.route('/')
def index():
    
     return render_template('index.html', products=products)
   

@app.route('/product/<int:product_id>')
def product(product_id):
  
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

    


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
