# `CLServiceSessionInternal`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLIdentifiableClientProtocol`
- 10 instance variables, 10 properties, 22 instance methods, 4 class methods

## Instance variables

```
@"CLDispatchSilo" _silo;
^v _locationdConnection;
@? _connectionFactory;
@? _clientCallback;
B _isValid;
i _sessionType;
@"NSString" identityToken;
@"NSData" storageToken;
@"CLLocationManager" manager;
@? weakClient;
```

## Properties

```
@property (TB,V_isValid) isValid;
@property (Ti,R,N,V_sessionType) sessionType;
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
+[CLServiceSessionInternal alwaysSessionWithLocationManager:queue:handler:];
+[CLServiceSessionInternal passiveSessionWithLocationManager:queue:handler:];
+[CLServiceSessionInternal sessionWithLocationManager:type:queue:handler:];
+[CLServiceSessionInternal whenInUseSessionWithLocationManager:queue:handler:];
```

## Instance methods

```
-[CLServiceSessionInternal tearDown];
-[CLServiceSessionInternal createConnection];
-[CLServiceSessionInternal handleMessage:];
-[CLServiceSessionInternal setIsValid:];
-[CLServiceSessionInternal storageToken];
-[CLServiceSessionInternal setManager:];
-[CLServiceSessionInternal dealloc];
-[CLServiceSessionInternal setStorageToken:];
-[CLServiceSessionInternal setWeakClient:];
-[CLServiceSessionInternal manageConnection];
-[CLServiceSessionInternal destroyConnection];
-[CLServiceSessionInternal manager];
-[CLServiceSessionInternal identityToken];
-[CLServiceSessionInternal invalidate];
-[CLServiceSessionInternal sessionType];
-[CLServiceSessionInternal setIdentityToken:];
-[CLServiceSessionInternal isValid];
-[CLServiceSessionInternal weakClient];
-[CLServiceSessionInternal _setConnectionFactory:];
-[CLServiceSessionInternal updateIdentityToken:withStorageToken:];
-[CLServiceSessionInternal handleMessageDiagnostics:];
-[CLServiceSessionInternal initWithLocationManager:serviceSessionType:queue:handler:];
```
