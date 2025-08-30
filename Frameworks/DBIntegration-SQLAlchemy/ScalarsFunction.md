# `scalars()`
In SQLAlchemy, the .scalars().all() function is used to retrieve a list of "scalar" results from a query. This is particularly useful when you are querying for a single column or an ORM entity, and you want to receive those values directly as Python objects, rather than as Row objects.
Here's a breakdown:
scalars():
This method is called on a Result object (which is typically returned by session.execute()). It transforms the Result object into a ScalarResult object. A ScalarResult object is specifically designed to handle cases where each row in the result set contains a single "scalar" value (e.g., a single column value or a single ORM entity). It effectively "unpacks" the first element from each Row object.
.all():
This method is then called on the ScalarResult object. It fetches all the results from the query and returns them as a Python list.
In essence, session.execute(select(MyEntity)).scalars().all() will:
Execute the SELECT statement (select(MyEntity)).
Obtain a Result object.
Transform this Result into a ScalarResult, which focuses on the primary (first) scalar value in each row (in this case, instances of MyEntity).
Fetch all these scalar values and return them as a list of MyEntity objects.

# `order_by()`
The order_by() function in SQLAlchemy is used to specify the order in which results from a query should be returned. It corresponds to the ORDER BY clause in SQL.
Basic Usage:
To order query results, you call the order_by() method on a Query object (or a Select object in SQLAlchemy 2.0 style) and pass the column(s) by which you want to order
Descending Order:
To order in descending order, use the .desc() method on the column:
Multiple Columns:
You can order by multiple columns by passing them as separate arguments to order_by():

Calculated Fields or Expressions:
You can also order by calculated fields or SQL expressions. For example, using a case() statement for custom ordering logic.
Note: When using multiple order_by() calls on the same query object, SQLAlchemy combines them into a single ORDER BY clause in the generated SQL, respecting the order in which they were called. There is no difference between query.order_by(col1).order_by(col2) and query.order_by(col1, col2).