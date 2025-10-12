from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

products_list = [
    {'id': 1, 'name': 'The Thinker\'s Journal', 'price': 24.99,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Journal'},
    {'id': 2, 'name': 'Procrastination Poster', 'price': 19.99,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Poster'},
    {'id': 3, 'name': 'Curiosity Mug', 'price': 15.00,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Mug'},
    {'id': 4, 'name': 'The Idea T-Shirt', 'price': 29.50,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=T-Shirt'},
    {'id': 5, 'name': 'Neural Network Art Print', 'price': 45.00,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Art+Print'},
    {'id': 6, 'name': 'Philosopher\'s Stone Paperweight', 'price': 35.00,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Paperweight'},
    {'id': 7, 'name': 'The "Why" Hat', 'price': 22.00,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Hat'},
    {'id': 8, 'name': 'Minimalist Calendar', 'price': 28.00,
     'imageUrl': 'https://placehold.co/400x400/e2e8f0/334155?text=Calendar'},
]
products_dict = {str(p['id']): p for p in products_list}


@app.before_request
def initialize_session():
    if 'cart' not in session:
        session['cart'] = {}


@app.route('/')
def home():
    total_items = sum(session['cart'].values())
    return render_template('index.html', products=products_list, total_items=total_items)


@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product_id_str = str(product_id)
    cart = session['cart']
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    session['cart'] = cart
    return redirect(url_for('home'))


@app.route('/cart')
def cart_view():
    cart_items = []
    total_price = 0

    for product_id, quantity in session.get('cart', {}).items():
        product = products_dict.get(product_id)
        if product:
            item_total = product['price'] * quantity
            total_price += item_total
            cart_items.append({
                'id': product_id,
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'imageUrl': product['imageUrl'],
                'item_total': item_total
            })

    total_items = sum(session['cart'].values())
    return render_template('cart.html', cart_items=cart_items, total_price=total_price, total_items=total_items)


@app.route('/update_cart', methods=['POST'])
def update_cart():
    new_cart = {}
    for product_id, quantity_str in request.form.items():
        if f"remove_{product_id}" in request.form:
            continue

        # Process quantity updates
        if quantity_str.isdigit():
            quantity = int(quantity_str)
            if quantity > 0:
                new_cart[product_id] = quantity

    session['cart'] = new_cart
    return redirect(url_for('cart_view'))


if __name__ == '__main__':
    app.run(debug=True)

