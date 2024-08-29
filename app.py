from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_data():
    # Call your scraping function here
    data = scrape()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
