from flask import Flask, render_template, request

app = Flask(__name__)

# List of dictionaries to simulate content from
#   a MySQL database query
grocery_list = [
    {
        "id":1,
        "product":"Milk"
    },
    {
        "id":2,
        "product":"Eggs"
    },
    {
        "id":3,
        "product":"Bread"
    },
    {
        "id":4,
        "product":"Rootbeer"
    },
    {
        "id":5,
        "product":"Diapers"
    }
]


# Route to display the list of demos
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


# Page to display a dropdown list of groceries and a button to send the
#   id of the selected grocery item to the webservice
@app.route('/select-list/', methods=["GET"])
def select_list():
    return render_template("select-list-demo.html", groceries=grocery_list)


# This route catches the data posted from the select-list-demo.html page
#   and simply writes the id of the grocery item to HTML
@app.route('/select-result/', methods=["POST"])
def select_list_result():
    select_list_data = request.form.get("groceries")
    return f"ID #{select_list_data} received!"


# The Delete route performs two tasks:
#   1) On a GET request it displays all the grocery items and a button next to 
#       each item to delete the grocery item
#   2) On a POST request when a delete button is pressed, it removes the item
#       from our fake database and redisplays the list of grocery items that
#       remain for deletion
@app.route('/delete/', methods=["GET", "POST"])
def delete_item():
    # Check if we received a POST method
    if request.method == "POST":
        # Get the grocery id number from assciated with its respective delete button
        item_id = int(request.form.get("remove"))
        # Find and remove the item
        for i in range(len(grocery_list)):
            if grocery_list[i]['id'] == item_id:
                del grocery_list[i]
                break

    # Display the delete page and pass along the grocery items to display
    return render_template("delete-demo.html", groceries=grocery_list)


if __name__ == '__main__':
    app.run(debug=True, host="localhost")
    