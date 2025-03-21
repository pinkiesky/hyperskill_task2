from flask import Flask, send_from_directory

app = Flask(__name__)

# Global counter to track page views
counter = 0


@app.route('/')
def index():
    # This tells Python we are referring to the global variable 'counter' defined outside the function.
    global counter
    counter += 1

    # Using an f-string to embed the counter value directly into the HTML.
    # f-strings allow you to insert expressions directly inside a string by prefixing the string with 'f'
    # and placing expressions in curly braces {}. They are available in Python 3.6 and later.
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Best Laptop</title>
        <link rel="stylesheet" type="text/css" href="/assets/styles.css">
    </head>
    <body>
        <h1>Product page</h1>
        <h2>Laptop XYZ</h2>
        <p>Brand: TechBrand</p>
        <p>Model: XYZ123</p>
        <p>Processor: Intel Core i7</p>
        <p>RAM: 16GB</p>
        <p>Storage: 512GB SSD</p>
        <p>Price: $999</p>
        <footer>You are visitor number: {counter}</footer>
        <p><a href="/metrics">Metrics</a></p>
        <p><a href="/metrics/reset">Reset Metrics</a></p>
    </body>
    </html>
    """
    return html


@app.route('/metrics')
def metrics():
    # `pass` below is a placeholder for future code.
    # In Python, pass is a null operation; nothing happens when it executes.
    # It's often used as a placeholder in functions or loops where code will be added later.
    # In this case, it indicates that the function is not yet implemented.
    # Remove `pass` and add your code here when you're ready to implement the page one.
    pass


@app.route('/metrics/reset')
def reset_metrics():
    pass

# The serve_static function is used to serve static files (like CSS, images, or JavaScript)
# from the 'assets' directory. When a URL matching /assets/<filename> is requested, Flask's
# send_from_directory function locates and returns the requested file.
# It's a common practice to keep static files in a separate directory for better organization.
# The send_from_directory function is a Flask utility that safely serves files from a specified directory.
# It's okay if you don't understand all the details of this function right now


@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('assets', filename)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
