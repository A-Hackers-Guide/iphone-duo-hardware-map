# `WiFiAwarePublisherDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[WiFiAwarePublisherDelegate publisher:terminatedWithReason:];
-[WiFiAwarePublisherDelegate publisher:failedToStartWithError:];
-[WiFiAwarePublisherDelegate publisherStarted:];
-[WiFiAwarePublisherDelegate publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:];
-[WiFiAwarePublisherDelegate publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:];
-[WiFiAwarePublisherDelegate publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:];
-[WiFiAwarePublisherDelegate publisher:dataTerminatedForHandle:reason:];
-[WiFiAwarePublisherDelegate publisher:detectedMulticastError:fromMulticastReceiver:];
-[WiFiAwarePublisherDelegate publisher:getKeysBlobForMulticastSession:];
-[WiFiAwarePublisherDelegate publisher:newPairingSession:];
-[WiFiAwarePublisherDelegate publisher:receivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:];
-[WiFiAwarePublisherDelegate publisher:receivedDataBlobForMulticastSession:fromPeer:];
-[WiFiAwarePublisherDelegate publisher:receivedMessage:fromSubscriberID:subscriberAddress:];
-[WiFiAwarePublisherDelegate publisher:receivedNewPairingSession:withInfo:];
-[WiFiAwarePublisherDelegate publisher:receivedNewPairingSession:withInfo:userApprovalHandler:];
```
