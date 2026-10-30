# `_CAFCarDataClientProxy`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCarDataClient`, `BSInvalidatable`
- 7 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _invalidatedLock;
@"NSUUID" _uniqueIdentifier;
@"NSXPCConnection" _connection;
@"CAFCarManager" _carManager;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"CAFCarConfiguration" _currentCarConfig;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (TB,R,N,V_invalidated) invalidated;
@property (T{os_unfair_lock_s=I},N,V_invalidatedLock) invalidatedLock;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"<CAFCarDataService>",R,N) remoteProxy;
@property (T@"CAFCarManager",W,N,V_carManager) carManager;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"CAFCarConfiguration",&,N,V_currentCarConfig) currentCarConfig;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_CAFCarDataClientProxy setWorkQueue:];
-[_CAFCarDataClientProxy invalidated];
-[_CAFCarDataClientProxy workQueue];
-[_CAFCarDataClientProxy uniqueIdentifier];
-[_CAFCarDataClientProxy invalidate];
-[_CAFCarDataClientProxy activate];
-[_CAFCarDataClientProxy connection];
-[_CAFCarDataClientProxy setConnection:];
-[_CAFCarDataClientProxy remoteProxy];
-[_CAFCarDataClientProxy carManager];
-[_CAFCarDataClientProxy setCarManager:];
-[_CAFCarDataClientProxy invalidatedLock];
-[_CAFCarDataClientProxy currentCarConfig];
-[_CAFCarDataClientProxy didNotifyPluginID:instanceID:value:];
-[_CAFCarDataClientProxy didRequestPluginID:instanceID:value:withResponse:];
-[_CAFCarDataClientProxy didUpdateAttributes:];
-[_CAFCarDataClientProxy didUpdateConfig:];
-[_CAFCarDataClientProxy didUpdateCurrentCarConfig:];
-[_CAFCarDataClientProxy didUpdatePluginID:values:];
-[_CAFCarDataClientProxy initWithCarManager:];
-[_CAFCarDataClientProxy setCurrentCarConfig:];
-[_CAFCarDataClientProxy setInvalidatedLock:];
```
