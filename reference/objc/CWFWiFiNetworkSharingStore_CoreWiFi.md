# `CWFWiFiNetworkSharingStore`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"CWFKeyValueStore" _store;
```

## Instance methods

```
-[CWFWiFiNetworkSharingStore activateWithCompletion:];
-[CWFWiFiNetworkSharingStore init];
-[CWFWiFiNetworkSharingStore invalidate];
-[CWFWiFiNetworkSharingStore resetMetadataForBundleID:accessoryID:];
-[CWFWiFiNetworkSharingStore clientIDs];
-[CWFWiFiNetworkSharingStore acknowledgedConnectedAPUpdateCounterForClientID:];
-[CWFWiFiNetworkSharingStore acknowledgedNetworksUpdateCounterForClientID:];
-[CWFWiFiNetworkSharingStore cachedAuthorizationStatusForClientID:];
-[CWFWiFiNetworkSharingStore connectedAPUpdateCounterForClientID:];
-[CWFWiFiNetworkSharingStore incrementConnectedAPUpdateCounterForClientID:];
-[CWFWiFiNetworkSharingStore incrementNetworksUpdateCounterForClientID:];
-[CWFWiFiNetworkSharingStore mostRecentlySharedNetworkDateForClientID:];
-[CWFWiFiNetworkSharingStore networkListUpdateCounterForClientID:];
-[CWFWiFiNetworkSharingStore networkMetadataForClientID:];
-[CWFWiFiNetworkSharingStore networkMetadataForClientID:networkID:];
-[CWFWiFiNetworkSharingStore setAcknowledgedConnectedAPUpdateCounter:clientID:];
-[CWFWiFiNetworkSharingStore setAcknowledgedNetworksUpdateCounter:clientID:];
-[CWFWiFiNetworkSharingStore setCachedAuthorizationStatus:clientID:];
-[CWFWiFiNetworkSharingStore setNetworkMetadata:clientID:networkID:];
```
