function Rule(definition=null, validation=null, motivation=null) {

  // Definition of a test-rule.


  // 1.) Describe the rule in a human-language, e.g. 'Object exists.':
  this.definition = definition
  

  // 2.) Validate the rule in a machine-language:

  // Validation is expected to be a func which returns a bool.
  // The func gets the object which is to be validated passed.
  // Let's set a default with false return, for quicker developing:
  if(validation===null) {
    validation = function(obj) {
      console.log('Validating: ' + obj)
      return false
    }
  }

  this.validation = validation


  // 3.) Optionally explain your motivation for the need of restrictiveness:
  this.motivation = motivation


}


function Test(obj, rules=[]) {

  // Definition of running tests upon an object, after the rules.

  
  this.obj = obj
  this.rules = rules
  
  this.run = function() {
    showLinkOfCalledFile('test.js')

    var areValid = true
  
    for(var i in this.rules) {

      var isValid = this.rules[i].validation(this.obj)

      if(isValid !== true && isValid !== false) {
        console.error("A rule's validation is expected to always return either true or false!")
      }
      var html = '<div class="rule">' +
      rules[i].definition + '</div><div class="'
      if(isValid) html += 'success'; else html += 'error'
      html += '">' + isValid + '</div>'
      show(html)
      if(isValid===false) {
        areValid = false
//        showHtml('<div class="error"><div class="error">' +       
//        'A rule just broke, aborting rules-validation, now.</div></div>')
//        return false
      }
    } // for each rule
    
    if(areValid) {
      showHtml('<div class="success"><div class="success">' + 
               'Congrats, all rules are met!</div></div>')
    }
    else showHtml('<div class="error"><div class="error">Some tests failed.</div></div>')
    return areValid
  } // run
}  // Test().


function testTest(obj) {

var definition = 'Object shall not have a property named "id".'
var validation = function (obj) { return obj.id === undefined }
var rule = {definition, validation}
var rules = [rule]

definition = 'Object must have a property named "name".'
validation = function (obj) { return obj.name !== undefined }
rules.push({definition, validation})


var testObj = new Test({}, rules)
testObj.run()

//`; showAndExecuteCode(code)
  
} //////////////////////////////////////////////////////// testTest()
