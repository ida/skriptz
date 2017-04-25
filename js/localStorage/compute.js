+function summsumm() {
+/*
+  Get each last cell, sum their contents and append it as the last row of table.
+*/
+  var sum = 0
+  var table = document.getElementsByTagName('div')[0]
+  var columns = getFirstChildren(table)
+  // Last column is supposed to be column to sum,
+  // we get the second last, cause last is actually
+  // the row-delete-buttons, symobilzed with an 'X':
+  var column_sum = columns[columns.length-2]
+  var cells = getFirstChildren(column_sum)
+  for(cell in cells) {
+    // Exclude first two cells of new-row and column-header:
+    if(cell != 0 && cell != 1) {
+      var cell_content = cells[cell].textContent
+      sum += Number(cell_content)
+console.debug(sum)
+    }
+  }
+  addRow('<b>Sum</b>,' + sum)
+/*
+  TODO: Refresh(remove+add) last row, when re-calculating sum on next possible click.
	Better: Have a sum-symbol at the end of reach column and row, at click append sum (ignore uninterpretable input, collect any float)
	Detail: Regard that cents-notation could be done by with either commas (',') or points ('.').
	Search for secondlast symbol, should be the centinel. Could be a n-thousands-separator.
+*/
+}
+

