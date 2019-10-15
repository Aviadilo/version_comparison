import functools
import re


@functools.total_ordering
class Version:
    def __init__(self, version):
        version, digits, rest = make_values(version)
        self.version = version
        self.digits = digits
        self.rest = rest

    def __eq__(self, other):
        return self.version == other

    def __lt__(self, other):
        if self.digits == other and self.rest != 0:
            return self.version > other
        return self.version < other


def make_values(raw_str):
    splited = raw_str.replace('-', '.').split('.')
    converted_version = convert_str_digits_to_int(splited)
    digits, rest = divide_into_two_values(converted_version)
    return converted_version, digits, rest


def convert_str_digits_to_int(our_list):
    for i in range(len(our_list)):
        if our_list[i].isdigit():
            our_list[i] = int(our_list[i])
    return our_list


def divide_into_two_values(full_version):
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
        print("Yes!")


if __name__ == "__main__":
    main()
