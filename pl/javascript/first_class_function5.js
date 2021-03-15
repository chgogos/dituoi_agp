// η συνάρτηση logger επιστρέφει μια συνάρτηση που δέχεται παραμέτρους
// closure

function html_tag(tag) {  
    function wrap_text(msg){
        console.log('<' + tag + '>' + msg + '</' + tag + '>')
    }
    return wrap_text;
}

print_h1 = html_tag("h1")
print_h1("Test Headline")

print_p = html_tag("p")
print_p("Test Paragraph")


{/* <h1>Test Headline</h1>
<p>Test Paragraph</p> */}