function square(x) {
    return x * x;
}

// custom map function
function my_map(func, arg_list){
    result = [];
    for(var i=0;i<arg_list.length;i++){
        result.push(func(i));
    }
    return result;
}

var squares = my_map(square, [1,2,3,4,5])

console.log(squares)

// [ 0, 1, 4, 9, 16 ]