import requests
user = "hello@world.com"
password = "12345678"
mainUrl = "http://instatestvx.me/"
headers = {"content-type": "application/json"}


class Methods:

    def send_request(self, link):

        r = requests.post(url=mainUrl + link, headers=headers,  auth=(user, password))
        json_data = r.json()
        return json_data["errors"]["message"]

    def check_status_code(self, response):
        if response == "The password and email you entered don't match. If you forgot your password, use \"Forgot Password\"":
            print("Test passed")
        else:
            print("Test failed")

class Tests:
    def verify_status_code(self):
        method = Methods()
        response = method.send_request(link="api/auth/login")
        method.check_status_code(response)


def main():
    test=Tests()
    test.verify_status_code()


main()