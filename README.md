# Auto Reservation in Inline

## Description
This is a program that allows users to pre-fill information on the reservation website Inline, enabling them to secure a booking quickly.

## Dependencies:
* [undetected_chromedriver](https://pypi.org/project/undetected-chromedriver/)
* [selenium](https://pypi.org/project/selenium/)

## How to use
You only need to fill in the basic information in these few lines of code.
```
name = 'xxx'
phone_number = 'xxxxxxxxxx'
gmail = 'xxxxxxxx@gmail.com'
```
and this section of code
```
lst_time = ['19', '17', '13', '11', '15']
```
allows you to select the time you would like to dine at the restaurant in a 24-hour format.

Enter the Inline reservation URL you want to automate in the code below.
```
driver.get('https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg')
```




### Once everything is set up, you can run the program and wait for the restaurant to release reservation slots!
