ZAQAR FEED
===

The purpose of this project is to have a client that can be used by other softwares in order to work
with openstack queues in a producer/consumer way.
You can use as standalone client configuring it using the conf/config.json (a sample is provided) or
putting your own conf file and updating the config.py in order to import it.
The generic config file is made like this:

    {
        "global": {
            "clientuuid": "A CLIENT UUID GEN",
            "os_auth_url": "https://keystone_public_endpoint:5000/v2.0",
            "os_project_name": "DEMO3_LAB",
            "os_project_id": "YOUR PROJECT ID",
            "os_auth_token": "TOKEN PASSED TO TEST YOUR CODE",
            "zaqar_endpoint": "https://zaqar_endpoint:8888"
        }
    }

You can also leave blank the **os auth token** parameter and resolve it using the *keystoneclient* provided: it implements a method that return a new token, validate it (scoped tokens).
As done with the auth token parameter, you can also provide just the project name parameter (leaving blank the project identifier), but be careful because the keystone client will return the first occurrence of the ID met by matching the name passed as parameter.

