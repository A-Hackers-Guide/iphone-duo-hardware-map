# `CWFSensingAutoDataCollector`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" __serviceObjects;
@"NSObject<OS_dispatch_queue>" __serviceQueue;
@"HMAccessory" __currentAccessory;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V__serviceObjects) _serviceObjects;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__serviceQueue) _serviceQueue;
@property (T@"HMAccessory",&,N,V__currentAccessory) _currentAccessory;
```

## Class methods

```
+[CWFSensingAutoDataCollector sharedCWFSensingAutoDataCollectorInstanceWith:];
```

## Instance methods

```
-[CWFSensingAutoDataCollector _serviceQueue];
-[CWFSensingAutoDataCollector set_serviceQueue:];
-[CWFSensingAutoDataCollector initWithHomes:];
-[CWFSensingAutoDataCollector _serviceObjects];
-[CWFSensingAutoDataCollector _currentAccessory];
-[CWFSensingAutoDataCollector cleanUpOutOfScopeAccessory];
-[CWFSensingAutoDataCollector currentAccessoryInfo:];
-[CWFSensingAutoDataCollector registerForAccessoriesInRoomWithDelegate:];
-[CWFSensingAutoDataCollector set_currentAccessory:];
-[CWFSensingAutoDataCollector set_serviceObjects:];
-[CWFSensingAutoDataCollector updateRegisteredServiceWithDelegate:];
```
