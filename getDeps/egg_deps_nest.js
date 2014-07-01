(function($) { $(document).ready(function() {
/*
For each parent iterate over li's and add depps, 
if not happened already = corresponding ul was checked and added to kollekted.

We have a series of lists (one ul followed by another -> 1st-level-siblings -> parents), looking like this:

    <ul class="egg">
        <li class="name">Products.CMFPlone
            <ul class="versions">
                <li class="version">4.3.3
                    <ul class="pins">
                        <li class="pin">&gt;=4.3,&lt;5
                        </li>
                        <ul class="pinned-versions">
                            <li class="pinned-version">2.1
                                <ul class="pinned-vs-op">
                                <ul class="pinned-by-names">
                                    <li class="pinned-by-name">plone.app.layout OR config
                                    </li>
                                </ul>
                        </ul>
                    </ul>
                    <ul class="deps">
                        <li>zope.interface
                            <ul class="dep-version-info">
                                <li class="dep-version-nr">4.3.3
                                </li>
                                <li class="dep-version-pin-op">==
                                </li>
                                <li class="dep-version-pin-by">[SELF](here:'Products.CMFPlone'==
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>

while egg not in  kollekted and kollekted < eggs
*/

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function get_deps(egg_name) {
// Get deps of 1st-level ul, remove after, repeat as long as not filled
    var parents   = $('body > ul > li:first-child')
    var paris = ''
    var deps = null
    // Get corresponding ul of li (same name):
    for(var i=0; i<parents.length; i++) {
        paris = parents[i]
        paris_name = $.trim(paris.firstChild.nodeValue)

        if(egg_name == paris_name && paris_name != 'Products.CMFPlone') {
            // Get deps:
            deps = $(paris).find('ul')[0]
            // Remove paris:
            $(paris).remove()
        }
    }
    return deps
}

function insert_deps(basket) {
    var items = $(basket).find('li')
    for(var i=0; i<items.length; i++) {
        var item = items[i]
        var item_name = $.trim(item.firstChild.nodeValue)
        //alert(item_name)
        // Get corresponding ul:
        var deps = get_deps(item_name)
        if(deps != null) { //paris still available 
            // Append ul to this li:
            $(item).append($(deps))
//            $(item).css('border','1px solid red')
            insert_deps(item)
        }
        else {
            if(item_name != 'No deps') {
                $(item).append('<ul><li>dooped</li></ul>')
            }
            else if (items) {
                item.parentNode.removeChild
            }
        }
    }

}//insert_deps

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
var root = $('body > ul:first-child > li') //'Plone'-li

//insert_deps(root) //  ini
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Kosmetik:
/*
$('li').each(function(){
    if(this.firstChild.nodeValue == 'No deps') {
        $(this).remove()
    }
})
*/


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//alert($('li:contains("Products.CMFPlone")').css('border', '3px solid').length) // visualize version-pins
// Create pindown-report:
$('body').prepend('<div id="pin-results"><div>')
var koller = []

$('span:contains("=")').each(function() {
    //$('#pin-results').prepend('<div><span>'+this.parentNode.firstChild.nodeValue+'</span> is pinned to <span>'+this.innerHTML + '</span> by <span>' + this.parentNode.parentNode.parentNode.firstChild.nodeValue + '</span><div>')
//    $('#pin-results').prepend('<div>'+this.parentNode.firstChild.nodeValue+this.innerHTML + this.parentNode.parentNode.parentNode.firstChild.nodeValue+'</div>')
    var entry = this.parentNode.firstChild.nodeValue + this.innerHTML// + this.parentNode.parentNode.parentNode.firstChild.nodeValue
    koller.push(entry)

})//css('border', '3px solid red') // visualize version-pins
koller.sort()
koller.reverse()
dups = []
for(var i=0; i<koller.length; i++) {
    var koll = koller[i]
    
$('body').prepend(koll.replace(/ /g,'')+'<br>')
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Kollekt dup-pins:
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}) })(jQuery);
