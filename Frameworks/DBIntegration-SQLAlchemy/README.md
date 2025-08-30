# Flask: Database Integration
- Flask integrates with databases primarily through Object-Relational Mappers (ORMs) like SQLAlchemy, often facilitated by the Flask-SQLAlchemy extension

## Flask-SQLAlchemy
- a Flask extension that integrates the SQLAlchemy ORM (Object Relational Mapper) with the Flask web framework
- acts as a bridge between your Flask application and your database, allowing you to manage your data using Python objects and methods, which significantly improves developer productivity and code readability
- simplifies database interactions within Flask applications by providing a convenient way to work with relational databases using Python objects instead of raw SQL queries

### 1. Choose a Database and Install Flask-SQLAlchemy
- Select a database system (e.g., SQLite, PostgreSQL, MySQL)
- install the Flask-SQLAlchemy extension using pip: `pip install Flask-SQLAlchemy`


### 2. Configure the Database URI
- In your Flask application's configuration, set the `SQLALCHEMY_DATABASE_URI` to specify the database connection details
- For example, for a SQLite database named site.db: `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'`

### 3. Define Database Models
- Create Python classes that represent your database tables
- these classes typically inherit from db.Model (provided by Flask-SQLAlchemy) and define columns using `db.Column` or `mapped_column`-
 with appropriate data types
- **mapped_column (from sqlalchemy.orm)**: `username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)`
    - represents a more modern and recommended approach introduced with SQLAlchemy 2.0, offering enhanced features, particularly in conjunction with Python type annotations and the Mapped generic type
    - specifically an ORM construct and is only valid within a Declarative class mapping
    - allows for more concise and type-safe model definitions, enables automatic derivation of column properties and can lead to cleaner code by inferring types and nullability
        - mapped_column with type annotations significantly improves static analysis and IDE features like type checking and autocompletion
        - db.Column does not offer this level of integration with type annotations
    - when used with Mapped from sqlalchemy.orm, mapped_column can infer the database column's type and nullability directly from the Python type annotation, reducing the need for explicit type declarations within the mapped_column function itself
    - enhances static analysis and IDE support, allowing linters and IDEs to provide better type checking and autocompletion
- **db.Column (or sqlalchemy.Column)**: `username = db.Column(db.String(80), unique=True, nullable=False)`
    - the traditional way to define a column in SQLAlchemy
    - directly specifies the database column's properties, such as its data type (e.g., db.Integer, db.String), nullability, primary key status, and default values
    - is still valid and functional in SQLAlchemy 2.0 and Flask-SQLAlchemy
    - Column is part of SQLAlchemy Core and can be used for defining Table objects in a more "core" way, independent of the ORM
**For new projects or when updating existing ones to leverage SQLAlchemy 2.0 features, mapped_column used in conjunction with Mapped and type annotations is the recommended approach due to its improved type safety, static analysis benefits, and alignment with modern Python practices. db.Column remains a valid option, especially in contexts where type annotations are not desired or when working with SQLAlchemy Core directly**


# DB Functions
- [`execute()`]()
- [`scalars()`]()
- [`order_by()`]()
- [`all()`]()
- []()
- []()



# Resoureces and Tools
- [Postman Docs](https://learning.postman.com/docs/introduction/overview/)
- [Status Codes](https://www.webfx.com/web-development/glossary/http-status-codes/)