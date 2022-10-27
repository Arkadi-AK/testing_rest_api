from faker import Faker

fake = Faker()


class CreateUser:
    @staticmethod
    def create_user_password():
        username = fake.user_name()
        password = fake.password()
        return {"username": username, "password": password}
