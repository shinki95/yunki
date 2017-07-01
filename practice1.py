#매우 간단한 전화번호부
name = ['김민경', '김태은', '최지영']
phone_number = ['01087437983', '01074669493', '01029660671']
major = ['불어불문과', '경제학부', '경영학부']
information = list(zip(name, phone_number,major))
contact = dict(zip(name,information))
contact[input("what's your name: ")]

 