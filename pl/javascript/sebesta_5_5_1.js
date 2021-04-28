function big(){
    function sub1() {
        var x = 7;
        sub2();
    }
    function sub2() {
        var y = x;
        console.log(y)
    }
    var x = 3;
    sub1();
}

big() // εμφανίζει 3 διότι η JavaScript χρησιμοποιεί στατική εμβέλεια

