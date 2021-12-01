members = [
  {
    "name": '조상우',
    "gender": '남자',
    "age": 47,
    "height": 181,
    "weight": 85,
  },
  {
    "name": '오일남',
    "gender": '남자',
    "age": 77,
    "height": 175,
    "weight": 65,
  },
  {
    "name": '한미녀',
    "gender": '여자',
    "age": 45,
    "height": 167,
    "weight": 49,
  },
  {
    "name": '압둘 알리',
    "gender": '남자',
    "age": 33,
    "height": 172,
    "weight": 78,
  },
  {
    "name": '장덕수',
    "gender": '남자',
    "age": 44,
    "height": 180,
    "weight": 73,
  },
  {
    "name": '강새벽',
    "gender": '여자',
    "age": 27,
    "height": 176,
    "weight": 54,
  },
]
# 조건  1. 남자     
#      2. 18세 이상 60세 미만     
#      3. 체중 70kg 이상    
#      4. 키 170cm 이상
target_members = []
for i in members:
    if (i["gender"] == "남자") and (i["age"] >= 18) and (i["age"] < 60) and (i["weight"] >= 70) and (i["height"] >= 170):
        target_members.append(i["name"])
print(target_members)