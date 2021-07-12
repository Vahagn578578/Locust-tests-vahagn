from locust import HttpUser, between, task
import logging


class Login(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        logging.info("Before login request")
        self.client.post("http://pa-api-users.priotix.xyz:8080/auth/login", data={"email": "vahagn@priotix.com",
                                                                                  "password": "11111111"})
        logging.info("After login request")
