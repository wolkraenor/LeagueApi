from . import app


@app.route("/items", methods=['GET'])
def all_items():
    items = ItemsService()
    data = items.store()
    return jsonify(data=data)

@app.route("/items/<name>", methods=['GET'])
def items_by_name(name):
    items = ItemsService()
    data = items.item_by_name(name=name)
    return jsonify(data=data)