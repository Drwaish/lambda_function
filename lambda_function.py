import tools as tl
import json
services = ["moorse_code", "temp_converter", "validate_password", "validate_email", "capitalize_string"]
def lambda_handler(event_jsonified, context):
    """
    lambda function to perform function.

    Parameters
    ----------
    event_jsonified
        Contain request header
    context
        Context of a function 

    Return 
    Dictionary Object

    """
    output = {}
    try:
        event = event_jsonified['body']
        event = json.loads(event, strict = False)
        use = event["use"]
        parameters = event["parameters"]
        print(use,  parameters)
        if use not in services:
            outputs["error"] = "Service not available"
        else:
            try:
                if use == "moorse_code":
                    parameters = event["parameters"]
                    message = parameters["text"]
                    if message is not None:
                        output["result"] = tl.encrypt(message)
                        return ({'status_code':200,
                                    'body': json.dumps(output)})
                elif use == "temp_converter":
                    parameters = event["parameters"]
                    to_temp = parameters["to_temp"]
                    from_temp = parameters["from_temp"]
                    temp = parameters["temp"]
                    if to_temp == "F" or to_temp == "C":
                        if from_temp == "F" or from_temp == "C":
                            if temp:
                                output["result"] = tl.temp_converter(to_temp, from_temp, temp)
                                return ({'status_code':200,
                                        'body': json.dumps(output)})
                            else :
                                output["error"] = "Value of temprature not found"
                        else:
                            outpput["error"] = "Conversion Symbol not valid (from)"
                    else:
                        output["error"] = "Parent symbol not valid (to) "

                elif use == "validate_password":
                    parameters = event["parameters"]
                    password = parameters["password"]
                    if password is not None:
                        output["result"] = tl.validate_password(password) 
                        return ({'status_code' : 200,
                                'body': json.dumps(output)})
                    else :
                        output["error"] = "Password not provided"

                elif use == "validate_email":
                    parameters = event["parameters"]
                    email = parameters["email"]
                    if email is not None:
                        output["result"] = tl.validate_email(email) 
                        return ({'status_code' : 200,
                                'body': json.dumps(output)})
                    else: 
                        output["error"] = "Email not provided"

            
                elif use == "capitalize_string":
                    parameters = event["parameters"]
                    string = parameters["string"]
                    if string is not None:
                        output["result"] = tl.string_capitalization(string) 
                        return ({'status_code' : 200,
                        'body': json.dumps(output)})
                else :
                    return ({"Status Code": 400,
                        'message': "Bad Params",
                        'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'body' : json.dumps(output)
                        })
            except Exception as identifier:
                return {'statusCode': 404,
                         'Error' : identifier, 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message': output
                        
                    }    
    except Exception as identifier:
        return {'StatusCode': 400,
                'Error': identifier,
                'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                "Message" : "Bad Params"
                }       
            
