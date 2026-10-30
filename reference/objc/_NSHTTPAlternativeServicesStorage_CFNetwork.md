# `_NSHTTPAlternativeServicesStorage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _inMemory;
@ _underlyingStorage;
@"_NSHTTPAlternativeServicesStorageSqlite" _oldStorage;
@"NSURL" _path;
```

## Properties

```
@property (T@"NSURL",R,N,V_path) path;
@property (TB) canSuspendLocked;
@property (T@,R,V_underlyingStorage) underlyingStorage;
```

## Class methods

```
+[_NSHTTPAlternativeServicesStorage sharedPersistentStore];
```

## Instance methods

```
-[_NSHTTPAlternativeServicesStorage entries];
-[_NSHTTPAlternativeServicesStorage HTTPServiceEntriesWithFilter:];
-[_NSHTTPAlternativeServicesStorage setCanSuspendLocked:];
-[_NSHTTPAlternativeServicesStorage initPersistentStoreWithURL:];
-[_NSHTTPAlternativeServicesStorage removeHTTPAlternativeServiceEntriesWithHost:partition:port:serviceType:];
-[_NSHTTPAlternativeServicesStorage canSuspendLocked];
-[_NSHTTPAlternativeServicesStorage removeHTTPAlternativeServiceEntriesCreatedAfterDate:];
-[_NSHTTPAlternativeServicesStorage underlyingStorage];
-[_NSHTTPAlternativeServicesStorage initInMemoryStore];
-[_NSHTTPAlternativeServicesStorage removeHTTPAlternativeServiceEntriesWithRegistrableDomain:];
-[_NSHTTPAlternativeServicesStorage storeHTTPServiceEntry:];
-[_NSHTTPAlternativeServicesStorage removeHTTPAlternativeServiceEntriesWithHost:port:];
-[_NSHTTPAlternativeServicesStorage path];
```
