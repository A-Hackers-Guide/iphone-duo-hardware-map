# `ULLogicAdapterServiceHandlingInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance methods

```
-[ULLogicAdapterServiceHandlingInterface removePendingConnectionRequestsByConnectionToken:];
-[ULLogicAdapterServiceHandlingInterface requestPredictionForConnectionToken:clientIdentifier:requestIdentifier:];
-[ULLogicAdapterServiceHandlingInterface requestObservationForConnectionToken:clientIdentifier:requestIdentifier:];
-[ULLogicAdapterServiceHandlingInterface addAnchorForConnectionToken:anchor:];
-[ULLogicAdapterServiceHandlingInterface queryServicesForClient:];
-[ULLogicAdapterServiceHandlingInterface runWithConfiguration:serviceIdentifier:legacyServiceIdentifier:clientIdentifier:connectionToken:requestIdentifier:];
-[ULLogicAdapterServiceHandlingInterface disconnectWithConnectionToken:clientIdentifier:requestIdentifier:];
-[ULLogicAdapterServiceHandlingInterface updateHomeKitUserInteractionAnchorForConnectionToken:anchor:];
-[ULLogicAdapterServiceHandlingInterface deleteServiceWithIdentifier:clientIdentifier:];
-[ULLogicAdapterServiceHandlingInterface removeCustomLoiWithIdentifier:forConnectionToken:];
-[ULLogicAdapterServiceHandlingInterface createCustomLoiAtCurrentLocationForConnectionToken:withConfiguration:];
-[ULLogicAdapterServiceHandlingInterface createServiceWithServiceType:locationTypes:clientId:];
-[ULLogicAdapterServiceHandlingInterface addAnchorForConnectionToken:anchor:betweenStartDate:andEndDate:];
```
