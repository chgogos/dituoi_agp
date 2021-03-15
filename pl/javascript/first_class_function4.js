// η συνάρτηση logger επιστρέφει μια συνάρτηση
function logger(msg) {
    function log_message(){
        console.log('Log: ' + msg)
    }
    return log_message;
}

log_hi = logger("Hi!")
log_hi()


// Log: Hi!