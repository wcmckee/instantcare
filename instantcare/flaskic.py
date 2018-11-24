from flask import Flask, request, jsonify, render_template
import ic

app = Flask(__name__)

@app.route('/createdb')
def createdb():
    nameofdb = request.args.get('nameofdb')
    #lenth = request.args.get('length')
    #ic.createdbtext(nameofdb)
    ic.createdatabase(nameofdb)

    return('{} database created!'.format(nameofdb))

@app.route('/createtext', methods=['GET', 'POST'])
def createtext():
    if request.method == 'POST':
        friendname = request.form.get('friendname')
        username = request.form.get('username')
        message = request.form.get('message')
        ic.createtext(friendname, username, message)
        return({'the friend {} left the following message for {}: {}'.format(friendname, username, message)})
    return(render_template('index.html'))

@app.route('/pushbutton', methods=['GET', 'POST'])
def pushbutton():
    if request.method == 'POST':

        username = request.args.get('username')
        lentime = request.args.get('lentime')

        ic.pushbutton(username, lentime)
        return({'the user {} pushed the button for {}'.format(username, lentim)})
    return(render_template('button.html'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556) 