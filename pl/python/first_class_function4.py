# επιστροφή συνάρτησης από συνάρτηση

# η συνάρτηση logger επιστρέφει μια συνάρτηση
def logger(msg):
    def log_message():
        print("Log:", msg)

    return log_message


log_hi = logger("Hi!")
log_hi()

# Log: Hi!