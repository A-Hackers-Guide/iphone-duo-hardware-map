# `PPSCoreStorage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"PPSSQLStorage" _sqlStorage;
@"PPSFlatStorage" _flatStorage;
@"NSDictionary" _storageMap;
```

## Properties

```
@property (T@"PPSSQLStorage",&,V_sqlStorage) sqlStorage;
@property (T@"PPSFlatStorage",&,V_flatStorage) flatStorage;
@property (T@"NSDictionary",&,V_storageMap) storageMap;
```

## Class methods

```
+[PPSCoreStorage sharedFlatStorage];
+[PPSCoreStorage sharedSQLStorage];
```

## Instance methods

```
-[PPSCoreStorage init];
-[PPSCoreStorage startStorage];
-[PPSCoreStorage setupStorage];
-[PPSCoreStorage setupMetadataStorage];
-[PPSCoreStorage setFlatStorage:];
-[PPSCoreStorage startAllStorage];
-[PPSCoreStorage flatStorage];
-[PPSCoreStorage mergePreUnlockDBFiles];
-[PPSCoreStorage setSqlStorage:];
-[PPSCoreStorage setStorageMap:];
-[PPSCoreStorage setupEntryObjects];
-[PPSCoreStorage sqlStorage];
-[PPSCoreStorage storageClassForKey:];
-[PPSCoreStorage storageClassForType:];
-[PPSCoreStorage storageMap];
```
