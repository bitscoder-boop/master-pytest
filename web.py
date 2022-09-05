from flask import Flask, jsonify


app = Flask(__name__)


def change(amount):
    res = []
    coins = [1,5,10,25]
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    res.append({num:coin_lookup[coin]})

    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res


@app.route('/')
def index():
    return jsonify({'hello': 'world'})


@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
