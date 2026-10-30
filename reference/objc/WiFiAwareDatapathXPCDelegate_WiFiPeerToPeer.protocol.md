# `WiFiAwareDatapathXPCDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance methods

```
-[WiFiAwareDatapathXPCDelegate datapathFailedToStartWithError:];
-[WiFiAwareDatapathXPCDelegate datapathConfirmedForPeerDataAddress:serviceSpecificInfo:];
-[WiFiAwareDatapathXPCDelegate datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:];
-[WiFiAwareDatapathXPCDelegate datapathReceivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:];
-[WiFiAwareDatapathXPCDelegate datapathStartedWithInstanceID:initiatorDataAddress:localInterfaceIndex:];
-[WiFiAwareDatapathXPCDelegate datapathTerminatedWithReason:];
-[WiFiAwareDatapathXPCDelegate datapathUpdatedInternetSharingPolicy:];
-[WiFiAwareDatapathXPCDelegate datapathUpdatedPeerRSSI:];
-[WiFiAwareDatapathXPCDelegate datapathUpdatedServiceSpecificInfo:];
-[WiFiAwareDatapathXPCDelegate datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:];
-[WiFiAwareDatapathXPCDelegate datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:];
```
