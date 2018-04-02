showLinkOfCalledFile('main.js')
showAndExecuteCode(`

var obj = new Obj()

testTest(obj)
`)

showLinkOfCalledFile('main.js')
show("<br>Hi!<br><br>Let's create an object and test it:")
showAndExecuteCode(`

var obj = new Obj()

var test = new Test(obj, obj.rules)

test.run()
`)


showLinkOfCalledFile('main.js')
show("<br>Now, let's create a tag and test it:")

showAndExecuteCode(`

var tag = new Tag()

var test = new Test(tag, tag.rules)

test.run()
`)


/*
for(var i in tag.rules) {
  showReturn(tag.rules[i].definition)
}

function NewTag(name='div') {
  this.name = name
  this.content = new Val()
}
var tagg = new NewTag()
//showHtml(Object.keys(tagg.content))
showHtml(tagg.content.get())


*/
//showAndExecuteCode('testTag()')
//showAndExecuteCode('testTest()')
