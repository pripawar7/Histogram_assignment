- This is a histogram generator for Campaign contribution to each presidential candidate during 2015-16 from commitees.
- The project is setup using a Python script for extracting the text data and converting it to javascript usable .json format. Plotting the graph is done using javascript and plotly.js.

Requirements:
1) Python 2.7
  - Can be downloaded from https://www.python.org/downloads/
2) npm http-server
  - Install npm from https://www.npmjs.com/get-npm
  - Install http-server using 'sudo npm install -g http-server'

Steps to run the project:
(Note: Currently there are more than 1500 eligible records to be displayed. User has the flexibility to provide number or records he/she wishes to display on the Histogram)
1) Run 'python generator.py number_of_records_to_be_displayed'
   - E.g: python generator.py 10
2) Run 'http-server -c-1'
