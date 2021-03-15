# η συνάρτηση html_tag επιστρέφει μια συνάρτηση
def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Test Headline")

print_p = html_tag("p")
print_p("Test Paragraph")

# <h1>Test Headline</h1>
# <p>Test Paragraph</p>
