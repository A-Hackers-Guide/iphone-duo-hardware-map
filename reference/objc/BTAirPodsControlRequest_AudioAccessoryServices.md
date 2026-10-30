# `BTAirPodsControlRequest`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _enabled;
@"BTAirPodsControlServiceClient" _client;
@? _getHandler;
@? _setHandler;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
```

## Properties

```
@property (T@"BTAirPodsControlServiceClient",&,N,V_client) client;
@property (TB,N,V_enabled) enabled;
@property (T@?,C,N,V_getHandler) getHandler;
@property (T@?,C,N,V_setHandler) setHandler;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_timeoutTimer) timeoutTimer;
```

## Instance methods

```
-[BTAirPodsControlRequest enabled];
-[BTAirPodsControlRequest setClient:];
-[BTAirPodsControlRequest setEnabled:];
-[BTAirPodsControlRequest setTimeoutTimer:];
-[BTAirPodsControlRequest timeoutTimer];
-[BTAirPodsControlRequest client];
-[BTAirPodsControlRequest getHandler];
-[BTAirPodsControlRequest setGetHandler:];
-[BTAirPodsControlRequest setHandler];
-[BTAirPodsControlRequest setSetHandler:];
```
