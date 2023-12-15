# PHASE-3-PROJECT

#  How to use it 🙂

[![See how to use it](https://i.postimg.cc/4ygX60Cx/Screencast-from-2023-12-15-01-28-56.gif)](Link_URL)


This bank management system project performs the essential functions of banking software. It allows the user to:

- View database records.
- Create records.
- Delete records.

[Preview](https://ibb.co/fQymvmn)


   ## preview
<img src="https://i.ibb.co/zNBKJK7/Screenshot-from-2023-12-15-01-28-03.png" alt="Image of the app running in the terminal" title="Money Fantasy">



     
## Table of Contents
- [Technologiesused](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

- [Author & License](#author--license)

## Technologies used
![python version](https://img.shields.io/badge/python-3.11.0+-re.svg)
![pytest version](https://img.shields.io/badge/pytest-7.2.4+-cyan.svg)
![sqlalchemy version](https://img.shields.io/badge/sqlalchemy-2.1%2B-blue.svg)


## Installation

### 1. Clone the repository

```bash
git clone git@github.com:SHAKA-ZULU5/PHASE-3-PROJECT.git
```

### 2. Navigate to the project's directory

```bash
cd PHASE-3-PROJECT
```

### 3. Install all the required dependencies

The root directory of this repository contains the `Pipfile` with all the required Python libraries for this project and restricts them to this repository.

To install `Dependency` and any other required libraries, run:

```python
pipenv install
```

### 4. Enter the pipenv shell

```python
pipenv shell
```


## Usage
* To launch the project follow these commands:
```python
cd lib/dbfolder
```
```python
python3 bank.py
```

- Use the following options to navigate through the main menu:

   - Press 'S' to view records.
   - Press 'F' to add new records.
   - Press 'R' to delete a customer and associated data.
   - Press 'Q' to quit the program.

### View Records Menu

#### Customer Records

- Press 'C' to see a list of all customers.

#### Transaction Records

- Press 'T' to see transaction records for a specific customer.

#### Account Records

- Press 'A' to see account records for a specific customer.

#### Back to Main Menu

- Press 'B' to return to the main menu.

### Add Records Menu

#### Add a New Customer

- Press 'C' to add a new customer.
- Enter the first name and last name of the customer when prompted.

#### Add a New Transaction

- Press 'T' to add a new transaction.
- Enter the required details for the transaction, such as the account ID, amount, and description (deposit or withdrawal).

#### Add a New Account

- Press 'A' to add a new account.
- Provide the account type (savings or current), initial deposit, and customer ID.

#### Back to Main Menu

- Press 'B' to return to the main menu.

### Delete Customer

To delete a customer and their associated data:

- Press 'R' in the main menu.
- Enter the customer's ID when prompted.
- Confirm the deletion.

#
## 5. License

This project is licensed under the [license name]. See the [LICENSE](LICENSE) file for details.



## Author & License

Authored by [Khalid Mohamed](https://github.com/khalid0310) on behalf of [SHAKA-ZULU5](https://github.com/SHAKA-ZULU5).

Collaborators:
- [Brian Kawa](https://github.com/briankawa)
- [Amar Ahmednur](https://github.com/amaar7)
- [Denis Laboso](https://github.com/Laboso2023)
- [Owen Smith](https://github.com/mwangiowen)

Repository: [PHASE-3-PROJECT](https://github.com/SHAKA-ZULU5/PHASE-3-PROJECT)


Licensed under the [MIT](https://choosealicense.com/licenses/mit/)

