# `WiFiAwarePublisherXPCDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance methods

```
-[WiFiAwarePublisherXPCDelegate publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:];
-[WiFiAwarePublisherXPCDelegate publishDataTerminatedForHandle:reason:];
-[WiFiAwarePublisherXPCDelegate publishDetectedMulticastError:fromMulticastReceiver:];
-[WiFiAwarePublisherXPCDelegate publishFailedToStartWithError:];
-[WiFiAwarePublisherXPCDelegate publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalCompletion:];
-[WiFiAwarePublisherXPCDelegate publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalHandler:];
-[WiFiAwarePublisherXPCDelegate publishPairingRequestEndedWithSubscriber:reason:];
-[WiFiAwarePublisherXPCDelegate publishPairingRequestIndicatedBySubscriber:withPairingMethod:pairingAuthenticationGeneratedCompletionHandler:];
-[WiFiAwarePublisherXPCDelegate publishReceivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:];
-[WiFiAwarePublisherXPCDelegate publishReceivedDataBlobForMulticastSession:fromPeer:];
-[WiFiAwarePublisherXPCDelegate publishReceivedMessage:fromSubscriberID:subscriberAddress:];
-[WiFiAwarePublisherXPCDelegate publishStartedWithInstanceID:maximumNANDataPath:];
-[WiFiAwarePublisherXPCDelegate publishTerminatedWithReason:];
-[WiFiAwarePublisherXPCDelegate newPairingSessionFromInitiatorAddress:];
-[WiFiAwarePublisherXPCDelegate publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:];
-[WiFiAwarePublisherXPCDelegate publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:];
-[WiFiAwarePublisherXPCDelegate publishKeysBlobForMulticastSession:];
-[WiFiAwarePublisherXPCDelegate publishPairingDidSucceedWithPairingKeyStoreID:deviceID:];
-[WiFiAwarePublisherXPCDelegate receivedNewPairingSessionFromInitiatorAddress:withSubscriberInfo:];
-[WiFiAwarePublisherXPCDelegate receivedNewPairingSessionFromInitiatorAddress:withSubscriberInfo:userApprovalHandler:];
```
