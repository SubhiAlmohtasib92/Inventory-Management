# Inventory-Manager
An inventory management system using Flask

## Getting Started


## Clone this repository and set your path to it's folder, to get it up and running on your local system.

```
https://github.com/SubhiAlmohtasib92/Inventory-Management.git

cd Inventory-Management
```
## What to look for here?
- [System Summary](#system-summary)
- [Running the app](#running-the-app)
- Features
  1. [Adding Products and Locations](#adding-products-and-locations)
  2. [Moving Products](#moving-products)
  3. [Products Report](#Products-Report)
- [Built Using](#built-using)
### Prerequisites

Assuming you have Python, proceed to install the rest using the command below:

```
pip3 install -r requirements.txt
```
## System Summary

This system is built to simulate a warehouse environment and handles balancing quantities over warehouses. It has 4 main views including *Homepage*,*Products*,*Locations* and *Movements*. **Products** and **Locations** let you add,edit entries from the system. **Movements** lets you move items into the central warehouse, out of the central warehouse; also to and from various locations.It also displays transfer history. **Homepage** will display products,warehouses and their respective balanced quantities.


## Running the app
1) Import inventory_management.sql to your MySQL database

2) Open the folder you've created and run the following commands:

```
 env\Scripts\activate
 
 flask run 
``` 

Either copy paste the url as shown above into your browser **or** simply check into *localhost:5000/* as shown below. You will see the initial views of each page as no actions are performed.

![init_site](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/initialview.png?raw=true)

## Features

### Adding Products and Locations
Products require product name and quantity to be filled. Location only requires location name


![adding](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/addingNewProduct.png?raw=true)

![adding](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/Producthasbeenadded.png)

![adding](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/ProductsList.png?raw=true)

![adding](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/addingnewlocation.png?raw=true)

![adding](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/locationhasbeenadded.png?raw=true)

![adding](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/locationsList.png?raw=true)



### Moving products
Here products can be moved to a location, from a location as well as to and from a location. Products initially are not assigned to any locations from the central warehouse.

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementsPage.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/addingnewmovement.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementhasbeenadded.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementvalidation-part1.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementvalidation-part2.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementvalidation-part3.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementvalidation-part4.png?raw=true)

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementsList.png?raw=true)

### Products Report
This report will show products balance in each location

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/ProductBalanceReport.png)



### Totals Report
This report will show products Totals and the quantity of each product per location

![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/movementsList_total.png)


![mvng](https://github.com/SubhiAlmohtasib92/Inventory-Management/blob/master/images/totalspage.png)


# Built using
- Flask



