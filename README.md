# FunkyMon
## For Developer use only
### Overview
* This tool has been generated from a blank [web2py](web2py.markdown) repo
* Currently hosted at [dataprocessing.pythonanywhere.com](https://dataprocessing.pythonanywhere.com/welcome/default/index)
* Virtual Machine that is hosting the site can be accessed [here](https://www.pythonanywhere.com/user/dataprocessing/)
### Local Dev Environment Setup
* Clone this repository: https://github.com/barry4356/FunkyMon.git
* Download web2py package to allow running locally [here](https://www.web2py.com/init/default/download)
* Ensure you can run web2py locally
    - extract the `web2py.zip` wherever you want to run it from on your PC
    - open the web2py folder
    - open `cmd` command line window
    - type: `python.exe web2py.py` to launch a local server
        - **Note**: May require python to be installed on your machine. See [this](https://www.python.org/downloads/) if you have issues running web2py
    - Command window will pop up telling you the IP address and port to open local browser session
    - Can be killed by closing the command prompt window
* Move the **entire** contents of the cloned repository into your web2py directory, replacing all files/folders
* Rename the directory into whatever you want
* You can then run your local instance of web2py following the steps:
    - open the repository folder
    - open `cmd` command line window
    - type: `python.exe web2py.py` to launch a local server
### Workflow
* Name any personal/feature branches whatever you want
* `development` branch is what is deployed to [dataprocessing.pythonanywhere.com](https://dataprocessing.pythonanywhere.com/welcome/default/index)
    - branch is not locked down; breaking the branch breaks the deployed software
* `master` branch is locked down, pull request only