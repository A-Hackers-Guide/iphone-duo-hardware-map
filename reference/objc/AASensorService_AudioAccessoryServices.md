# `AASensorService`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `AAServicesXPCClientInterface`
- 20 instance variables, 9 properties, 39 instance methods, 1 class methods

## Instance variables

```
@"AAController" _aaController;
B _activateCalled;
@? _activateCompletion;
I _availableSensors;
B _invalidateCalled;
B _invalidateDone;
@"NSMutableDictionary" _ovadDataDict;
@"NSMutableDictionary" _requestedSensorRates;
I _subscribedSensors;
@? _subscriptionErrorHandler;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSString" _btAddress;
d _deviceDiscoveryTimeout;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@? _sensorAvailabilityUpdatedHandler;
@? _sensorDataInfoUpdatedHandler;
d _subscriptionTimeout;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSString",C,N,V_btAddress) btAddress;
@property (Td,N,V_deviceDiscoveryTimeout) deviceDiscoveryTimeout;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_sensorAvailabilityUpdatedHandler) sensorAvailabilityUpdatedHandler;
@property (T@?,C,N,V_sensorDataInfoUpdatedHandler) sensorDataInfoUpdatedHandler;
@property (Td,N,V_subscriptionTimeout) subscriptionTimeout;
```

## Class methods

```
+[AASensorService supportsSecureCoding];
```

## Instance methods

```
-[AASensorService clientID];
-[AASensorService dispatchQueue];
-[AASensorService _ensureXPCStarted];
-[AASensorService activateWithCompletion:];
-[AASensorService setClientID:];
-[AASensorService setInvalidationHandler:];
-[AASensorService init];
-[AASensorService unsubscribeAll];
-[AASensorService _activateXPC:reactivate:];
-[AASensorService interruptionHandler];
-[AASensorService setDispatchQueue:];
-[AASensorService invalidate];
-[AASensorService _activate:];
-[AASensorService _interrupted];
-[AASensorService encodeWithCoder:];
-[AASensorService activate];
-[AASensorService setBtAddress:];
-[AASensorService setInterruptionHandler:];
-[AASensorService _reportError:];
-[AASensorService description];
-[AASensorService initWithCoder:];
-[AASensorService invalidationHandler];
-[AASensorService _invalidated];
-[AASensorService btAddress];
-[AASensorService sensorServiceReportSensorInfo:];
-[AASensorService unsubscribeWithSensorDataFlags:];
-[AASensorService _broadcastAACPAvailabilities];
-[AASensorService _sendPTEventToAccessory:value:completion:];
-[AASensorService deviceDiscoveryTimeout];
-[AASensorService sendPTEventToAccessory:value:completion:];
-[AASensorService sensorAvailabilityUpdatedHandler];
-[AASensorService sensorDataInfoUpdatedHandler];
-[AASensorService setDeviceDiscoveryTimeout:];
-[AASensorService setSensorAvailabilityUpdatedHandler:];
-[AASensorService setSensorDataInfoUpdatedHandler:];
-[AASensorService setSubscriptionTimeout:];
-[AASensorService subscribeWithSensorDataFlags:completion:];
-[AASensorService subscribeWithSensorDataFlags:rate:completion:];
-[AASensorService subscriptionTimeout];
```
