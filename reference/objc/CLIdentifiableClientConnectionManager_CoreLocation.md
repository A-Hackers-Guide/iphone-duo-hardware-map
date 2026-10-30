# `CLIdentifiableClientConnectionManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLIdentifiableClientProtocol`
- 13 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"CLDispatchSilo" _silo;
^v _locationdConnection;
@"NSString" _startMessageName;
@"NSMutableDictionary" _startMessagePayload;
B _shouldBeRunning;
B _started;
@? _responseHandler;
d _lastHistoricalLocationTimestamp;
@? _connectionFactory;
@"NSString" identityToken;
@"NSData" storageToken;
@"CLLocationManager" manager;
@? weakClient;
```

## Properties

```
@property (TB,V_shouldBeRunning) shouldBeRunning;
@property (TB,V_started) started;
@property (T@"NSString",&,N,VidentityToken) identityToken;
@property (T@"NSData",&,N,VstorageToken) storageToken;
@property (T@"CLLocationManager",&,N,Vmanager) manager;
@property (T@?,W,N,VweakClient) weakClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CLIdentifiableClientConnectionManager tearDown];
-[CLIdentifiableClientConnectionManager createConnection];
-[CLIdentifiableClientConnectionManager pause];
-[CLIdentifiableClientConnectionManager setStarted:];
-[CLIdentifiableClientConnectionManager storageToken];
-[CLIdentifiableClientConnectionManager _start];
-[CLIdentifiableClientConnectionManager setManager:];
-[CLIdentifiableClientConnectionManager dealloc];
-[CLIdentifiableClientConnectionManager setStorageToken:];
-[CLIdentifiableClientConnectionManager setWeakClient:];
-[CLIdentifiableClientConnectionManager manageConnection];
-[CLIdentifiableClientConnectionManager started];
-[CLIdentifiableClientConnectionManager _pauseLocationUpdater];
-[CLIdentifiableClientConnectionManager destroyConnection];
-[CLIdentifiableClientConnectionManager manager];
-[CLIdentifiableClientConnectionManager initWithStartMessageName:startMessagePayload:locationManager:responseHandler:];
-[CLIdentifiableClientConnectionManager handleResponseMessage:];
-[CLIdentifiableClientConnectionManager setShouldBeRunning:];
-[CLIdentifiableClientConnectionManager initWithStartMessageName:startMessagePayload:responseHandler:];
-[CLIdentifiableClientConnectionManager identityToken];
-[CLIdentifiableClientConnectionManager _resumeLocationUpdater];
-[CLIdentifiableClientConnectionManager setIdentityToken:];
-[CLIdentifiableClientConnectionManager weakClient];
-[CLIdentifiableClientConnectionManager initWithSilo:locationManager:startMessageName:startMessagePayload:responseHandler:];
-[CLIdentifiableClientConnectionManager _setConnectionFactory:];
-[CLIdentifiableClientConnectionManager updateLastHistoricalLocationTimestamp:];
-[CLIdentifiableClientConnectionManager updateIdentityToken:withStorageToken:];
-[CLIdentifiableClientConnectionManager shouldBeRunning];
-[CLIdentifiableClientConnectionManager resume];
```
