# `CLBackgroundActivitySession`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLIdentifiableClientProtocol`
- 8 instance variables, 9 properties, 21 instance methods, 5 class methods

## Instance variables

```
@"CLDispatchSilo" _silo;
^v _locationdConnection;
@? _clientCallback;
B _shouldBeRunning;
@"NSString" identityToken;
@"NSData" storageToken;
@"CLLocationManager" manager;
@? weakClient;
```

## Properties

```
@property (TB,V_shouldBeRunning) shouldBeRunning;
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
+[CLBackgroundActivitySession backgroundActivitySession];
+[CLBackgroundActivitySession backgroundActivitySessionWithLocationManager:];
+[CLBackgroundActivitySession backgroundActivitySessionWithQueue:handler:];
+[CLBackgroundActivitySession sessionWithLocationManager:queue:handler:];
+[CLBackgroundActivitySession sessionWithLocationManager:requestPrivilege:queue:handler:];
```

## Instance methods

```
-[CLBackgroundActivitySession tearDown];
-[CLBackgroundActivitySession createConnection];
-[CLBackgroundActivitySession handleMessage:];
-[CLBackgroundActivitySession storageToken];
-[CLBackgroundActivitySession setManager:];
-[CLBackgroundActivitySession dealloc];
-[CLBackgroundActivitySession setStorageToken:];
-[CLBackgroundActivitySession setWeakClient:];
-[CLBackgroundActivitySession manageConnection];
-[CLBackgroundActivitySession setHandler:];
-[CLBackgroundActivitySession destroyConnection];
-[CLBackgroundActivitySession manager];
-[CLBackgroundActivitySession setShouldBeRunning:];
-[CLBackgroundActivitySession identityToken];
-[CLBackgroundActivitySession invalidate];
-[CLBackgroundActivitySession setIdentityToken:];
-[CLBackgroundActivitySession weakClient];
-[CLBackgroundActivitySession updateIdentityToken:withStorageToken:];
-[CLBackgroundActivitySession shouldBeRunning];
-[CLBackgroundActivitySession handleMessageDiagnostics:];
-[CLBackgroundActivitySession initWithLocationManager:queue:handler:];
```
