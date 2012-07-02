robotframework-selenium2library-extensions
==========================================
Extends the [robotframework-selenium2library](https://github.com/rtomac/robotframework-selenium2library/ "robotframework-selenium2library").

Extra keywords
==============

[Action Chains](http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html)
Lazily initiates an action chains.

   Chain Sleep
   Chain Click
   Chain Click And Hold
   Chain Drag And Drop
   Chain Key Up
   Chain Key Down
   Chain Move By Offset
   Chain Move To Element
   Chain Move To Element With Offset
   Chain Release
   Chain Send Keys
   Chain Send Keys To Element

Execute the created action chains:

   Chains Perform Now

Drag and drop shortcuts: immediately performed.

   Drag And Drop
   Drag And Drop With Offset

Page Tests:

    Select IFrame
    Is Element Present
    Is Visible

Note: some limitations regarding drag and drop
==============================================
Note that action chains are not well supported by some dirvers.
In particular, HTML5 Drag and Drop have not worked so far for firefox and chrome
on my linux machine.
It is working with jquery's drag and drop.

Here are some notable webkit and chrome-driver bugs to follow:
* keyup can't simulated: (https://bugs.webkit.org/show_bug.cgi?id=16735)
* html5's drag and drop with chrome-driver: (http://code.google.com/p/selenium/issues/detail?id=3604)

Requirements
============
* Robotframework
* robotframework-selenium2library

Installation
============

    git clone https://github.com/hmalphettes/robotframework-selenium2library-extensions.git

And in your robotframework test, import the library. For example:

    *** Settings
    Library           ${CURDIR}/../../src/Selenium2LibraryExtensions    WITH NAME    Selenium2LibraryExtensions


Run the tests
=============

    ./test/run_tests.sh

How-to extend robotframework-selenium2library rather than fork it
=================================================================
Use any of the techniques documented to write a python plugin for robotframework.
In your keyword's method here how to access the active selenium's browser:

   selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
   selenium_browser = selenium2lib._current_browser()

Now refer to selenium driver's python API and go wild.

    
License
=======
ASL-2.0 just like robotframework-selenium2library.
