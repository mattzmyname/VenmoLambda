pip3 install;
deactivate;
cd venv37/lib/python3.7/site-packages;
zip -r ../../../../my-deployment-package.zip .;
cd ../../../../;
zip -g my-deployment-package.zip *.py;

