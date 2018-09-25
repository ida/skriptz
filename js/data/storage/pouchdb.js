function Pouchee(db_name, wrapperEle=null) {
  this.ini(db_name, wrapperEle)
}
Pouchee.prototype.ini = function(db_name, wrapperEle) {
  // If no wrapperEle is passed, db will not be displayed.
  var PouchDB = require('pouchdb')
  this.db = new PouchDB(db_name)
  this.ele = wrapperEle
  if(this.ele !== null) {
    this.showDB()  // show data initially
    this.db.changes({since: 'now', live: true}).on('change', function() {
      this.showDB() // show new data after db.put()
    });
  }
}
Pouchee.prototype.showMessage = function(msg) {
  // Add ele with msg and insert it as first-child of body.
  var ele = document.createElement('div')
  ele.innerHTML = msg
  document.body.insertBefore(ele, document.body.firstChild)
}
Pouchee.prototype.showDB = function() {
  var ele = this.ele
  var i, row, rows, items = null
  function genHtml(obj, html='<div>', excludeUnderscoredKeys=true) {
    console.log('obj',obj)
    let key, value = null
    for(key in obj) {
      if(excludeUnderscoredKeys === false ||
         key == '_id' || // exception of the rule: we want id
         excludeUnderscoredKeys === true  && key.startsWith('_') === false) {
        value = obj[key]
        html += '<div>'
        html += key
        html += '</div>'
        html += '<div>'
        if(value instanceof Object) {
          html = genHtml(value, html)
        }
        else {
          html += value
        }
        html += '</div>'
      }
    }
    html += '</div>'
    return html
  }
  this.db.allDocs({include_docs: true}, function(err, docs) {
    if(err) {
      this.showMessage(err)
      return false
    }
    rows = docs.rows
    for(i=0; i < rows.length; i++) {
      row = rows[i]
//      html += genHtml(row.doc)
    ele.innerHTML = genHtml(row.doc)
    }
    var html = genHtml(rows)
    console.log('html',html)
    //ele.innerHTML = genHtml(rows)
  });
  return true
}
/*
function addEntry(db, dict={}) {
  var id = dict._id
  entryChanged = false
  db.get(id).then(function(doc) {
    for(var key in dict) {
      if(doc[key] != dict[key]) {
        doc[key] = dict[key] // (re-)set doc-prop
        entryChanged = true
      }
    }
    if(entryChanged === true) {
      return db.put(doc) // update db
    }
  }).then(function() {
  	return db.get(id) // return doc for next line (?)
	}).catch(function(err) {
    dict._id = id // pouchdb expects a key named '_id'
    db.put(dict).then(function (result) { // create new doc
    }).catch(function (err) {
      console.log('Could not create entry with id "' + id + '":', err)
    });
	});
}
function deleteEntry(db, id) {
  db
    .get(id)
    .then(function(doc) {
      return db.remove(doc)
    })
    .catch(function(error) {
      showMessage('deleteEntry() errors with: ' + error)
    });
}
function dictToList(dict) {
  items = ['id', row.id]
  for(key in row.doc) {
    if(key.startsWith('_') === false) {
      items.push(key)
      items.push(row.doc[key])
    }
  }
  html = genHtmlList(items)
}
function getEntry(db, id, doWithEntry=null) {
}
function genHtml(obj, html='<div>', excludeUnderscoredKeys=true) {
  let key, value = null
  for(key in obj) {
    if(excludeUnderscoredKeys === false ||
       key == '_id' || // exception of the rule: we want id
       excludeUnderscoredKeys === true  && key.startsWith('_') === false) {
      value = obj[key]
      html += '<div>'
      html += key
      html += '</div>'
      html += '<div>'
      if(value instanceof Object) {
        html = genHtml(value, html)
      }
      else {
        html += value
      }
      html += '</div>'
    }
  }
  html += '</div>'
  return html
}
function genHtmlDict(obj) {
  var html = '<dl>'
  for(var key in obj) {
    html += '<dt>' + key + '</dt>'
    html += '<dd>' + obj[key] + '</dd>'
  }
  html += '</dl>'
  return html
}
function genHtmlList(items) {
  var html = '<ul style="border-top: 1px solid silver;">'
  for(var i=0; i < items.length; i++) {
    html += '<li style="\
      border-bottom: 1px solid silver; \
      display: inline-block; \
      Gwidth: 40%;">'
    html += items[i]
    html += '</li>'
  }
  html += '</ul>'
  return html
}
function showDB(db, ele) {
  var html = ''
  var i, row, rows, items = null
  db.allDocs({include_docs: true}, function(err, docs) {
    if(err) {
      ele.innerHTML += 'An error occured: ' + err
      return false
    }
    rows = docs.rows
    for(i=0; i < rows.length; i++) {
      row = rows[i]
      html += genHtml(row.doc)
      items = ['id', row.id]
      for(key in row.doc) {
        if(key.startsWith('_') === false) {
          items.push(key)
          items.push(row.doc[key])
        }
      }
      //html = genHtmlList(items)
    }
    ele.innerHTML = html
  });
  return true
}
function initializeDB(db_name, ele=null) {
  var PouchDB = require('pouchdb')
  var db = new PouchDB(db_name) // ini pouch-db
  if(ele !== null) {
    db_ele = document.createElement('div')
    ele.insertBefore(db_ele, ele.firstChild)
    showDB(db, db_ele)  // show data initially
    db.changes({since: 'now', live: true}).on('change', function() {
      showDB(db, db_ele) // show new data after db.put()
    });
  }
  return db
}
function showMessage(msg) { 
  // Add ele with msg and insert it as first-child of body.
  var ele = document.body.insertBefore(
    document.createElement('div'),document.body.firstChild)
  ele.innerHTML = msg
  console.log(msg) 
}
function main(db_name, ele) {
  var db = initializeDB(db_name, ele)
  var id = '27'
  var title = 'Anui title'
  var desc = 'Describing the entry without actually saying anything.'
  var doc = {
    _id: id,
    title: title,
    desc: desc,
  }
  deleteEntry(db, id)
  addEntry(db, doc)
  db.put(doc)
    .then(function(d){afterPut(d)} )
    .catch(function(e){showMessage(e)})
  db.get(id)
    .then(function(d){afterGet(d)} )
    .catch(function(e){showMessage(e)})
} main(db_name, ele)
*/

var pouchee = new Pouchee('my_datbase', document.body)

setTimeout(function(){window.location.href=window.location.href},7000)
