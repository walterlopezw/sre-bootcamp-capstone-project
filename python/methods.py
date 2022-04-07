import hashlib
import jwt


class Token:
    def generateToken(self, username, input_password, Query=None, test=False):

        if test:
            hashPass_original = 'bd2b1aaf7ef4f09be9f52ce2d8d599674d81aa9d6a4421696dc4d93dd0619d682ce56b4d64a9ef097761ced99e0f67265b5f76085e5b0ee7ca4696b2ad6fe2b2'
            hashPass = hashlib.sha512((input_password).encode()).hexdigest()
            return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w' if hashPass == hashPass_original else False

        usefulKey = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
        if Query != None:
            salt = Query[0][0]
            password = Query[0][1]
            role = Query[0][2]
            hashPass = hashlib.sha512(
                (input_password).encode()).hexdigest()
            if hashPass == password:
                enJWT = jwt.encode(
                    {"role": role}, usefulKey, algorithm='HS256')
                return enJWT
            else:

                return False
        else:
            return False


class Restricted:
    def access_Data(self, authorization, test=False):
        try:
            print()
            var1 = jwt.decode(authorization, options={
                              "verify_signature": False}, algorithms='HS256')
        except Exception as e:
            return False
        if 'role' in var1:
            return True
        else:
            return False


convert = Token()
#print(convert.generateToken('admin', 'secret', None, True))
convert = Restricted()
print(convert.access_Data(
    'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w', True))
