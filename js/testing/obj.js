function Val(value=null) {
  this._value = value
  this.add = function(value) {
    if(typeof(value) == typeof(this._value)) this._value += value
    else console.error('Value to add has a different type than current ' +
                       'value, cannot add them, aborting now.')
  }
  this.get = function() { return this._value }
  this.set = function(value) {  this._value = value  }
  this.sub = function(value) {
    if(typeof(value) == typeof(this._value)) this._value -= value
    else console.error('Value to add has a different type than current ' +
                       'value, cannot subtract it, aborting now.')
  }
}


function Obj(obj={}) {
  var obj = obj
  this.props = new Val(['props', 'rules'])
  this.rules = [
    {
      definition: `
We want to have a known set of property-names, to inhibit unwanted overwrites of
existing props.<br>For that we use the convention to have a property named 'props'
reserved in every object.<br>Lets make sure, it exists.
      `,
      validation: function(obj) { return obj.props !== undefined },
    },
    {
      definition: `
The property 'props' is a list of all known props, it must contain itself.
      `,
      validation: function(obj) { return obj.props.get().indexOf('props') !== -1 },
    },
    {
      definition: `
Reserve another prop-id 'rules' for the, er rules, it exists?
      `,
      validation: function(obj) { return obj.props.get().indexOf('rules') !== -1 },
    },
  ]
}

 
function testObj()  {
  
var o = new Obj()



o.props.add = function(name, val=new Val()) {
  for(var i in this._val) {
    if(this._val[i] == name) {
      console.error('Propname exists already, aborting now.')
      return false // abort, if name exists
    }
  }
  this._val.push(name)   // collect prop
  o.name = new Val(val) // set new prop
  console.log('Added new prop.')
  return true
}

o.props.add('opp')
o.props.add('opp')
  /*
  */
    
} // testObj

