from test.base import *


class Methods(Base):

    def send_request(self, link):

        r = requests.post(url=self.mainUrl + link, headers=self.headers,  auth=(self.user, self.password))
        return r.status_code

    def check_status_code(self, status_code):
        if status_code == 200:
            print("Server back 200")
        else:
            print("Server back " + str(status_code))
