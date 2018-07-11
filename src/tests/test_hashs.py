"""
File: test_hashs.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""


from hashlib import sha256


def test_simple_hashs():

    data = "I'm Theveloper".encode('utf-8')

    s = sha256(data).hexdigest()

    print(s)

    assert s == sha256(data).hexdigest(), "Always Same!"
