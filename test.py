from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route("/proxy", methods=["POST"])
def proxy():
    data = request.json
    api_url = "https://www.fused.io/server/v1/realtime-shared/fsh_6ovAiUq4UfofTq4yNYciUW/run/file"
    params = {
        "dtype_out_raster": "tiff",
        "dtype_out_vector": "csv",
        "geojson": data["geojson"],
    }
    response = requests.get(api_url, params=params)
    return response.text, response.status_code, response.headers.items()


if __name__ == "__main__":
    app.run(debug=True)
