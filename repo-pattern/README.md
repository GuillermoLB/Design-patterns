# Repository Pattern

## Before

- **Issues:**
  - Repetition of code (without having a common interface).
  - Switching to a different storage method (e.g., NoSQL, text file, etc.) requires significant code changes.
    - For example, if we change **the data storing method** (SQL, NoSQL, etc.), we also need to change how we **access/modify** that data.
  - Using an ORM like SQLAlchemy is limited to SQL-based solutions.

---

## After

- **Solution:**
  - Separate the **data storing method** (e.g., `PostRepository` class) from the **accessing/modifying method** (e.g., `Repository` abstract class).
  - For testing:
    - Create a **mock class** that inherits from the abstract class representing the accessing/modifying method.
    - Use a `dataclass` as the data model to simplify mocking.
    - Implement a mock repository using a Python dictionary instead of SQL or other storage methods.
    - In unit tests that **do not test repository logic** but need to emulate repository operations, mock the repository operations.

---

This approach improves flexibility, reduces code repetition, and simplifies testing by decoupling the data storage logic from the access/modification logic.