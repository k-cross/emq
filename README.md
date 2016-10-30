# EMQ Project Website
* The basic website for the EMQ Project
## Dependencies
* pip install
    * flask-bootstrap
    * flask-wtf
    * flask-script
    * flask-mysql
## Setup
* If you use a IDE or some fancy text editor that generates a lot of noise (temp files) then please add those files to the .gitignore so you don't accidentally upload them.
* Check to make sure you have Selenium and Flask (>=v0.11)
    * You can try the command in your native cli: "pip install flask"
    * You can try the command in your native cli: "pip install selenium"
* Test User
    * Login as 'a' and pw is 'a'
    * Cart is automatically filled with 3 items of pID 1 and 2 of pID 2
### Using Virtual Environment
* Create Environment
    * virtualenv venv
* Use Environment
    * source venv/bin/activate ========> Works on *nix/mac
    * venv\Scripts\activate =========> Works on windows
