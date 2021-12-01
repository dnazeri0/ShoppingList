from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    item = request.form['item']
    file = open("ListOutput", "a+")
    file.writelines(item)
    file.write("\n")
    file.close()
    return "Item added to shopping list."

if __name__ == '__main__':
  app.run(debug=True)
