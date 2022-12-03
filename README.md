# tapu_müd_bil_sis
Tapu Müdürlüğü Bilgi Sistemi

### Filesystem
```bash
├── README.md                      
├── database                    
│   ├── tapu_db_data.sql            # basic queries to test datas
│   ├── tapu_db_queries.sql         # inserts datas to the created tables
│   └── tapu_db_schema.sql          # creates 4 table
└── scripts
    ├── database.py                 # database api script to comm with database
    └── gui.py                      # modern gui to queries and results
```

### Installation
First of all check that how can you install related modules can be installed to your system.
Following script may not work!

```bash
pip3 install -r requirements.txt
```

### How to Run

##### Step-1
It is need to be create a database as "tapu_db" with PostgreSQL.

##### Step-2
Run prepared sql files in tapu_db with specific order as following;

- 1.tapu_db_schema.sql
- 2.tapu_db_data.sql

##### Step-3
And now, it is time to run example queries.
Run tapu_db_queries.sql step by step to see the datas.

##### Step-4: Query with Pyhon API
Change PostgreSQL password according to your system.

```bash
python3 database.py
```

##### Step-5: GUI

```bash
python3 gui.py
```