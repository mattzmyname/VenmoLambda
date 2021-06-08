from venmo_api import Client


class VenmoClient:
    def __init__(self, user, password):
        self.access_token = Client.get_access_token(
            username=user,
            password=password)
        self.venmo = Client(access_token=self.access_token)

    def get_user(self, username):
        # Search for users. You get 50 results per page.
        users = self.venmo.user.search_for_users(query=username)
        if len(users) == 0:
            raise Exception("No-users found")
        if len(users) > 1:
            raise Exception("Non-unique username")

        return users[0]

    def request_money(self, target, amount, description):
        self.venmo.payment.request_money(amount=amount,
                                         note=description,
                                         target_user=target)

    def log_out(self):
        self.venmo.log_out("Bearer " + self.access_token)
        print("Logged out!")
