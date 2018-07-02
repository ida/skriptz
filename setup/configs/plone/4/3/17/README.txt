What
====

Version-configs for differing Plone-versions that work and are structured into
several configs for:

- plone.recipe.zope2instance
- Products.CMFPlone
- Plone



Why
===

- If it's not reproducible, it doesn't exist.

- Some users may want to choose a reduced setup, meaning
not install Plone-addons defined in the Plone-egg.

- Get an overview of minimun eggs needed and optionally additonal eggs wanted.



How
===

These configs have been generated with these steps:

1. Install a Plone standalone-instance of wanted Plone-version with the
UnifiedInstaller, collect all egg-names and their versions of the eggs-cache
and create a file 'versions.cfg' of it.

2. Create a directory, move versions.cfg into it and add a file 'buildout.cfg'
with the following content:

    [buildout]
    extends = versions.cfg
    [instance]
    recipe = plone.recipe.zope2instance


3. Run buildout, create a 'plone.recipe.zope2instance.cfg' of the eggs-cache.

4. Rename eggs-directory to zope2_eggs, in buildout.cfg append:

    eggs = Products.CMFPlone


5. Run buildout, create a 'Products.CMFPlone.cfg' of the diff between
the directory 'zope2_eggs' and 'eggs'.

6. Rename 'eggs' to 'cmfplone_eggs', in buildout.cfg change eggs to Plone:

    eggs = Plone

7. Run buildout, create a 'Plone.cfg' of the diff between the directories
'cmfplone_eggs' and 'eggs'.



Approach
========

- The UnifiedInstaller delivers an awesome reference for bullet-proof working
Plone-setups, let's ectract the used egg-versions of there.

- To get an idea which main-egg needs which dependency-eggs, separate the
configs.



Epilogue
========

- The used buildout was installed with pip, unlike the UnifiedInstaller which
installs buildout via a script called 'bootstrap.py'. For that it was necessary
t pin plone.recipe.zope2instance to 4.4.0 (currently newest vs).

- The version-configs were generated with scripts living in this directory of
this repo:

    '../../../py/plone/buildouting'

