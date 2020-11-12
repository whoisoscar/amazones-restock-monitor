**Background**
--
Just a script to check the stcok status of items on Amazon ES.
With lockdown and all, many products are sold out quick, this will keep you notified when that desired product is back available.

**Installation**
--
To install files:
`````
git clone https://github.com/whoisoscar/amazones-restock-monitor
`````
To Install Required Modules:
`````
pip install -r requirements.txt
`````

**Usage**
--
`````
cd amazones-restock-monitor
python3 main.py
`````
Configurations are done within the main.py file.
These configurations include:
* Amazon ES product link
* Discord Webhook URL
* Monitor Delay