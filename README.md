Try using Binder for notebooks online?
https://github.com/jupyterhub/binderhub

binder can use requirements.txt to imoort python libraries using pip
https://mybinder.readthedocs.io/en/latest/sample_repos.html

gui code for programming guide is currently in longterm folder, using pyinstaller, http://www.pyinstaller.org/ to solve portability issues. Hopefully. 

run,
pyinstaller --distpath ./portable mess.py

to create the mess executable in portable -> mess -> ./mess

# qprogramming
Quantum Engineering CDT Quantum programming guide

The current pdf is called main.pdf

Latex style guide,

Referencing, please use \autoref not \ref for figures, sections and tables.
use \cite for references and check the bib file for the reference before you add a repeat.
Labelling, please don't put spaces in labels
