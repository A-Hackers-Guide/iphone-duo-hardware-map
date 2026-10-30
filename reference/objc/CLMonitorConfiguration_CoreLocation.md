# `CLMonitorConfiguration`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLIdentifiableClientProtocol`
- 11 instance variables, 15 properties, 25 instance methods, 3 class methods

## Instance variables

```
@"CLDispatchSilo" _silo;
@? _vendingHandler;
@? _eventHandler;
B _useMonitorQueue;
@"NSString" identityToken;
@"NSData" storageToken;
@"CLLocationManager" manager;
@? weakClient;
@"NSString" _name;
@"NSString" _path;
@"NSString" _onBehalfOfBundleIdentifer;
```

## Properties

```
@property (TB,N,V_useMonitorQueue) useMonitorQueue;
@property (T@"NSString",R,C,N,V_path) path;
@property (T@?,C,N) vendingHandler;
@property (T@"NSString",R,V_onBehalfOfBundleIdentifer) onBehalfOfBundleIdentifer;
@property (T@"NSString",R,V_name) name;
@property (T@"NSObject<OS_dispatch_queue>",R) queue;
@property (T@?,R,N) eventHandler;
@property (T@"NSString",&,N,VidentityToken) identityToken;
@property (T@"NSData",&,N,VstorageToken) storageToken;
@property (T@"CLLocationManager",&,N,Vmanager) manager;
@property (T@?,W,N,VweakClient) weakClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CLMonitorConfiguration _configWithMonitorName:];
+[CLMonitorConfiguration configWithMonitorName:onBehalfOfBundleIdentifier:queue:eventHandler:];
+[CLMonitorConfiguration configWithMonitorName:queue:eventHandler:];
```

## Instance methods

```
-[CLMonitorConfiguration eventHandler];
-[CLMonitorConfiguration setEventHandler:];
-[CLMonitorConfiguration storageToken];
-[CLMonitorConfiguration vendMonitorWithIdentityAndAuthorizationAttributes:];
-[CLMonitorConfiguration setManager:];
-[CLMonitorConfiguration initWithName:path:onQueue:eventHandler:useMonitorQueueForVendingMonitor:vendingHandler:];
-[CLMonitorConfiguration dealloc];
-[CLMonitorConfiguration setStorageToken:];
-[CLMonitorConfiguration setWeakClient:];
-[CLMonitorConfiguration setVendingHandler:];
-[CLMonitorConfiguration vendingHandler];
-[CLMonitorConfiguration queue];
-[CLMonitorConfiguration manager];
-[CLMonitorConfiguration identityToken];
-[CLMonitorConfiguration setUseMonitorQueue:];
-[CLMonitorConfiguration setIdentityToken:];
-[CLMonitorConfiguration hash];
-[CLMonitorConfiguration weakClient];
-[CLMonitorConfiguration initWithName:path:onQueue:eventHandler:];
-[CLMonitorConfiguration onBehalfOfBundleIdentifer];
-[CLMonitorConfiguration updateIdentityToken:withStorageToken:];
-[CLMonitorConfiguration initWithName:path:onSilo:eventHandler:useMonitorQueueForVendingMonitor:vendingHandler:];
-[CLMonitorConfiguration name];
-[CLMonitorConfiguration useMonitorQueue];
-[CLMonitorConfiguration path];
```
