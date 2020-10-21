
class Parser:
    @staticmethod
    def is_magic_string(s):
        assert(type(s) == str)
        return ("magic" in s)
