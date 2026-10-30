# `ACCSQLiteStatement`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"ACCSQLite" _SQLite;
@"NSString" _SQL;
^{sqlite3_stmt=} _handle;
B _reset;
@"NSMutableArray" _temporaryBoundObjects;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_temporaryBoundObjects) temporaryBoundObjects;
@property (T@"ACCSQLite",R,W,N,V_SQLite) SQLite;
@property (T@"NSString",R,N,V_SQL) SQL;
@property (T^{sqlite3_stmt=},R,N,V_handle) handle;
@property (TB,N,GisReset,V_reset) reset;
```

## Instance methods

```
-[ACCSQLiteStatement columnCount];
-[ACCSQLiteStatement doubleAtIndex:];
-[ACCSQLiteStatement step];
-[ACCSQLiteStatement bindNullAtIndex:];
-[ACCSQLiteStatement SQLite];
-[ACCSQLiteStatement int64AtIndex:];
-[ACCSQLiteStatement intAtIndex:];
-[ACCSQLiteStatement setTemporaryBoundObjects:];
-[ACCSQLiteStatement columnNameAtIndex:];
-[ACCSQLiteStatement textAtIndex:];
-[ACCSQLiteStatement resetAfterStepError];
-[ACCSQLiteStatement setReset:];
-[ACCSQLiteStatement retainedTemporaryBoundObject:];
-[ACCSQLiteStatement reset];
-[ACCSQLiteStatement finalizeStatement];
-[ACCSQLiteStatement isReset];
-[ACCSQLiteStatement bindValue:atIndex:];
-[ACCSQLiteStatement bindValues:];
-[ACCSQLiteStatement blobAtIndex:];
-[ACCSQLiteStatement allObjects];
-[ACCSQLiteStatement handle];
-[ACCSQLiteStatement bindText:atIndex:];
-[ACCSQLiteStatement initWithSQLite:SQL:handle:];
-[ACCSQLiteStatement bindInt64:atIndex:];
-[ACCSQLiteStatement columnTypeAtIndex:];
-[ACCSQLiteStatement allObjectsByColumnName];
-[ACCSQLiteStatement SQL];
-[ACCSQLiteStatement temporaryBoundObjects];
-[ACCSQLiteStatement bindDouble:atIndex:];
-[ACCSQLiteStatement bindBlob:atIndex:];
-[ACCSQLiteStatement bindInt:atIndex:];
-[ACCSQLiteStatement objectAtIndex:];
```
