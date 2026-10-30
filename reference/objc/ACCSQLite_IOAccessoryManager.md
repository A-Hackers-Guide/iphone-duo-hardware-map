# `ACCSQLite`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 16 properties, 68 instance methods, 0 class methods

## Instance variables

```
@"<ACCSQLiteDelegate>" _delegate;
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
B _shouldVacuum;
B _corrupt;
B _traced;
```

## Properties

```
@property (T^{sqlite3=},N,V_db) db;
@property (TQ,N,V_openCount) openCount;
@property (TB,N,V_corrupt) corrupt;
@property (T@"NSMutableDictionary",R,N,V_statementsBySQL) statementsBySQL;
@property (T@"NSDateFormatter",&,N,V_dateFormatter) dateFormatter;
@property (T@"NSString",R,N,V_path) path;
@property (T@"NSString",R,N,V_schema) schema;
@property (T@"NSString",R,N,V_schemaVersion) schemaVersion;
@property (T@"NSString",&,N,V_objectClassPrefix) objectClassPrefix;
@property (Ti,N,V_userVersion) userVersion;
@property (Tq,N,V_synchronousMode) synchronousMode;
@property (TB,R,N) isOpen;
@property (TB,R,N,V_hasMigrated) hasMigrated;
@property (TB,N,V_shouldVacuum) shouldVacuum;
@property (TB,N,V_traced) traced;
@property (T@"<ACCSQLiteDelegate>",&,N,V_delegate) delegate;
```

## Instance methods

```
-[ACCSQLite setUserVersion:];
-[ACCSQLite setDb:];
-[ACCSQLite changes];
-[ACCSQLite db];
-[ACCSQLite userVersion];
-[ACCSQLite propertyForKey:];
-[ACCSQLite open];
-[ACCSQLite openWithError:];
-[ACCSQLite setProperty:forKey:];
-[ACCSQLite rollback];
-[ACCSQLite analyze];
-[ACCSQLite close];
-[ACCSQLite setCorrupt:];
-[ACCSQLite begin];
-[ACCSQLite lastInsertRowID];
-[ACCSQLite vacuum];
-[ACCSQLite dealloc];
-[ACCSQLite corrupt];
-[ACCSQLite setDateFormatter:];
-[ACCSQLite dateFormatter];
-[ACCSQLite end];
-[ACCSQLite dropAllTables];
-[ACCSQLite creationDate];
-[ACCSQLite schemaVersion];
-[ACCSQLite setDelegate:];
-[ACCSQLite schema];
-[ACCSQLite delegate];
-[ACCSQLite remove];
-[ACCSQLite executeSQL:];
-[ACCSQLite setDateProperty:forKey:];
-[ACCSQLite datePropertyForKey:];
-[ACCSQLite isOpen];
-[ACCSQLite path];
-[ACCSQLite removePropertyForKey:];
-[ACCSQLite selectCountFrom:where:bindings:];
-[ACCSQLite statementsBySQL];
-[ACCSQLite synchronousMode];
-[ACCSQLite _createSchemaHash];
-[ACCSQLite _synchronousModeString];
-[ACCSQLite _tableNameForClass:];
-[ACCSQLite allTableNames];
-[ACCSQLite columnNamesForTable:];
-[ACCSQLite dbUserVersion];
-[ACCSQLite deleteFrom:matchingValues:];
-[ACCSQLite deleteFrom:where:bindings:];
-[ACCSQLite hasMigrated];
-[ACCSQLite initWithPath:schema:];
-[ACCSQLite insertOrReplaceInto:values:];
-[ACCSQLite objectClassPrefix];
-[ACCSQLite openCount];
-[ACCSQLite removeAllStatements];
-[ACCSQLite select:from:];
-[ACCSQLite select:from:where:bindings:];
-[ACCSQLite select:from:where:bindings:orderBy:limit:block:];
-[ACCSQLite selectAllFrom:where:bindings:];
-[ACCSQLite selectFrom:where:bindings:limit:];
-[ACCSQLite selectFrom:where:bindings:orderBy:limit:block:];
-[ACCSQLite setObjectClassPrefix:];
-[ACCSQLite setOpenCount:];
-[ACCSQLite setSynchronousMode:];
-[ACCSQLite setTraced:];
-[ACCSQLite statementForSQL:];
-[ACCSQLite traced];
-[ACCSQLite update:set:where:bindings:limit:];
-[ACCSQLite executeSQL:arguments:];
-[ACCSQLite setShouldVacuum:];
-[ACCSQLite shouldVacuum];
-[ACCSQLite _periodicVacuum];
```
