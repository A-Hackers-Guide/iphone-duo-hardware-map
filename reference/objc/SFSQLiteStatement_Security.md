# `SFSQLiteStatement`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFSQLiteRow`
- 6 instance variables, 10 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"SFSQLite" _SQLite;
@"NSString" _SQL;
^{sqlite3_stmt=} _handle;
B _reset;
@"NSMutableArray" _temporaryBoundObjects;
@"NSDictionary" _indexesByColumnName;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_temporaryBoundObjects) temporaryBoundObjects;
@property (T@"NSDictionary",&,N,V_indexesByColumnName) indexesByColumnName;
@property (T@"SFSQLite",R,W,N,V_SQLite) SQLite;
@property (T@"NSString",R,N,V_SQL) SQL;
@property (T^{sqlite3_stmt=},R,N,V_handle) handle;
@property (TB,N,GisReset,V_reset) reset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SFSQLiteStatement columnCount];
-[SFSQLiteStatement doubleAtIndex:];
-[SFSQLiteStatement step];
-[SFSQLiteStatement bindNullAtIndex:];
-[SFSQLiteStatement enumerateColumnsUsingBlock:];
-[SFSQLiteStatement SQLite];
-[SFSQLiteStatement int64AtIndex:];
-[SFSQLiteStatement setIndexesByColumnName:];
-[SFSQLiteStatement intAtIndex:];
-[SFSQLiteStatement setTemporaryBoundObjects:];
-[SFSQLiteStatement columnNameAtIndex:];
-[SFSQLiteStatement textAtIndex:];
-[SFSQLiteStatement resetAfterStepError];
-[SFSQLiteStatement setReset:];
-[SFSQLiteStatement retainedTemporaryBoundObject:];
-[SFSQLiteStatement reset];
-[SFSQLiteStatement finalizeStatement];
-[SFSQLiteStatement isReset];
-[SFSQLiteStatement bindValue:atIndex:];
-[SFSQLiteStatement bindValues:];
-[SFSQLiteStatement blobAtIndex:];
-[SFSQLiteStatement allObjects];
-[SFSQLiteStatement indexesByColumnName];
-[SFSQLiteStatement handle];
-[SFSQLiteStatement bindText:atIndex:];
-[SFSQLiteStatement initWithSQLite:SQL:handle:];
-[SFSQLiteStatement bindInt64:atIndex:];
-[SFSQLiteStatement columnTypeAtIndex:];
-[SFSQLiteStatement allObjectsByColumnName];
-[SFSQLiteStatement SQL];
-[SFSQLiteStatement temporaryBoundObjects];
-[SFSQLiteStatement bindDouble:atIndex:];
-[SFSQLiteStatement bindBlob:atIndex:];
-[SFSQLiteStatement bindInt:atIndex:];
-[SFSQLiteStatement indexForColumnName:];
-[SFSQLiteStatement objectAtIndex:];
```
