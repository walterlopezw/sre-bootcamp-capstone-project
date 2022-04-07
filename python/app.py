# new
from urllib import request


# please dont import all from flask, convert, methods and repeate convert
from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, abort
from convert import *
from methods import *
#from convert import *
import mysql.connector

app = Flask(__name__)
login = Token()
protected = Restricted()
convert = CidrMaskConvert()
validate = IpValidate()


# Just a health check
# e.g. http://127.0.0.1:8000/
@app.route("/")
def urlRoot():
    #return "OK"
    return render_template('index.html')

# Just a health check
# e.g. http://127.0.0.1:8000/_health
@app.route("/_health")
def urlHealth():
    #return "OK"
    return render_template('health.html')



@app.route("/login", methods=['POST'])
def urlLogin():
    var1 = request.form['username']
    var2 = request.form['password']
    # This database data is here just for you to test, please, remember to define your own DB
    # You can test with username = admin, password = secret
    # This DB has already a best practice: a salt value to store the passwords
    con = mysql.connector.connect(
        host='localhost',
        user='mentor_walii',
        password='mentor_walii',
        database='mentor_walii'
    )
    cursor = con.cursor()
    query = "SELECT salt, password, role from users where username ='{}';".format(var1)
    print(query)
    cursor.execute(query)
    Query = cursor.fetchall()
    print(Query)
    var3 = login.generateToken(var1, var2, Query)
    if var3 is not False:
        r = {"data": var3}
        return jsonify(r)
    abort(401)




# e.g. http://127.0.0.1:8000/cidr-to-mask?value=8
@app.route("/cidr-to-mask")
def urlCidrToMask():
    print("VERIFY")
    var1 = request.headers.get('Authorization')
    print(request.headers)
    if not protected.access_Data(var1):
        abort(401)
    val = request.args.get('value')
    r = {"function": "cidrToMask", "input": val,
         "output": convert.cidr_to_mask(val), }
    return jsonify(r)
# # e.g. http://127.0.0.1:8000/mask-to-cidr?value=255.0.0.0


@app.route("/mask-to-cidr")
def urlMaskToCidr():
    var1 = request.headers.get('Authorization')
    if not protected.access_Data(var1):
        abort(401)
    val = request.args.get('value')
    r = {"function": "maskToCidr", "input": val,
         "output": convert.mask_to_cidr(val), }
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
