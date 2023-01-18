## Shoe Inventory - OOP Capstone
---

## Table of Contents

   1.[Description](#desc)\
   2.[How To Install](#inst)\
   3.[How To Use](#use)\

---

## 1.Description. <a name="desc"></a>

Built during HyperionDev Software Engineering Bootcamp.
This script will read "inventory.txt" and based on your choice
will show tables, return lowest stock ... see <a name="use">How to Use</a> for more

---

## 2.How to install. <a name="inst"></a>

Click on "<> Code" button in this repository.\
Click "Download zip"
Unzip Files
And you are done!

---

## 3. How to Use. <a name="use"></a>

Run "inventory.py". You should see the following: 

```
>>> Starting Shoe Inventory Managemnet System <<<

>>> 24 shoes were loaded from 'inventory.txt' <<<

Shoe Inventory Managemnet System:
  1. Update Shoes from 'inventory.txt'.  
  2. View Shoes in database.
  3. Show 'Low Stock' shoe.
  4. Put 'Sale' on highest qty shoe.
  5. Calculate total value / shoe.
  6. Search for shoe.
  0. Exit.

 >>>
```

In order to add shoes to database edit the "inventory.txt" file.\
Add data in order below:\

Country,Code,Product,Cost,Quantity

Remeber not to delete the 1st row from "inventory.txt" file.\

MENU: 

  1.[Update Shoes from 'inventory.txt'.](#one)\
  2.[View Shoes in database.](#two)\
  3.[Show 'Low Stock' shoe.](#three)\
  4.[Put 'Sale' on highest qty shoe.](#four)\
  5.[Calculate total value / shoe.](#five)\
  6.[Search for shoe.](#six)\
  0.[Exit.](#zero)\


## 1. Update Shoes from 'inventory.txt'.<a name="one"></a>
This menu option will update any changes made to "inventory.txt".\
This function is run o start-up.\ 
After any changes made to "inventory.txt" this must be run.\

Output:
```
 >>> 24 shoes were loaded from 'inventory.txt' <<<
```


## 2. View Shoes in database.<a name="two"></a>
This menu option will show list of all shoes in a table.\

Output:
```
_______________________________________________________________
| Product             | Code     | Qty | Cost | Country       |
| Air Max 90          | SKU44386 | 20  | 2300 | South Africa  |
| Jordan 1            | SKU90000 | 50  | 3200 | China         |
| Blazer              | SKU63221 | 19  | 1700 | Vietnam       |
| Cortez              | SKU29077 | 60  | 970  | United States |
| Air Force 1         | SKU89999 | 43  | 2000 | Russia        |
| Waffle Racer        | SKU57443 | 4   | 2700 | Australia     |
```


## 3. Show 'Low Stock' shoe.<a name="three"></a>
This menu option will show shoe with lowest stock.\

Output:
```
--------------------------[LOW ON STOCK]--------------------------
----------------------------[SKU95000]----------------------------
_______________________________________________________________
| Product             | Code     | Qty | Cost | Country       |
| Air Mag             | SKU95000 | 2   | 2000 | Vietnam       |
```


## 4. Show 'Low Stock' shoe.<a name="four"></a>
This menu option will show shoe with lowest stock.\

Output:
```
--------------------------[LOW ON STOCK]--------------------------
----------------------------[SKU95000]----------------------------
_______________________________________________________________
| Product             | Code     | Qty | Cost | Country       |
| Air Mag             | SKU95000 | 2   | 2000 | Vietnam       |
```


## 5. Calculate total value / shoe.<a name="five"></a>
This menu option will calculate and show total stock value for each shoe.\

Output:
```
________________________________________________________________________________
| Product             | Code     | Qty | Cost | Country       | Value / Item   |
| Air Max 90          | SKU44386 | 20  | 2300 | South Africa  | 46000          |
| Jordan 1            | SKU90000 | 50  | 3200 | China         | 160000         |
| Blazer              | SKU63221 | 19  | 1700 | Vietnam       | 32300          |
| Cortez              | SKU29077 | 60  | 970  | United States | 58200          |
```


## 6. Search for shoe.<a name="six"></a>
This menu option will search for shoe provided the code.\

Output:
```
Shoe Code: SKU29077

----------------------------[SKU29077]----------------------------
_______________________________________________________________
| Product             | Code     | Qty | Cost | Country       |
| Cortez              | SKU29077 | 60  | 970  | United States |

```


## 0. Exit.<a name="zero"></a>
Exits the script.
