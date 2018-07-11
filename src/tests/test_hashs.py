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

    # no matter how many times you run it,
    # the  result is going to be the same 256 character string
    # sha256 함수를 아무리 여러번 재사용해도 결과는 항상 같습니다!

    assert s == sha256(data).hexdigest(), "Always Same!"
