# CNC-Compiler
Final Project for my Programing Languages Class
The goal was to make turtle draw the basic shape of snorlax's face.
Requirements:
Anaconda
Setup the virtual environment:
clone repo
download anaconda
Once Anaconda is downloaded open up Anaconda Powershell and type in: "conda init powershell"
Then close it and go to VS Code terminal and type: "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"
Then trash that terminal and try to run a sample file
Setup your own virtual environment using "create -n environment_name python=3.10 anaconda"
conda activate environment_name
Run these commands to download the requirements:
conda install -c "conda-forge/label/gcc7" openjdk
pip install antlr4-python3-runtime
Run it:
python run_me.py

When adding new gcodes to the gcodes.g4 file:
make sure to follow the syntax already presented there
run 'java -Xmx500M  -cp ".\antlr.jar;$CLASSPATH"  org.antlr.v4.Tool -Dlanguage=Python3 -visitor gcode.g4'
the code in gcodeVisitor.py gets overwritten so save it to then save the functionality of the old gcodes