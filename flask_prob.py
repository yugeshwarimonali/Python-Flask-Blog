from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/amstrong/<int:n>')
def amstrong(n):
        n = int(input('Enter a number: '))
        sum = 0
        order = len(str(n))
        copy_n = n

        while (n > 0):
            digit = n % 10
            sum += digit ** order
            n = n // 10

        if (sum == copy_n):
            print(f"{copy_n} is Armstrong!!")
            return True
        else:
            print(f"{copy_n} is not Armstrong!!")
            return False


if __name__ == "__main__":
    app.run(debug=Ture)