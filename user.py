class User:
    """THis is a simple class representing user data"""

    def __init__(self, first_name, last_name, user_age, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.username = username
        self.password = password

    def to_dictionary(self):
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.user_age,
                'username': self.username,
                'password': self.password}
