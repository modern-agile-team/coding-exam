function fourth(fo) {
    const N = fo[0];
    const M = fo[1];
    let result = 0;
    for(let i = 0; i < M.length; i++) {
      if(N.includes(M[i])) {
        if(M.indexOf(M[i]) === M.lastIndexOf(M[i])) {
          result += M.indexOf(M[i]);
        } else result += M.lastIndexOf(M[i]);
      }; 
    };
   return result;
  };
  fourth(['good' ,'daood']);