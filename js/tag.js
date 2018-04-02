        function Tag(name='div') {
  this.name = name
  this.content = null
  this.rules = [        // Let's make up some rules, like we're creators.

    {
      definition: 'A tag must have a name-property.',
      validation:  function(tag) { return tag.name !== undefined },
      motivation: 'Existential.',
    },
    
    
    {
      definition: 'A name-property must be a string.',
      validation:  function(tag) { return typeof(tag.name) == 'string' },
      motivation: 'Typical.',
    },
    
    
    {
      definition: 'A name-property cannot be an empty string.',
      validation:  function(tag) { return tag.name != '' },
      motivation: 'Edgy.',
    },
    
    
    {
      definition: 'A tag must have a content-property.',
      validation:  function(tag) { return tag.content !== undefined },
      motivation: 'No empty tags.',
    },
    
    
    {
      definition: 'The content-property must either contain a non-empty string ' +
                  'OR an array of tag-object(s) OR be null.',
      validation:  function(tag) { if(
            tag.content === null      
        ||
            typeof(tag.content) == 'string' && tag.content != ''
        ||
            Array.isArray(tag.content) && tag.content.length > 0
                                       && tag.content[0] instanceof Tag
        )  { return true }
        return false
      },
      motivation: 'Either text or tags, because text-node should always live' +
                  'in a dedicated tag, to not mix up text- and element-nodes.',
    },

    
    {
      definition: 'The content-property can, but should not be empty.',
      validation:  function(tag) {
        if(tag.content === null) {
          showWarning('Tag is empty.')
        }
        return true
      },
      motivation: 'No empty tags.',
    },

  ]
  
}
  

Tag.prototype.add = function(tagName='div', content=null) {
  if( typeof(this.content) == 'string') {
    console.error('Tag has text, using add() is not allowed. ' +
                  'Aborting now, nothing changed.')
  }
  else {
    var child = new Tag()
    child.name = tagName
    if(content !== null) {
      child.content = content
    }
    this.content.push(child)
  }

}

Tag.prototype.adds = function(amount, tagName='div') {
  if( typeof(amount == 'number') && amount > 0) {
    for(var i=0; i < amount; i++) {
      this.add(tagName)
//      this.content[i].content = String(Number(i) + Number(1))
    }
  }
  else {
    console.error('Passed "amount" is either not a number or \
smaller than one, aborting now, nothing changed.')
  }
}

Tag.prototype.text = function(text=null) {
  if(this.content.length > 0 && this.content[0] instanceof Tag) {
    console.error('Tag has children-tags, using text() is not allowed. ' +
                  'Aborting now, nothing changed.')
  }
  else {
    if(text !== null) this.content = text
    return this.content
  }
}


Tag.prototype.validate = function() {

  var isValid = true   // Assume best until proven otherwise.

  var tag = this       // Grab tag because "this" switches context.


  
  for(var i=0; i < this.rules.length; i++) {
    var truth = this.rules[i].validation(tag)
    if(truth === false) {
      isValid = false // Assuming the best will always lead to disappointment.
      var error = 'Validation fails for this rule:\n    ' + this.rules[i].definition
      console.error(error); showError(textToHtml(error))
      return isValid // Break futher validations as soon as a rule breaks.
    }
  }


  return isValid // Truth suceeded, yey!

}


function testTag(tag=null) {
/*

  Make all the rules of `Tag.validate` fail.

*/


  
  showLinkOfCalledFile('tag.js')

  

  function showMsg(msg) {
    // Show messages in console and in body-ele.   
    console.debug(msg)
    showHtml('<div>' + msg + '</div>')
  }

  function testFailed(msg='Test failed!') {
    // Show errors in console and in body-ele.   
    console.error(msg)
    showError(msg)
  }

  


  showMsg("Let's create and validate a tag, all should be fine:")
  if(tag===null) tag = new Tag()
  var truth = tag.validate()
  if(truth !== true) testFailed('\
Validation fails immediately after instanciation of a tag, not good.')



  showMsg("Delete name-property, validation should fail:")
  delete tag.name
  truth = tag.validate()
  if(truth !== false) testFailed('\
Deleted name-property, but validation passes fine, tststs.')



  showMsg("Name-property is not a string, validation should fail:")
  tag.name = null
  truth = tag.validate()
  if(truth !== false) testFailed('\
Name-property is not a string, but validation passed, ohoh.')


  showMsg("Name-prop is an empty str, should fail:")
  tag.name = ''
  truth = tag.validate()
  if(truth !== false) testFailed('\
Name-property is an empty string, but validation works, nanana.')
  tag.name = 'div' // Restore valid value, before continuing.



  showMsg("Content cannot be a number, fail:")
  tag.content = 23
  truth = tag.validate()
  if(truth !== false) testFailed('\
Content-property is not valid, but validation works, erm.')



} // EO testTag
