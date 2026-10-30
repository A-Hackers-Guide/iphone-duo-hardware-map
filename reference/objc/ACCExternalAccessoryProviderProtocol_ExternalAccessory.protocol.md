# `ACCExternalAccessoryProviderProtocol` (protocol)

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance methods

```
-[ACCExternalAccessoryProviderProtocol handleIncomingExternalAccessoryData:forEASessionIdentifier:withReply:];
-[ACCExternalAccessoryProviderProtocol EAAccessoryLeft:];
-[ACCExternalAccessoryProviderProtocol EAAccessoryArrived:];
-[ACCExternalAccessoryProviderProtocol accessoryClosedEASession:];
-[ACCExternalAccessoryProviderProtocol resumeEASessionData:];
-[ACCExternalAccessoryProviderProtocol initialEAAccessoriesAttachedAfterClientConnection:];
-[ACCExternalAccessoryProviderProtocol stopDestinationSharingForUUID:];
-[ACCExternalAccessoryProviderProtocol startDestinationSharingForUUID:options:];
-[ACCExternalAccessoryProviderProtocol vehicleStatusUpdate:forAccessoryUUID:];
-[ACCExternalAccessoryProviderProtocol nmeaSentenceArrived:forAccessoryUUID:withTimestamps:];
-[ACCExternalAccessoryProviderProtocol destinationSharingStatus:forDestinationUUID:supportedParams:forUUID:];
-[ACCExternalAccessoryProviderProtocol updateAccessoryInfo:];
-[ACCExternalAccessoryProviderProtocol startDestinationSharingForUUID:];
```
