# site_credentials.py

environment_to_test = 0
access_certificate_name = ""

def get_environment():
    return environment_to_test

def get_certificate():
    return access_certificate_name

def set_credentials(env, cert):
    global environment_to_test, access_certificate_name
    environment_to_test = env
    access_certificate_name = cert
