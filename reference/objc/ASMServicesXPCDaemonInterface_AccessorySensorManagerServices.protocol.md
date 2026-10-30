# `ASMServicesXPCDaemonInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`](../userland/System__Library__PrivateFrameworks__AccessorySensorManagerServices.framework__AccessorySensorManagerServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance methods

```
-[ASMServicesXPCDaemonInterface forceStartWiFiAwareBrowser:];
-[ASMServicesXPCDaemonInterface forceStartWiFiAwareListener:];
-[ASMServicesXPCDaemonInterface getPeripheralIdentifierFromBtAddress:btAddress:completion:];
-[ASMServicesXPCDaemonInterface inertialOdometryAvailabilityChanged:forPeripheral:btAddress:];
-[ASMServicesXPCDaemonInterface inertialOdometryDataReceived:];
-[ASMServicesXPCDaemonInterface modify:peripheralConfiguration:identifier:completion:];
-[ASMServicesXPCDaemonInterface modifyInertialOdometryWithBtAddress:configuration:btAddress:completion:];
-[ASMServicesXPCDaemonInterface modifyInertialOdometryWithIdentifier:configuration:identifier:completion:];
-[ASMServicesXPCDaemonInterface setupDataPipeWithCompanionDevice:completion:];
-[ASMServicesXPCDaemonInterface startWiFiAwarePublisherForHandoff:];
-[ASMServicesXPCDaemonInterface startWiFiAwareSubscriberAndPairForHandoff:];
-[ASMServicesXPCDaemonInterface subscribeToInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:completion:];
-[ASMServicesXPCDaemonInterface subscribeToInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:completion:];
-[ASMServicesXPCDaemonInterface unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:completion:];
-[ASMServicesXPCDaemonInterface unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:completion:];
-[ASMServicesXPCDaemonInterface write:withData:characteristic:identifier:completion:];
```
