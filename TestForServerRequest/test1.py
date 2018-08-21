import requests
user = "hello@world.com"
password = "12345678"
mainUrl = "http://google.com/"
headers = {"content-type": "application/json"}


class Methods():

    def send_request(self, link):

        r = requests.post(url=mainUrl + link, headers=headers,  auth=(user, password))
        return r.status_code

    def check_status_code(self, status_code):
        if status_code == 200:
            print("Server back 200")
        else:
            print("Server back " + str(status_code))

class Tests:
    def verify_status_code(self):
        method = Methods()
        code = method.send_request(link="api/auth/login")
        method.check_status_code(code)


def main():
    test=Tests()
    test.verify_status_code()

main()