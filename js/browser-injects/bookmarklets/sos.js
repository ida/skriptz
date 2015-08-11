javascript:( function(){
alert('I')
var EXCLUDE = '0'

var new_links = []

var excludes = [
'31830537', 
'31880236',
]

var body = document.getElementsByTagName('body')[0]
    body.innerHTML(new_links)

var links = document.getElementsByClass('question-hyperlink')

for(var i=0; i<links.length; i++) {

    EXCLUDE = '0'
    
    var link = links[i]

    var dest = link.getAttribute('href')

    var post_nr = dest.split('/')[-2]

    for(var j=0; j<excludes.length; j++) {

        if(excludes[j] == post_nr) {

            EXCLUDE = '1'

        } // EXCLUDE  

    } // each exclude


    if(EXCLUDE == '0') {

        new_links.push(link)

    } // ! EXCLUDE


    body.innerHTML(new_links)
 


} // each link

})();
