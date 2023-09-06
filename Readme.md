# Mock Lambda Function 
 A user can perform following functionalities:

 ## Moorse Code
 A user can generate morse code of given string. Following is the  payload of request body
 ```

  request = {
              "use" : "moorse_code" ,
              "parameters" : {"text":"GEEKS-FOR-GEEKS"} 
            }

 ```
 ## Temp Converter
 A user can convert temprature from Farenheit to Celsius and vice versa. Following is the  payload of request body

### From Farenheit to Celsius
```

request = {
            "use" : "temp_converter" ,
            "parameters" :{"to_temp" : "F",
            "from_temp": "C",
            "temp" : 45 } 
          }

```
### From Celsius to Farenheit
```

request = { 
            "use" : "temp_converter" ,
            "parameters" :{"to_temp" : "C",
            "from_temp": "F",
            "temp" : 45 } 
          }

```
## Password Strength Checker
 A user can check strength of their passwords. Following is the  payload of request body

```
request = {
           "use" : "validate_password",
           "parameters" : {"password" : "qwqertyuu"}
          }

```

## Email Validation
 A user can cvalidate email. Following is the  payload of request body
 ```

 request = {
            "use" : "validate_email" ,
            "parameters" : {"email" : "qwert@gmail.com" }
           }

 ```

## String Capitalization

First Letter of word become capitalize. Following is the payload

```

request = {
            "use" : "capitalize_string" ,
            "parameters" :{"string" : zzzain} 
          }

```

# How to run this repository?
## Create Environment
First, create conda environment
```bash
conda create -n <name_of_environment> python == 3.10.12
conda activate <name_of_environment>
```
## Clone Repository 
```bash

git clone https://github.com/Drwaish/lambda_function.git
cd lambda_function
python3 driver.py

```