function First(f) {
    const a = f.split(" ");
    const b = a.splice(0,1);
    const num = parseInt(b);
    const word = a.join(" ");
    return word.repeat(num);
  };
  console.log(First("4 안녕"));