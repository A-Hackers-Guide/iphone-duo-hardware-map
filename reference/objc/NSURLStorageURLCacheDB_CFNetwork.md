# `NSURLStorageURLCacheDB`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
^{sqlite3=} _dbReadConnection;
^{sqlite3=} _dbWriteConnection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _dbReadConnectionLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _dbWriteConnectionLock;
^{sqlite3_stmt=} _sqlUpdateReceiverDataStmt;
^{sqlite3_stmt=} _sqlInsertStmtResponse;
^{sqlite3_stmt=} _sqlInsertStmtBlobData;
^{sqlite3_stmt=} _sqlInsertStmtReceiverData;
^{sqlite3_stmt=} _sqlUpdateResponseStmt;
^{sqlite3_stmt=} _sqlUpdateBlobDataStmt;
^{sqlite3_stmt=} _sqlSelectStmt;
^{sqlite3_stmt=} _sqlSelectEntry_idAndRecevierDataForKeyStmt;
^{sqlite3_stmt=} _sqlDeleteStmtResponse;
^{sqlite3_stmt=} _sqlDeleteStmtBlobData;
^{sqlite3_stmt=} _sqlDeleteStmtReceiverData;
@"NSMutableArray" _entryIDsToDelete;
Q _writeCount;
B _updatingSchema;
B _isDBOpen;
@"NSString" _dbPathDirectory;
@"NSString" _dbPathFile;
q _maxDBSize;
Q _currentFSBackedUsage;
Q _currentSQLiteDBUsage;
Q _currentTotalPersistentCacheUsage;
q _minSizeForFileSystemBackedCacheItem;
```

## Instance methods

```
-[NSURLStorageURLCacheDB dealloc];
```
