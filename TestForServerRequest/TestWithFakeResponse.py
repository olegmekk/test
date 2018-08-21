import requests
user = "hello@world.com"
password = "12345678"
mainUrl = "http://instatestvx.me/"
headers = {"content-type": "application/json"}
json = {"success": "false","errors": {"email": [user], "password": [password], "message": "The password and email you entered don't match. If you forgot your password, use \"Forgot Password\""}}


class Methods():

    def send_request(self):

        json_data = json["errors"]["message"]
        return json_data

    def response(self, response):
        if response == "The password and email you entered don't match. If you forgot your password, use \"Forgot Password\"":
            print("Test passed")
        else:
            print("Test failed")


class Tests:
    def verify_status_code(self):
        method = Methods()
        response = method.send_request()
        method.response(response)


def main():
    test=Tests()
    test.verify_status_code()


main()