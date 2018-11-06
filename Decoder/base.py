import base64
import base58

from decoder_interface import AbstractDecoder
from solver import solver


class Base(AbstractDecoder):
    algorithms = ["base64", "urlbase64", "base32", "base16", "base58"]

    def __init__(self, algorithm=None):
        self.algorithm = None
        super(Base, self).__init__(algorithm)
        self.result = None

    def update(self, data):
        def try_all_algorithms(data):
            result = {}
            try:
                result.update({"base64": base64.b64decode(data)})
            except Exception as e:
                pass

            try:
                result.update({"urlbase64": base64.urlsafe_b64decode(data)})
            except Exception as e:
                pass

            try:
                result.update({"base32": base64.b32decode(data)})
            except Exception as e:
                pass

            try:
                result.update({"base16": base64.b16decode(data)})
            except Exception as e:
                pass

            try:
                result.update({"base58": base58.b58decode(data)})
                # self.result.update({"base58": base58.b58decode_check(data)})
            except Exception as e:
                pass
            return result

        try:
            result = try_all_algorithms(data)
            if self.algorithm is not None:
                self.result = result.get(self.algorithm, None)
            else:
                self.result = result
        except Exception as e:
            pass

    def digest(self):
        if type(self.result) is not dict:
            return self.result#, self.algorithm
        # Need to create alg for choosing most successfull type of decoding
        if len(self.result) == 0:
            return dict(self.result).items()[0][1], dict(self.result).items()[0][0]
        value = solver(self.result)
        self.algorithm = value[1]
        return value[0]

    def hexdigest(self):
        if type(self.result) is not dict:
            return self.result#, self.algorithm
        # Need to create alg for choosing most successfull type of decoding
        if len(self.result) == 0:
            return dict(self.result).items()[0][1], dict(self.result).items()[0][0]
        value = solver(self.result)
        self.algorithm = value[1]
        return value[0].hex()
