''' Driver of lammbda function '''
import lambda_function as lf
import json

# request = {"use" : "moorse_code" ,
# "parameters" : {"text":"GEEKS-FOR-GEEKS"} }

request = {"use" : "temp_converter" ,
"parameters" :{"to_temp" : "F",
"from_temp": "C",
"temp" : 45 } }

# request = {"use" : "validate_password",
# "parameters" : {"password" : "qwqertyuu"}}

# request = {"use" : "validate_email" ,
# "parameters" : {"email" : "qwert@gmail.com" } }

# request = {"use" : "capitalize_string" ,
# "parameters" :{"string" : zzzain} }

content = None
requests = {}
requests["body"] = json.dumps(request)
result = lf.lambda_handler(requests, content)
print(json.dumps(result, indent=4))
