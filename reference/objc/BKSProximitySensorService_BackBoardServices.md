# `BKSProximitySensorService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSProximitySensorClient_IPC`
- 5 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"BSServiceInitiatingConnection" _connection;
@"BSServiceDispatchQueue" _bsServiceDispatchQueue;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
@"BSCompoundAssertion" _observers;
B _lock_observingDetectionMaskChanges;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSProximitySensorService sharedInstance];
```

## Instance methods

```
-[BKSProximitySensorService _init];
-[BKSProximitySensorService _connectToRemoteServiceIfNeeded];
-[BKSProximitySensorService addObserver:forReason:];
-[BKSProximitySensorService proximityDetectionMaskDidChange:];
```
