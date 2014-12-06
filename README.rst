IN DEVELOPMENT: PLEASE DON'T USE
--------------------------------
sassdog
-------


Simple python command line tool to compile .scss files into .css files when they are changed. Sassdog spits out minified .css files that are ready to use as normal.

Sassdog glues together watchdog, pyscss and csscompressor to automate sass compilation, without the need to use ruby or js. If your using django/flask/tornado... then you might find sassdog a handy tool for developing web applications. Once sassdog is started, it will sit and wait for you to create and modify .scss files (which are sass files) and then compile them into .css files.


Installing
----------
Using pip you can install with:

	pip install https://github.com/nickpolet/sassdog/zipball/master

Useage
------
Move to the directory of your project:

	cd path/to/awesome/project/

Then start sassdog:

	sassdog

Sassdog will sit a wait untill you create/modify a .scss file. When you make changes to the sass files it will compile them into loving minified css files.

If you want to compile all your .scss files when starting sassdog, run:

	sassdog --compile

To stop sassdog, just press CTRL+C to stop the python process.
