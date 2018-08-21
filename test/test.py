from test.methods import *


method = Methods()
code = method.send_request(link="api/auth/login")
method.check_status_code(code)

