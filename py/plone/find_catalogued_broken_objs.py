
# Find broken objs, to be able to recreate them, so reindexing or upgrading will work:
# Usage: Via ZMI, locate to portal_skins/custom, select "Script(Python)" of dropdwonmenu, insert these lines, save. Then click "Test"-tab on top.
from Products.CMFCore.utils import getToolByName
catalog = getToolByName(context, 'portal_catalog')
results = catalog.searchResults(Language='all')
for brain in results:
    try:
        item = brain.getObject()
    except:
        print brain.getPath()
return printed

#TODO: Extend this script to bypass expired-content-permisson-check, to get *all* objs:
#mtool = context.portal_membership
#show_inactive = mtool.checkPermission('Access inactive portal content', context)
#contents = context.portal_catalog.queryCatalog(show_inactive=show_inactive)
