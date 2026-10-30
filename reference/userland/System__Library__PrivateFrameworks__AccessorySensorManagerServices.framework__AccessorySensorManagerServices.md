# `/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`

iOS 27.2 dyld shared cache image. Version `20.27.0.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/AccessorySensorManagerDefines_Private.framework/AccessorySensorManagerDefines_Private`
- `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`
- `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 5 classes, 4 protocols, 117 methods, 15 properties

### Class pages

Every class and protocol, with its methods: [`ASMCompanionServices`](../objc/ASMCompanionServices_AccessorySensorManagerServices.md), [`ASMInertialOdometryServices`](../objc/ASMInertialOdometryServices_AccessorySensorManagerServices.md), [`ASMPeripheralConfig`](../objc/ASMPeripheralConfig_AccessorySensorManagerServices.md), [`ASMPeripheralControlServices`](../objc/ASMPeripheralControlServices_AccessorySensorManagerServices.md), [`ASMPeripheralInertialOdometryConfig`](../objc/ASMPeripheralInertialOdometryConfig_AccessorySensorManagerServices.md), [`ASMServicesXPCClientInterface`](../objc/ASMServicesXPCClientInterface_AccessorySensorManagerServices.protocol.md), [`ASMServicesXPCDaemonInterface`](../objc/ASMServicesXPCDaemonInterface_AccessorySensorManagerServices.protocol.md), [`NSCoding`](../objc/NSCoding_AccessorySensorManagerServices.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_AccessorySensorManagerServices.protocol.md)

### Classes

`ASMCompanionServices`, `ASMInertialOdometryServices`, `ASMPeripheralConfig`, `ASMPeripheralControlServices`, `ASMPeripheralInertialOdometryConfig`

### Protocols

`ASMServicesXPCClientInterface`, `ASMServicesXPCDaemonInterface`, `NSCoding`, `NSSecureCoding`

### Properties

```
@property (class, TB,R) supportsSecureCoding;
@property (TI,N,V_clientID) clientID;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (TI,N,V_clientID) clientID;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_inertialOdometryAvailabilityHandler) inertialOdometryAvailabilityHandler;
@property (T@?,C,N,V_inertialOdometryDataReceivedHandler) inertialOdometryDataReceivedHandler;
@property (TI,N,V_clientID) clientID;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Strings (144)

```
v16@?0@\"NSError\"8
Successfully resubscribed to inertial odometry availability for %@
Cleaned up failed availability reestablishment state for %@
modifying inertial odometry stream
-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke_2
### unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress failed to start XPC
### modifyPeripheralInertialOdometryWithBtAddress failed to start XPC
### unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier failed to start XPC
-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke_2
Invalidated
Updated inertial odometry availability for %@
Yes
-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke
### forceStartWiFiAwareBrowser failed to start XPC
-[ASMPeripheralControlServices _invalidated]
-[ASMInertialOdometryServices _reestablishAvailabilityForBtAddress:]
### Failed to unsubscribe from inertial odometry availability for btAddress %@: %{error}
Unknown
Resubscribing to inertial odometry availability for peripheral: %@
### Availability resubscription failed for %@: %{error}
Converting btAddress %@ to identifier %@ for availability resubscription
Waiting for availability before reestablishing data subscriptions
Updating inertial odometry availability entry for %@ using identifier %@
-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke
-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke_2
ASMCompanionServices
com.apple.AccessorySensorManager
-[ASMInertialOdometryServices _reestablishSubscriptions]
-[ASMInertialOdometryServices _cleanupFailedDataReestablishment:]
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2
cms
startWiFiAwarePublisherForHandoff
### subscribeToInertialOdometryAvailabilityChangeWithIdentifier no XPC
Tracking inertial odometry availability subscription for btAddress %@
### unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress no XPC
setupDataPipeWithCompanionDevice for btAddress:%@
-[ASMInertialOdometryServices _interrupted]
Reestablishing subscriptions after daemon restart
### No identifier mapping found for btAddress %@
-[ASMInertialOdometryServices invalidate]_block_invoke
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2
### Failed to subscribe to inertial odometry availability for btAddress %@: %{error}
### Availability resubscription XPC error for %@: %{error}
-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:btAddress:]_block_invoke
### Activate XPC error: %{error}
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke
### startWiFiAwareSubscriberAndPairForHandoff failed to start XPC
### forceStartWiFiAwareListener no XPC
-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke
### forceStartWiFiAwareBrowser no XPC
ASMInertialOdometryServices
### setupDataPipeWithCompanionDevice XPC error: %{error}
-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke_2
-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke
### modifyPeripheralInertialOdometryWithBtAddress no XPC
subscribing to inertial odometry availability
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_3
### subscribeToInertialOdometryAvailabilityChangeWithBtAddress no XPC
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_3
### modifyPeripheralConfiguration no XPC
inom
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_3
### startWiFiAwarePublisherForHandoff no XPC
ASMPeripheralControlServices, CID 0x%X
### writeWithData failed to start XPC
ASMInertialOdometryServices, CID 0x%X
-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke_2
-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke_2
Recorded btAddress - %@ with identifer - %@
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke
Tracking inertial odometry availability subscription for %@
### setupDataPipeWithCompanionDevice failed to start XPC
forceStartWiFiAwareBrowser, CID 0x%X
-[ASMPeripheralControlServices _interrupted]
modifyPeripheralConfiguration %@ for %@, CID 0x%X
-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke
### modifyPeripheralInertialOdometryWithIdentifier failed to start XPC
-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke
### subscribeToInertialOdometryAvailabilityChangeWithIdentifier failed to start XPC
### startWiFiAwarePublisherForHandoff XPC error: %{error}
-[ASMPeripheralControlServices invalidate]_block_invoke
### writeWithData no XPC
Client received inertial odometry data - %@
-[ASMCompanionServices _interrupted]
### setupDataPipeWithCompanionDevice no XPC
forceStartWiFiAwareListener, CID 0x%X
### forceStartWiFiAwareListener XPC error: %{error}
-[ASMPeripheralControlServices writeWithData:characteristic:identifier:completion:]_block_invoke
-[ASMInertialOdometryServices _invalidated]
-[ASMInertialOdometryServices _recordInertialOdometryAvailability:forBtAddress:]
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2
### Failed to subscribe to inertial odometry availability for %@: %{error}
### Failed to unsubscribe from inertial odometry availability for %@: %{error}
-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke_2
### startWiFiAwareSubscriberAndPairForHandoff no XPC
### forceStartWiFiAwareBrowser XPC error: %{error}
### Interrupted
cid
-[ASMPeripheralControlServices writeWithData:characteristic:identifier:completion:]_block_invoke_2
Availability now available for %@, reestablishing data subscription
-[ASMInertialOdometryServices _recordBtAddressToIdentifierMapping:identifier:]
-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke
### startWiFiAwareSubscriberAndPairForHandoff XPC error: %{error}
ASMCompanionServices, CID 0x%X
Inertial odometry availability has been updated to %s for %@
%@
### XPC connection unexpectedly invalidated
### unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier no XPC
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2
-[ASMCompanionServices _invalidated]
### forceStartWiFiAwareListener failed to start XPC
-[ASMCompanionServices invalidate]_block_invoke
No XPC connection available
unsubscribing from inertial odometry availability
-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke_2
### modifyPeripheralConfiguration failed to start XPC
Cleaned up failed data reestablishment state for %@
Removing inertial odometry availability subscription tracking for %@
-[ASMPeripheralControlServices modifyPeripheralConfiguration:identifier:completion:]_block_invoke
Removing inertial odometry availability subscription tracking for btAddress %@
?
-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke
### startWiFiAwarePublisherForHandoff failed to start XPC
-[ASMPeripheralControlServices modifyPeripheralConfiguration:identifier:completion:]_block_invoke_2
-[ASMInertialOdometryServices _cleanupFailedAvailabilityReestablishment:]
writeWithData %@ with %@ characteristic for %@, CID 0x%X
-[ASMInertialOdometryServices _attemptReconnection]
-[ASMInertialOdometryServices _attemptReestablishData]
-[ASMInertialOdometryServices inertialOdometryDataReceived:]_block_invoke
### modifyPeripheralInertialOdometryWithIdentifier no XPC
### subscribeToInertialOdometryAvailabilityChangeWithBtAddress failed to start XPC
Attempting reconnection after interruption
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_3
### _reestablishAvailabilityForIdentifier no XPC
Invalidating
-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke
-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]
-[ASMInertialOdometryServices _recordInertialOdometryAvailability:forPeripheral:]
No
startWiFiAwareSubscriberAndPairForHandoff
ASMPeripheralControlServices
-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke
v8@?0
### Reconnection XPC start failed: %{error}
```
