# CNC-Compiler
Final Project for my Programing Languages Class
Requirements:
Anaconda
Setup the virtual environment:
clone repo
download anaconda
Once Anaconda is downloaded open up Anaconda Powershell and type in: "conda init powershell"
Then close it and go to VS Code terminal and type: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Then trash that terminal and try to run a sample file
Setup your own virtual environment using "create -n environment_name python=3.10 anaconda"
conda activate environment_name
Run these commands to download the requirements:
conda install -c "conda-forge/label/gcc7" openjdk
pip install antlr4-python3-runtime
Run it:
python run_me.py
