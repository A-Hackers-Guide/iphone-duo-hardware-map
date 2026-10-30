# `ASMInertialOdometryServices`

- Image: [`/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`](../userland/System__Library__PrivateFrameworks__AccessorySensorManagerServices.framework__AccessorySensorManagerServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 18 instance variables, 6 properties, 44 instance methods, 1 class methods

## Instance variables

```
B _invalidateCalled;
B _invalidateDone;
@"NSMutableDictionary" _inertialOdometryAvailabilityMap;
@"NSMutableDictionary" _btAddressToIdentifierMap;
@"NSXPCConnection" _xpcCnx;
@"NSMutableSet" _subscribedInertialOdometryDataPeripheralsByIdentifier;
@"NSMutableSet" _subscribedInertialOdometryAvailabilityPeripheralsByIdentifier;
@"NSMutableSet" _subscribedInertialOdometryDataPeripheralsByBtAddress;
@"NSMutableSet" _subscribedInertialOdometryAvailabilityPeripheralsByBtAddress;
@"NSMutableSet" _pendingDataReestablishmentByIdentifier;
@"NSMutableSet" _pendingDataReestablishmentByBtAddress;
@"NSMutableDictionary" _inertialOdometryConfigsByIdentifier;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@? _inertialOdometryAvailabilityHandler;
@? _inertialOdometryDataReceivedHandler;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_inertialOdometryAvailabilityHandler) inertialOdometryAvailabilityHandler;
@property (T@?,C,N,V_inertialOdometryDataReceivedHandler) inertialOdometryDataReceivedHandler;
```

## Class methods

```
+[ASMInertialOdometryServices supportsSecureCoding];
```

## Instance methods

```
-[ASMInertialOdometryServices clientID];
-[ASMInertialOdometryServices dispatchQueue];
-[ASMInertialOdometryServices _ensureXPCStarted];
-[ASMInertialOdometryServices setClientID:];
-[ASMInertialOdometryServices setInvalidationHandler:];
-[ASMInertialOdometryServices init];
-[ASMInertialOdometryServices interruptionHandler];
-[ASMInertialOdometryServices setDispatchQueue:];
-[ASMInertialOdometryServices invalidate];
-[ASMInertialOdometryServices _interrupted];
-[ASMInertialOdometryServices encodeWithCoder:];
-[ASMInertialOdometryServices setInterruptionHandler:];
-[ASMInertialOdometryServices description];
-[ASMInertialOdometryServices initWithCoder:];
-[ASMInertialOdometryServices invalidationHandler];
-[ASMInertialOdometryServices _invalidated];
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:];
-[ASMInertialOdometryServices _attemptReconnection];
-[ASMInertialOdometryServices _attemptReestablishData];
-[ASMInertialOdometryServices _cleanupFailedAvailabilityReestablishment:];
-[ASMInertialOdometryServices _cleanupFailedDataReestablishment:];
-[ASMInertialOdometryServices _clearInertialOdometryAvailabilityMap];
-[ASMInertialOdometryServices _clearInertialOdometryPeripheralSets];
-[ASMInertialOdometryServices _recordBtAddressToIdentifierMapping:identifier:];
-[ASMInertialOdometryServices _recordInertialOdometryAvailability:forBtAddress:];
-[ASMInertialOdometryServices _recordInertialOdometryAvailability:forPeripheral:];
-[ASMInertialOdometryServices _reestablishAvailability];
-[ASMInertialOdometryServices _reestablishAvailabilityForBtAddress:];
-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:];
-[ASMInertialOdometryServices _reestablishDataForIdentifier:];
-[ASMInertialOdometryServices _reestablishSubscriptions];
-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:btAddress:];
-[ASMInertialOdometryServices inertialOdometryAvailabilityHandler];
-[ASMInertialOdometryServices inertialOdometryDataReceived:];
-[ASMInertialOdometryServices inertialOdometryDataReceivedHandler];
-[ASMInertialOdometryServices isInertialOdometryAvailableForBtAddress:];
-[ASMInertialOdometryServices isInertialOdometryAvailableForPeripheral:];
-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:];
-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:];
-[ASMInertialOdometryServices setInertialOdometryAvailabilityHandler:];
-[ASMInertialOdometryServices setInertialOdometryDataReceivedHandler:];
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:];
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:];
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:];
```
