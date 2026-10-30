# `SFSQLite`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 16 properties, 70 instance methods, 0 class methods

## Instance variables

```
@"<SFSQLiteDelegate>" _delegate;
@"NSString" _path;
@"NSString" _schema;
@"NSString" _schemaVersion;
@"NSMutableDictionary" _statementsBySQL;
@"NSString" _objectClassPrefix;
q _synchronousMode;
i _userVersion;
^{sqlite3=} _db;
Q _openCount;
@"NSDateFormatter" _dateFormatter;
B _hasMigrated;
B _corrupt;
B _traced;
@"NSDateFormatter" _oldDateFormatter;
```

## Properties

```
@property (T^{sqlite3=},N,V_db) db;
@property (TQ,N,V_openCount) openCount;
@property (TB,N,V_corrupt) corrupt;
@property (T@"NSMutableDictionary",R,N,V_statementsBySQL) statementsBySQL;
@property (T@"NSDateFormatter",&,N,V_dateFormatter) dateFormatter;
@property (T@"NSDateFormatter",&,N,V_oldDateFormatter) oldDateFormatter;
@property (T@"NSString",R,N,V_path) path;
@property (T@"NSString",R,N,V_schema) schema;
@property (T@"NSString",R,N,V_schemaVersion) schemaVersion;
@property (T@"NSString",&,N,V_objectClassPrefix) objectClassPrefix;
@property (Ti,N,V_userVersion) userVersion;
@property (Tq,N,V_synchronousMode) synchronousMode;
@property (TB,R,N) isOpen;
@property (TB,R,N,V_hasMigrated) hasMigrated;
@property (TB,N,V_traced) traced;
@property (T@"<SFSQLiteDelegate>",&,N,V_delegate) delegate;
```

## Instance methods

```
-[SFSQLite setUserVersion:];
-[SFSQLite setDb:];
-[SFSQLite changes];
-[SFSQLite db];
-[SFSQLite userVersion];
-[SFSQLite propertyForKey:];
-[SFSQLite open];
-[SFSQLite openWithError:];
-[SFSQLite setProperty:forKey:];
-[SFSQLite rollback];
-[SFSQLite analyze];
-[SFSQLite close];
-[SFSQLite setCorrupt:];
-[SFSQLite begin];
-[SFSQLite lastInsertRowID];
-[SFSQLite vacuum];
-[SFSQLite dealloc];
-[SFSQLite corrupt];
-[SFSQLite setDateFormatter:];
-[SFSQLite dateFormatter];
-[SFSQLite end];
-[SFSQLite dropAllTables];
-[SFSQLite creationDate];
-[SFSQLite schemaVersion];
-[SFSQLite setDelegate:];
-[SFSQLite schema];
-[SFSQLite delegate];
-[SFSQLite remove];
-[SFSQLite executeSQL:];
-[SFSQLite setDateProperty:forKey:];
-[SFSQLite datePropertyForKey:];
-[SFSQLite isOpen];
-[SFSQLite path];
-[SFSQLite removePropertyForKey:];
-[SFSQLite selectCountFrom:where:bindings:];
-[SFSQLite statementsBySQL];
-[SFSQLite synchronousMode];
-[SFSQLite _createSchemaHash];
-[SFSQLite _synchronousModeString];
-[SFSQLite _tableNameForClass:];
-[SFSQLite allTableNames];
-[SFSQLite attemptProperDatabasePermissions];
-[SFSQLite autoVacuumSetting];
-[SFSQLite columnNamesForTable:];
-[SFSQLite dbUserVersion];
-[SFSQLite deleteFrom:matchingValues:];
-[SFSQLite deleteFrom:where:bindings:];
-[SFSQLite hasMigrated];
-[SFSQLite initWithPath:schema:];
-[SFSQLite insertOrReplaceInto:values:];
-[SFSQLite objectClassPrefix];
-[SFSQLite oldDateFormatter];
-[SFSQLite openCount];
-[SFSQLite removeAllStatements];
-[SFSQLite select:from:];
-[SFSQLite select:from:mapEachRow:];
-[SFSQLite select:from:where:bindings:];
-[SFSQLite select:from:where:bindings:orderBy:limit:block:];
-[SFSQLite select:from:where:bindings:orderBy:limit:forEachRow:];
-[SFSQLite selectAllFrom:where:bindings:];
-[SFSQLite selectFrom:where:bindings:limit:];
-[SFSQLite selectFrom:where:bindings:orderBy:limit:block:];
-[SFSQLite setObjectClassPrefix:];
-[SFSQLite setOldDateFormatter:];
-[SFSQLite setOpenCount:];
-[SFSQLite setSynchronousMode:];
-[SFSQLite setTraced:];
-[SFSQLite statementForSQL:];
-[SFSQLite traced];
-[SFSQLite update:set:where:bindings:limit:];
```
