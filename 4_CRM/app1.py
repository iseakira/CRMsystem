from flask import render_template,request
from models import app

#ページ遷移
@app.route("/")
def index():
    return render_template("1_index.html")


@app.route("/item")
def item():
    return render_template("2_item.html")


#　機能系
@app.route("/add_customer",methods=["POST"])
def add_customer():
    customer_id = request.form["input-customer-id"]
    customer_name = request.form["input-customer-name"]
    age = request.form["input-age"]
    print(customer_id)
    return customer_id
if __name__ == "__main__":
    app.run(debug=True)