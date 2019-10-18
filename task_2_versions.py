import functools


@functools.total_ordering
class Version:
    def __init__(self, version):
        version, digits, rest = self.__make_values(version)
        self.version = version
        self.digits = digits
        self.rest = rest

    def __eq__(self, other):
        return self.version == other

    def __lt__(self, other):
        if self.digits == other and self.rest != 0:
            return self.version > other
        return self.version < other

    def __make_values(self, raw_str):
        splited_version = raw_str.replace('-', '.').split('.')
        converted_version = self.__convert_str_digits_to_int(splited_version)
        digits, rest = self.__divide_into_two_values(converted_version)
        return converted_version, digits, rest

    def __convert_str_digits_to_int(self, splited_version):
        for i in range(len(splited_version)):
            if splited_version[i].isdigit():
                splited_version[i] = int(splited_version[i])
        return splited_version

    def __divide_into_two_values(self, full_version):
        digits = full_version[:3]
        rest = full_version[3:] if full_version[3:] else 0
        return digits, rest


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.1-a', '1.0.1-b'),
        ('1.0.1-a', '1.0.1'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1-b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()
