# Bot Covid

<div align="center">
 <img  src="https://user-images.githubusercontent.com/56304060/116772748-90f48300-aa6e-11eb-8c9d-920d16f07132.jpg"  alt="Twilio"  width="250"  />
</div>


## About

This is whatsapp bot that I made with the help of `Flask` and `Twilio's messaging API`. It gives information about the current COVID status in all over the world. One can narrow down the search by providing particular place name or date. It also gives a list of verified oxygen cylinder resources and hospitals or clinics with avialable COVID bed based on the geographic location. The main purpose of this app is to help people for accessing the verified data so that they can resolve their issues.

### How it works

The app uses Twilio's messaging API to create a WhatsApp bot. The bot runs in the backend which is made by Flask, and it is responsible for collecting all the messaging queries and giving appropriate responses.

## Features

- Gives current updates about COVID-19 in all over the world
- User can query for a particular place to know about the status
- Gives verified information about oxygen suppilers and hospitals that have vaccant COVID beds
- Regularly update verified data
- Easy to use

## How to use it

1. Add this `+1 (415) 523-8886` number in your contacts
2. Open `WhatsApp` chat for this number and type a message `join all-fuel`
3. The line above is a code to register your number in Twilio's database
4. Type-in a `hi` message and the bot will introduce itself

## Set up

### Requirements

> If you wanna contribute to this project, then do the following steps:
- Fork this repository
- I'm assuming you have `git` and `python 3.7+` installed on your system
- Open up a terminal and clone the forked version of this project to your local system using this command `git clone https://github.com/HOTSONHONET/CovidWhatsapp.git`
- Create a virtual environment by this command `virtualenv <name-of-your-env>`
- Activate your virtual env by this command `<name-of-your-env>/Scripts/activate`
- Install all the dependecies by using this command `pip install -r <path-to-the-requirements.txt-file-in-the-cloned-repo>`
- Then, use these [guidelines](https://www.dataschool.io/how-to-contribute-on-github/) to contribute in this project

### Cloud deployment

I have deployed this application on [![Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)



## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

