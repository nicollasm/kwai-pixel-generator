from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
import logging
from logic import generate_pixel_script

app = Flask(__name__)
app.config.from_pyfile('config/default_config.py')
csrf = CSRFProtect(app)
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

events = [
    'addPaymentInfo', 'addToCart', 'buttonClick', 'purchase', 'contentView',
    'download', 'formSubmit', 'initiatedCheckout', 'contact', 'placeOrder',
    'search', 'completeRegistration', 'addToWishlist', 'subscribe'
]


@app.route('/')
def index():
    return render_template('index.html', events=events)


@app.route('/generate_script', methods=['POST'])
def generate():
    data = request.json
    if not data or "platform" not in data or "pixel_id" not in data or "event" not in data:
        return jsonify({"error": "Dados incompletos."}), 400

    platform = data["platform"]
    pixel_id = data["pixel_id"]
    event = data["event"]

    try:
        script = generate_pixel_script(platform, pixel_id, event)
        return jsonify({"script": script})
    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}), 500


@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


if __name__ == '__main__':
    app.run(debug=True)
