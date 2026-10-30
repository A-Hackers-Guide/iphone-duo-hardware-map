# `PLSQLStatement`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _isInsert;
B _isDelete;
^{sqlite3_stmt=} _statement;
@"NSObject<OS_dispatch_semaphore>" _dbSem;
```

## Properties

```
@property (T^{sqlite3_stmt=},V_statement) statement;
@property (TB,R,V_isInsert) isInsert;
@property (TB,R,V_isDelete) isDelete;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_dbSem) dbSem;
```

## Instance methods

```
-[PLSQLStatement finalize];
-[PLSQLStatement perform];
-[PLSQLStatement setStatement:];
-[PLSQLStatement dealloc];
-[PLSQLStatement setDbSem:];
-[PLSQLStatement reset];
-[PLSQLStatement isInsert];
-[PLSQLStatement dbSem];
-[PLSQLStatement statement];
-[PLSQLStatement bindValue:withFormater:atPosition:];
-[PLSQLStatement isDelete];
-[PLSQLStatement initWithSQLQuery:forDatabase:withDBSem:result:];
```
