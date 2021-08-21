# Import Modules
from flask import Flask, jsonify, request

# Create App
app = Flask(__name__)

# Create Contacts List
contacts = [
    {
        'id': 1,
        'Name': u'ABC',
        'Contact': u'416647978', 
        'Done': False
    },
    {
        'id' : 2,
        'Name': u'DEF',
        'Contact': u'647416312',
        'Done': False
    },
    {
        'id' : 3,
        'Name': u'GHI',
        'Contact': u'1234567890',
        'Done': False
    },
]

# Test
@app.route("/")
def hello_world():
    return ("Hello World!")

# Create Route with Post Method
@app.route("/add-data", methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please Provide the Data!"
        }, 400)

    # Create Contact Dictionary
    contact = {
        'id' : contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact' : request.json.get('Contact', ""),  
        'done' : False  
    }

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
        })

# End Lines
if (__name__ == "__main__"):
    app.run(debug=True)
