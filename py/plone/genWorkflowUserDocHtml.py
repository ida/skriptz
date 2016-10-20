# We expect a file "definition.xml"in the same directory, outputs a 'defintion.html'-file in this directory.
wf_def_file = 'definition.xml'
wf_def = ''.join(open(wf_def_file).readlines()[1:]) # omit first line
wf_def = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>Workflow definition</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
</head>
<body lang="en" dir="ltr">
""" + wf_def + """
<script>
function getStateRoles(state_id) {
  var roles = []
  $('state[state_id=' + state_id + '] permission-role').each(function() {
    var role = $(this).text()
console.debug(role)
    if(roles.indexOf(role) == -1) {
        roles.push(role)
    }
  });
console.debug(roles)
  return ' (' + roles.join(', ') + ')'
}
function getTargetStateId(transition_id) {
  var transitions = document.getElementsByTagName('transition')
  for(var i=0;i<transitions.length;i++) {
      if(transitions[i].getAttribute('transition_id') == transition_id) {
          return transitions[i].getAttribute('new_state')
      }
  }
}
function getTransitionRoles(transition_id) {
    var string = ' ('
    $('transition').each(function() {
        if($(this).attr('transition_id') == transition_id) {
            var roles = $(this).find('guard-role')
            for(var i=0; i < roles.length; i++) {
                string += roles[i].innerHTML
                if(i < roles.length-1) { string += ', ' }
            }
        }
    });
    return string += ')'
}
function highlight(ele) {
  $(ele).css('background', 'yellow')
  $('#' + ele.className).css('background', 'yellow')
}
function downlight(ele) {
  $(ele).css('background', '#fff')
  $('#' + ele.className).css('background', '#fff')
}
document.addEventListener("DOMContentLoaded", function(event) { 
  var html = ''

  var state_tags = document.getElementsByTagName('state')
  for(var i=0; i < state_tags.length; i++) {
    var state_id = state_tags[i].getAttribute('state_id')
    html += '<div id="' + state_id + '">'
      + state_id + getStateRoles(state_id)
//      + ' (' + state_tags[i].getAttribute('title') + ')'

    var transition_tags = state_tags[i].getElementsByTagName('exit-transition')
    for(var j=0; j < transition_tags.length; j++) {
        var transition_id = transition_tags[j].getAttribute('transition_id')
        var target_state_id = getTargetStateId(transition_id)
      html += '<div class="' + target_state_id + '" style="padding-left: 1em; background: #fff">'
        + transition_tags[j].getAttribute('transition_id') + getTransitionRoles(transition_id)
      html += '</div>'
    }
    html += '</div>'
  }
  document.body.innerHTML = html
  transition_tags = $('body > div > div')
  for(var j=0; j < transition_tags.length; j++) {
    transition_tags[j].onmouseover=function() { highlight(this) }
    transition_tags[j].onmouseout=function() { downlight(this) }
  }
});
</script>
</body>
</html>"""
open(wf_def_file.split('.')[0] + '.html', 'w').write(wf_def)
