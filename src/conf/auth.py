from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JsonWebToken


jwt = JsonWebToken("admin", expires_in=900)
auth = HTTPTokenAuth("Bearer")
