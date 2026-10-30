# `CWFHomeManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HMHomeManagerDelegate`, `HMHomeDelegate`
- 8 instance variables, 12 properties, 25 instance methods, 1 class methods

## Instance variables

```
B __isHomeInformationAvailable;
@"HMHomeManager" __homeManager;
@"NSMutableDictionary" __serviceObjects;
@"NSObject<OS_dispatch_queue>" __serviceQueue;
@"<NSObject>" __activeAssertion;
@"HMFLocationAuthorization" __homeLocationAuthorization;
@"CWFSensingAutoDataCollector" __autoDataColletor;
@"<CWFHomeManagerDelegate>" __delegate;
```

## Properties

```
@property (T@"HMHomeManager",&,N,V__homeManager) _homeManager;
@property (TB,N,V__isHomeInformationAvailable) _isHomeInformationAvailable;
@property (T@"NSMutableDictionary",&,N,V__serviceObjects) _serviceObjects;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__serviceQueue) _serviceQueue;
@property (T@"<NSObject>",&,N,V__activeAssertion) _activeAssertion;
@property (T@"HMFLocationAuthorization",&,N,V__homeLocationAuthorization) _homeLocationAuthorization;
@property (T@"CWFSensingAutoDataCollector",&,N,V__autoDataColletor) _autoDataColletor;
@property (T@"<CWFHomeManagerDelegate>",&,N,V__delegate) _delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CWFHomeManager cwfHomeManagerWithDelegate:];
```

## Instance methods

```
-[CWFHomeManager initWithDelegate:];
-[CWFHomeManager dealloc];
-[CWFHomeManager homeManagerDidUpdateHomes:];
-[CWFHomeManager _delegate];
-[CWFHomeManager set_delegate:];
-[CWFHomeManager _serviceQueue];
-[CWFHomeManager set_serviceQueue:];
-[CWFHomeManager _serviceObjects];
-[CWFHomeManager set_isHomeInformationAvailable:];
-[CWFHomeManager registerForAccessoryStateChange:withParams:forCWFHMServiceType:];
-[CWFHomeManager _activeAssertion];
-[CWFHomeManager _autoDataColletor];
-[CWFHomeManager _homeLocationAuthorization];
-[CWFHomeManager _homeManager];
-[CWFHomeManager _isHomeInformationAvailable];
-[CWFHomeManager createServiceObjectFor:withParams:andAccessory:];
-[CWFHomeManager getServiceEvents];
-[CWFHomeManager getServiceTypeStringFor:];
-[CWFHomeManager initHomeManagerInstance];
-[CWFHomeManager removeObjectForServieType:withUUID:];
-[CWFHomeManager set_activeAssertion:];
-[CWFHomeManager set_autoDataColletor:];
-[CWFHomeManager set_homeLocationAuthorization:];
-[CWFHomeManager set_homeManager:];
-[CWFHomeManager set_serviceObjects:];
```
