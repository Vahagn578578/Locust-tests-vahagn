from locust import HttpUser, between, task
import logging


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        logging.info("Before login request")
        self.client.post("http://pa-api-users.priotix.xyz:8080/auth/login", data={"email": "vahagn@priotix.com",
                                                                                  "password": "11111111"})
        logging.info("After login request")
        logging.info("Before users/info get request")

        # how to use token for the request below?

        self.client.get("http://pa-api-storage.priotix.xyz:8080/users/info")
        logging.info("After users/info get request")
