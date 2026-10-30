# `CLLocationUpdater`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 16 instance methods, 11 class methods

## Instance variables

```
@"CLDispatchSilo" _silo;
@? _clientCallback;
@"NSString" _messageName;
@"NSMutableDictionary" _mutableMsgDictionary;
@"CLIdentifiableClientConnectionManager" _connectionManager;
```

## Properties

```
@property (T@"CLIdentifiableClientConnectionManager",&,N,V_connectionManager) connectionManager;
```

## Class methods

```
+[CLLocationUpdater _liveUpdaterWithQueue:handler:];
+[CLLocationUpdater _liveUpdaterWithConfiguration:queue:handler:];
+[CLLocationUpdater liveUpdaterWithConfiguration:queue:handler:];
+[CLLocationUpdater liveUpdaterWithQueue:handler:];
+[CLLocationUpdater historicalUpdaterWithDateInterval:sampleCount:queue:handler:];
+[CLLocationUpdater _historicalUpdaterWithDateInterval:sampleCount:queue:handler:];
+[CLLocationUpdater _historicalUpdaterWithCenter:radius:dateInterval:sampleCount:queue:handler:];
+[CLLocationUpdater historicalUpdaterWithCenter:radius:dateInterval:sampleCount:queue:handler:];
+[CLLocationUpdater historicalUpdaterWithCenter:radius:dateInterval:sampleCount:locationManager:queue:handler:];
+[CLLocationUpdater historicalUpdaterWithDateInterval:sampleCount:locationManager:queue:handler:];
+[CLLocationUpdater liveUpdaterWithConfiguration:locationManager:queue:handler:];
```

## Instance methods

```
-[CLLocationUpdater tearDown];
-[CLLocationUpdater pause];
-[CLLocationUpdater setConnectionManager:];
-[CLLocationUpdater dealloc];
-[CLLocationUpdater setHandler:];
-[CLLocationUpdater invalidate];
-[CLLocationUpdater connectionManager];
-[CLLocationUpdater resume];
-[CLLocationUpdater handleMessageDiagnostics:];
-[CLLocationUpdater handleMessageHistoricalLocations:];
-[CLLocationUpdater handleMessageHistoricalLocationsFinished:];
-[CLLocationUpdater handleMessageLocation:];
-[CLLocationUpdater handleMessageLocationUnavailable:];
-[CLLocationUpdater handleMessageWithName:payload:];
-[CLLocationUpdater initWithRegistrationMessageName:messagePayload:locationManager:queue:handler:];
-[CLLocationUpdater initWithRegistrationMessageName:messagePayload:locationManager:queue:handler:connectionManager:];
```
