from flask import Flask, request, jsonify
import decoder

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received JSON:", data)
    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")

def procces_data(data):
    
    received_data = []
    
    if len(received_data) == 0:
        metadata = data["content"]
    else:
        received_data.append(data["raw"])
    
    if metadata != 0 and len(received_data) == metadata["requierd_chunks"]:
    
        decoder.decode_file(metadata["requierd_chunks"], metadata["redundant_chunks"], received_data)
        