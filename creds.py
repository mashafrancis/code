import os

from dotenv import load_dotenv

load_dotenv()

creds_json = {
    "type": "service_account",
    "project_id": "code-344818",
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCSf70yWhpcwPZi\n7VMlrCmHHojS+wGrl8tATG8ftzIX7qXDqHpOYjiEdXGz6Wrmmlq41jhdIcD2XN7E\n0svGlLFKWeLNJJfZPzEcrCbRHT/09wpgcAMfMiOmCsU/3qrpYGMRaSc5au8c00iu\nvp11pivS6ArAdbxhWyLB3eLxpmlpFNlEtHVNZCV/9AA2M7Vgap7woomUAPz2ADfE\nqXFweJ43F+LnXsQUp9Ai56qDQVwvvNk/wUWqFEx9WlxsEYBj4B+s2qOKlvGTf62E\nil8xehj+NYX1wI5aUgSqbkSY0PdYY+30pvKyxge8D7OeXPKlZysQ8ZjEA/rmCT3o\ne/C2foUdAgMBAAECggEAFU9JeRKMNSPIczlsV9WEMOhrJK1oX8pzwUWdAHMIcVzA\ndgaCy/YTnIjs4iu45hRbz/kxN7LaO7vkl6LGC3vDkjoi+I4zHGHJxg7wkoh7rill\nNAP3IEmNz/BPIuxD1jC0GGtATmTUpU/CidCmXN+wDjy8m6REo7C7DJI3GcmIGcW7\nN0bMNiy0/NgyYQzhxgl/QoKUO6q2paPKu+Bl+J2xrsbL9cqqFtKsxRMokJDDbqFf\ngMsoqbZipdOqS3B/S2JqcPjsoPtPKCfaF0slXX2gU49wp844Ezt8NWKu+Csjr0xS\nZT5tZAT2g7mNqxghzmSyMK752dLN54ul0r3WGkFxwQKBgQDJPsqxqf2HHTONzRPo\nFN7UB9GcJS0ASy+GsNw//bnRgwPH4ra4Mjz9c6OccONQEW7NbF99eROh4c34WbSw\nn9KLdrQlaWIDiwhLpp343sMRstr0z+A34J9DjltfpgF+0KEm0MKZLlJRKCsFP8aC\n5wx/uJYhDTGoIbcZF5URe2pkTQKBgQC6W70J/ynX8jOJmx6ZJYpOw0dHw3JdK904\n98oHSXPlQyTsW1n8G6ZQ0zLTBusxRhucUrTNdVFvEP/w1omH4XBu+zkBgJ75Dr/9\nNsAZgNm6mBUJNLrhKiQzdTSWMH3I3bGZeRrRz8uJ38EWwsI8+alPK/aJHviSIhSc\nd6XjqMNMEQKBgDU6THZNVedEy/v3gApkasN+Bezc0FhBiqJ/aOHsBBfsJTXbOyTg\n9My8p0ubeCQXWE0xGtifC5hHlyjW4TnOK+wDS4aRpwD05w7LVQEcOlAWFF+oE8/z\ns2w03OohiEe4esc/dBj77X3Vt/s9cQ3yepXVhq/bQ4UK1djnKeBj2jIJAoGBAJsV\nAMmy6BVm3vCif+IeVWyaIVVdFmzmteBUhHFv9NxS9gUjOE0OjWcxelgWp96HYy7B\nvOhFuxDcasD3J9hGCRSyR4wyhxjn52lHCLGwgoA/UzIoCWSbdyjDXpGlpOdlZgg7\nuc/kRpNj+wF/7bhkYzsZcL5HYb/qUJCtGQXNSUihAoGBALQYg70H9rtjjGIZVOap\nZ8Xmuj07NQD3j/pkllxAt/v2n35D7TCnsOHzhwpw1ynozRz9OZcNy2t9kbJc5Mk5\n+zeJShJZA4iIuIyjlmhZEvT5YCZYQLiC/qg0qgRJ/nmZZhISgXnCViOHe6zAcMNl\nu9gwkSBuLj5iRk3pmJLziYRi\n-----END PRIVATE KEY-----\n",
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
}
