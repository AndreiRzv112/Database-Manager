# Database Manager
Database Manager is a tool made in Python that helps you interact with your own sqlite3 db.

# Usage

```python
from manager import database
db = database()

db.create(name="database_name", dir="database_folder") 
# "dir" stands for directory, it can be None
```
