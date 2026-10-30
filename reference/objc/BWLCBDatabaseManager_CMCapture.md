# `BWLCBDatabaseManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _lcbDatabaseQueue;
@"NSMutableDictionary" _lcbDatabaseByPortType;
B _databasesWereUpdated;
@"NSString" _databasePathFolder;
@"NSString" _databasePathPrefix;
* _containerSandboxToken;
@"<BWLCBDatabaseManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSDictionary",R,N) lcbDatabaseByPortType;
@property (T@"<BWLCBDatabaseManagerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[BWLCBDatabaseManager initialize];
+[BWLCBDatabaseManager sharedManager];
```

## Instance methods

```
-[BWLCBDatabaseManager init];
-[BWLCBDatabaseManager dealloc];
-[BWLCBDatabaseManager setDelegate:];
-[BWLCBDatabaseManager delegate];
-[BWLCBDatabaseManager databaseForPortType:];
-[BWLCBDatabaseManager lcbDatabaseByPortType];
-[BWLCBDatabaseManager loadDatabasesForSensorConfigurationsByPortType:];
-[BWLCBDatabaseManager saveDatabasesIfNeeded];
-[BWLCBDatabaseManager updateDatabase:forPortType:];
```
