# `_NSHTTPAlternativeServicesStorageSqlite`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _path;
@"NSObject<OS_dispatch_queue>" _workQueue;
B _garbageCollectionDispatched;
B _dbInitialized;
B _isMemoryStore;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
@"NSMutableSet" memoryEntries;
@"NSMutableSet" clearEntries;
^{sqlite3=} dbConnection;
^{sqlite3_stmt=} selectAllEntriesStmt;
^{sqlite3_stmt=} selectAllValidEntriesStmt;
^{sqlite3_stmt=} selectEntriesStmt;
^{sqlite3_stmt=} insertEntriesStmt;
^{sqlite3_stmt=} deleteWithTimeStmt;
^{sqlite3_stmt=} deleteWithHostAndPortStmt;
^{sqlite3_stmt=} deleteWithHostPartitionPortTypeStmt;
^{sqlite3_stmt=} deleteWithRegistrableDomainStmt;
```

## Instance methods

```
-[_NSHTTPAlternativeServicesStorageSqlite dealloc];
```
