class BluedartProfile(object):
    def __init__(self, api_type, login_id, license_key, area=None, customer_code=None, is_admin=None, password=None,
                 version=None, use_test_server=False):
        self.api_type = api_type
        self.login_id = login_id
        self.password = password
        self.area = area
        self.customer_code = customer_code
        self.is_admin = is_admin
        self.license_key = license_key
        self.version = version
        self.use_test_server = use_test_server
