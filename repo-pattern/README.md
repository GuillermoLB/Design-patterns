Before

- Repetition of code (without having a common interface)
- Switching (to NoSQL, text file, whatever...) requires a lot of changes in the code
  - So if we if we change **the data storing method** (SQL, NoSQL...) also need to change how we **access/modify** that data 
  - Could use an ORM like SQLAlchemy but only for SQL-based

After

- Separate the **data storing method** (PostRepository class) from the **accessing/modifying method** (Repository abstract class)
- For testing, we can create a **mock class** that inherits from the abstract class that represents the accessing/modifying method. Then, as it uses a dataclass, as data model, whe can make a mock implementation by using a python dictionary implementation instead of sql, etc.
Then in the unit tests that **are not going to tests the repo logic** but need to emulate the reo operation, we can mock that repo operations