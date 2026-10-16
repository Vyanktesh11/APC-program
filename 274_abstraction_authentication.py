from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credential):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self, credential):
        return credential == "python123"

class OTPAuthentication(Authentication):
    def authenticate(self, credential):
        return credential == "123456"

class BiometricAuthentication(Authentication):
    def authenticate(self, credential):
        return credential == "fingerprint_verified"

methods = [PasswordAuthentication(), OTPAuthentication(), BiometricAuthentication()]
credentials = ["python123", "123456", "fingerprint_verified"]
for method, credential in zip(methods, credentials):
    print(type(method).__name__, method.authenticate(credential))
