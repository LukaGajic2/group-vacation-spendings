# GROUP VACATION SPENDINGS

A command line based Python program to handle data automation for a fictional group of people who are on vacation and will track their common spendings(such as restaurant bills, tickets fees, taxi bills,etc...).
<br/>
<br/>

## Idea
<br/>
Idea is that, at the end of the day, provide amount that every member have spent that day on common activities. The program will then update total amount spent by each member and print it to terminal.
Then it will calculate average spending and compare to every member spending and calculate difference towards calculated average spending and print it to terminal.

In that way the whole group will have accurate numbers in spendings and could compare and adjust their spendings under or at the end of vacation.


Link to live site:
- https://vacation-spendings.herokuapp.com/
<br/>
<br/>
<br/>

![Alt text](/images/am-i-responsive.png)
<br/>
<br/>
<br/>

## PROCESS CHART
<br/>

![Alt text](/images/chart-shot.png)

<br/>
<br/>
<br/>

# FEATURES

- At the start user can read short instructions about the programme and some guidelines on how to input correct data.

![Alt text](/images/first-shot.png)

- After providing data program will evaluate if the data is correct and proceed with further steps.

![Alt text](/images/validation-shot.png)

- After evaluating steps the programme will execute all functions and calculate and print new total amount spend by each group member and ,as well, new average spending's per group member. 

![Alt text](/images/result-shot.png)



## Testing

I confirm that I have tested this project manually by following steps:
- Passed the code through PEP8 linter and no errors reported
- Giving invalid inputs: strings instead for numbers, float numbers instead of whole numbers, less or
more then 5 required values
- Tested in my local terminal


## Validator testing

- PEP8
    - returned E501 error 'code line too long'
    - all errors have been fixed

# DEPLOYMENT

This project has been deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Create a new Heroku app
    - Set Config Vars (CREDS and PORT)
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy

# LANGUAGES
- Python 3.11.3
<br/>

# CREDITS

-Code Institute for the deployment template
