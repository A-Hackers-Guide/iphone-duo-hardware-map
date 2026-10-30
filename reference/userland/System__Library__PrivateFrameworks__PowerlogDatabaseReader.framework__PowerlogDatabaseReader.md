# `/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader`

iOS 27.2 dyld shared cache image. Version `3486.52.2.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libsqlite3.dylib`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 0 protocols, 9 methods, 1 properties

### Class pages

Every class and protocol, with its methods: [`PLDatabaseReader`](../objc/PLDatabaseReader_PowerlogDatabaseReader.md)

### Classes

`PLDatabaseReader`

### Properties

```
@property (T^{sqlite3=},V_dbConnection) dbConnection;
```

## Strings (22)

```
SELECT name FROM sqlite_master WHERE type = 'table' AND name LIKE \"%PL%\"
SELECT * FROM '%@';
failed to open conn: %d\n
PRAGMA cache_size = 50;
Error prepare statement; query =%@, error = %s
Invalid table name/database file
)
Input database file (%@) is invalid!
failed to initialize library: %d\n
!!! returnCode=%s
Fail to query tables in database
PRAGMA table_info('%@');
(
%@
Fail to open connection to database file!
No table defined
,
failed to set cache size to 50 x 4KB: %d
[SQLITE] UNKNOWN DATATYPE colType=%d
Database busy!
ERROR: sqlite3_step error=%d, %s
Invalid statement/connection!
```
