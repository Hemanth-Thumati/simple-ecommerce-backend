from flask import Flask, jsonify, request

app = Flask(__name__)
products = []
cart = []

@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'POST':
        product = request.get_json()
        products.append(product)
        return jsonify({'message': 'Product added!'}), 201
    return jsonify(products)

@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def manage_cart():
    if request.method == 'POST':
        item = request.get_json()
        cart.append(item)
        return jsonify({'message': 'Item added to cart!'}), 201
    elif request.method == 'DELETE':
        cart.clear()
        return jsonify({'message': 'Cart cleared!'})
    return jsonify(cart)

@app.route('/checkout', methods=['POST'])
def checkout():
    cart.clear()
    return jsonify({'message': 'Checkout successful! Thank you for your purchase.'})

if __name__ == '__main__':
    app.run(debug=True)