from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return '{Hello, World!}'
 
@app.route('/name/&amp;amp;lt;name&amp;amp;gt;')
def show_user(name):
    return 'Hi! {0}'.format(name)

@app.route('/test/')
def test():
    return '{我好帥}'
 
app.run(debug=True, host='0.0.0.0', port=5566, threaded=True,processes=1)

##################################################
################### 用CMD執行 #####################
