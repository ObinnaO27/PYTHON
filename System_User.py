# Obinna Ohale
# Introduction to Programming with Python
# Script 21: "External Class File and the Import Statement"


class System_User:
    def __init__(self, user_id=-1, user_name="default", user_role="default"):

        self._user_id = user_id
        self._user_name = user_name
        self._user_role = user_role


    def set_user_id(self, new_id):
        self._user_id = new_id

    def get_user_id(self):
        return self._user_id

    def set_user_name(self, new_name):
        self._user_name = new_name

    def get_user_name(self):
        return self._user_name

    def set_user_role(self, new_role):
        self._user_role = new_role
        return

    def get_user_role(self):
        return self._user_role


