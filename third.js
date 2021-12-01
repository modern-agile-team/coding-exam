function Third(th) {
    const result = [];
    const gen = th.filter(one => one.gender === '남자')
    .filter(two => two.age >= 18 && two.age < 60)
    .filter(three => three.weight >= 70)
    .filter(four => four.height >= 170);
    for(let i = 0; i < gen.length; i++) {
      result.push(gen[i].name);
    };
    return result
  };
  console.log(Third([
    {
      name: '조상우',
      gender: '남자',
      age: 47,
      height: 181,
      weight: 85,
    },
    {
      name: '오일남',
      gender: '남자',
      age: 77,
      height: 175,
      weight: 65,
    },
    {
      name: '한미녀',
      gender: '여자',
      age: 45,
      height: 167,
      weight: 49,
    },
    {
      name: '압둘 알리',
      gender: '남자',
      age: 33,
      height: 172,
      weight: 78,
    },
    {
      name: '장덕수',
      gender: '남자',
      age: 44,
      height: 180,
      weight: 73,
    },
    {
      name: '강새벽',
      gender: '여자',
      age: 27,
      height: 176,
      weight: 54,
    },
  ]));