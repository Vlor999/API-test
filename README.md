# API
Using the French `API` to get informations about the closest gas station, knowing prices and other.

## Launcher : 
### Import the project
Firstly we have to import the porject : 
```bash
git clone git@github.com:Vlor999/API-test.git
```

### Launching the project
You will need to have a connection to internet to make the `API` requests.
#### Virtuel Environment 
Here is the first step for the venv : 
```bash
python3 -m pip install -r requirements.txt 
```

#### The project 
```bash
source venv/bin/activate
python3 main.py
```
or
```bash
source venv/bin/activate
chmod u+x main.py
./main.py
```


## Structure

### Root Directory
- README.md

### `data` Directory
- struct.json
- timezone.xml
- `recup/`
  - mydatas-04-07-2025:`current-date`.json

### `src` Directory
- getter_data.py
- handle_data.py
- writter_data.py
- `__pycache__/`

### `venv` Directory

