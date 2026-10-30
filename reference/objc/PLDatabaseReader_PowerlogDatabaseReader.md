# `PLDatabaseReader`

- Image: [`/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader`](../userland/System__Library__PrivateFrameworks__PowerlogDatabaseReader.framework__PowerlogDatabaseReader.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{sqlite3=} _dbConnection;
```

## Properties

```
@property (T^{sqlite3=},V_dbConnection) dbConnection;
```

## Instance methods

```
-[PLDatabaseReader dealloc];
-[PLDatabaseReader performStatement:];
-[PLDatabaseReader setDbConnection:];
-[PLDatabaseReader dbConnection];
-[PLDatabaseReader initWithDatabaseFile:];
-[PLDatabaseReader stringValueOfTable:];
-[PLDatabaseReader tableNamesFromDatabase];
-[PLDatabaseReader openDatabaseFile:];
-[PLDatabaseReader prepareStatementAndPerformWithString:];
```
