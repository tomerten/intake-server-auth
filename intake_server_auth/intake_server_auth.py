from intake.auth.secret import BaseAuth
from json import load


class SecretAuth(BaseAuth):
    def __init__(self, secret, pwdfile, key="intake-secret"):
        self.secret = secret
        self.key = key

        with open(pwdfile, "r") as f:
            self.users = load(f)

    def allow_connect(self, header):
        try:
            return self.get_case_insensitive(header, self.key, "") == self.secret
        except:
            return False

    def allow_access(self, header, source, catalog):
        user = header.get("X-Forwarded-User", None)
        source_name = source.describe()["name"]

        allowed_users = self.users.get(source_name, [])

        if user in allowed_users:
            return True
        return False
