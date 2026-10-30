# `CAFCarManager`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 9 instance variables, 12 properties, 50 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionLock;
i _carDataToken;
@ _observableCache;
@"CAFCar" _currentCar;
@"CAFBatchUpdate" _invalidatedUpdate;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
@"CARObserverHashTable" _observers;
@"CAFCarManagerConfiguration" _config;
@"_CAFCarDataClientProxy" _connectionProxy;
```

## Properties

```
@property (T{os_unfair_lock_s=I},N,V_connectionLock) connectionLock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_notifyQueue) notifyQueue;
@property (T@"CAFCar",&,N,V_currentCar) currentCar;
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (T@"CAFCarManagerConfiguration",C,N,V_config) config;
@property (Ti,N,V_carDataToken) carDataToken;
@property (T@"_CAFCarDataClientProxy",&,N,V_connectionProxy) connectionProxy;
@property (T@"CAFBatchUpdate",C,N,V_invalidatedUpdate) invalidatedUpdate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFCarManager connectionLock];
-[CAFCarManager initWithConfig:];
-[CAFCarManager config];
-[CAFCarManager setConfig:];
-[CAFCarManager removeObserver:];
-[CAFCarManager init];
-[CAFCarManager dealloc];
-[CAFCarManager notifyQueue];
-[CAFCarManager addObserver:];
-[CAFCarManager invalidate];
-[CAFCarManager description];
-[CAFCarManager setObservers:];
-[CAFCarManager observers];
-[CAFCarManager registerObserver:];
-[CAFCarManager connectionProxy];
-[CAFCarManager setNotifyQueue:];
-[CAFCarManager initWithIdentifier:];
-[CAFCarManager unregisterObserver:];
-[CAFCarManager setConnectionLock:];
-[CAFCarManager setConnectionProxy:];
-[CAFCarManager currentCar];
-[CAFCarManager setInvalidatedUpdate:];
-[CAFCarManager observableCache];
-[CAFCarManager setObservableCache:];
-[CAFCarManager _setupCafdConnectionIfAvailable];
-[CAFCarManager shouldInitializeCharacteristic:];
-[CAFCarManager _closeConnectionWithReason:];
-[CAFCarManager _connectionDidInvalidateForProxy:];
-[CAFCarManager _didReceiveLifecycleNotification:];
-[CAFCarManager _isEntitled];
-[CAFCarManager _locked_closeConnectionWithReason:];
-[CAFCarManager _updateCar];
-[CAFCarManager carDataToken];
-[CAFCarManager enableNotificationForCharacteristic:enable:response:];
-[CAFCarManager enableNotificationForControl:enable:response:];
-[CAFCarManager handleResponse:instanceID:response:];
-[CAFCarManager initWithRegistrationFilePath:];
-[CAFCarManager invalidatedUpdate];
-[CAFCarManager notifyControl:value:];
-[CAFCarManager performGroupedRequest:key:value:withResponse:];
-[CAFCarManager readCharacteristic:response:];
-[CAFCarManager requestControl:value:response:];
-[CAFCarManager setCarDataToken:];
-[CAFCarManager setCurrentCar:];
-[CAFCarManager shouldAllocAccessoryType:];
-[CAFCarManager shouldAllocAccessoryType:serviceConfig:];
-[CAFCarManager shouldAllocAccessoryType:serviceType:characteristicType:];
-[CAFCarManager shouldAllocAccessoryType:serviceType:controlType:];
-[CAFCarManager shouldInitializeControl:];
-[CAFCarManager writeCharacteristic:value:response:];
```
