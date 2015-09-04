# Find broken objs, to be able to recreate them, so reindexing or upgrading will work:
from Products.CMFCore.utils import getToolByName
catalog = getToolByName(context, 'portal_catalog')
results = catalog.searchResults(Language='all')
for brain in results:
    try:
        item = brain.getObject()
    except:
        print brain.getPath()
return printed
