def solution(people):
    good_people = []
    for person in people:
        if (18<= person['age'] < 60) and  person['gender']=='남자' \
            and person['weight']>=70 and person['height']>170:
            
            good_people.append(person['name'])

    return good_people

if __name__ == "__main__":
    list1 = [
        {
            'name': '조상우',
            'gender': '남자',
            'age' : 47,
            'height' : 181,
            'weight' : 85,
        },
    
        {
            'name': '오일남',
            'gender': '남자',
            'age' : 77,
            'height' : 175,
            'weight' : 65,
        },

        {
            'name': '한미녀',
            'gender': '여자',
            'age' : 45,
            'height' : 167,
            'weight' : 49,
        },
        {
            'name': '압둘 알리',
            'gender': '남자',
            'age' :33,
            'height' : 172,
            'weight' : 78,
        },
        {
            'name': '장덕수',
            'gender': '남자',
            'age' : 44,
            'height' : 180,
            'weight' : 73,
        },
        {
            'name': '강새벽',
            'gender': '여자',
            'age' : 27,
            'height' : 176,
            'weight' : 54,
        }
    

    ]
    print(solution(people=list1))
        