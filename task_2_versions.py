import functools
import re


@functools.total_ordering
class Version:
    def __init__(self, version):
        version = make_value(version)
        self.version = version

    def __eq__(self, other):
        return self.version == other

    def __lt__(self, other):
        return self.version < other


def make_value(raw_str):
    if not re.search('[a-zA-Z]', raw_str):
        raw_str = raw_str + '.z'
    splited = re.split('\.|-', raw_str)
    splited = make_int(splited)
    return splited


def make_int(our_list):
    for i in range(len(our_list)):
        if our_list[i].isdigit():
            our_list[i] = int(our_list[i])
    return our_list


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
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
