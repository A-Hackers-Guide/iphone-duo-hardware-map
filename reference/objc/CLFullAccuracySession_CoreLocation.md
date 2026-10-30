# `CLFullAccuracySession`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLIdentifiableClientProtocol`
- 9 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"CLDispatchSilo" _silo;
^v _locationdConnection;
@? _clientCallback;
B _isValid;
@"NSData" storageToken;
@"NSString" identityToken;
@"CLLocationManager" manager;
@? weakClient;
@"NSString" _purposeKey;
```

## Properties

```
@property (TB,V_isValid) isValid;
@property (T@"NSString",R,C,N,V_purposeKey) purposeKey;
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
+[CLFullAccuracySession fullAccuracySessionWithLocationManager:purposeKey:queue:handler:];
```

## Instance methods

```
-[CLFullAccuracySession tearDown];
-[CLFullAccuracySession createConnection];
-[CLFullAccuracySession handleMessage:];
-[CLFullAccuracySession setIsValid:];
-[CLFullAccuracySession storageToken];
-[CLFullAccuracySession setManager:];
-[CLFullAccuracySession dealloc];
-[CLFullAccuracySession setStorageToken:];
-[CLFullAccuracySession setWeakClient:];
-[CLFullAccuracySession manageConnection];
-[CLFullAccuracySession destroyConnection];
-[CLFullAccuracySession manager];
-[CLFullAccuracySession identityToken];
-[CLFullAccuracySession invalidate];
-[CLFullAccuracySession setIdentityToken:];
-[CLFullAccuracySession isValid];
-[CLFullAccuracySession weakClient];
-[CLFullAccuracySession updateIdentityToken:withStorageToken:];
-[CLFullAccuracySession handleMessageDiagnostics:];
-[CLFullAccuracySession initWithLocationManager:purposeKey:queue:handler:];
-[CLFullAccuracySession purposeKey];
```
