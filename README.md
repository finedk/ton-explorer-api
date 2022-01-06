# TON explorer api
The simple python class for use official TON explorer API

**Distributed by GPL-3.0 License**
## Content
- [Appointment](#Appointment)
- [Example](#Example)
- [Installation and use](#Installation-and-use)
- [Technical information](#Technical-information)
- [From the author](#From-the-author)

## Appointment
This class can be used separately from the main script, with its help you can facilitate the process of working with the TON explorer api

## Example
The fast recording process my script with main class

*More in the `for_readme` folder*

![example](https://github.com/alekszavg/ton-explorer-api/blob/main/for_readme/bandicam-2022-01-06-14-42-05-357.gif)

## Installation and use
First you need `git clone https://github.com/alekszavg/ton-explorer-api.git`

Than you need `pip install -r requirements.txt`

You can use `import` to got this class 

Make import class `TonExplorer` from `main.py` in this file is needed class

![how-use](https://github.com/alekszavg/ton-explorer-api/blob/main/for_readme/2022-01-06%2015-10-29%20Скриншот%20экрана.png)

Then you created instance of a class with its own settings

![settings](https://github.com/alekszavg/ton-explorer-api/blob/main/for_readme/2022-01-06%2015-16-47%20Скриншот%20экрана.png)

## Technical information
+ I use official TON explorer api
+ Is request limit - 30 req/minute
+ If something is wrong my class return you `False`. If all is ok he return what you requested or dict (dict is json from request answer)

## From the author
I wrote this in 2 days and so I'm not sure there are no bugs! If you want to offer something, then create a request, I will try to respond to it in time

**Good luck!**
