# `WiFiAwarePublisher`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAwarePublisherXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 11 instance variables, 7 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"NSMutableArray" _dataSessionHandles;
@"NSNumber" _publishID;
@"NSNumber" _maximumNANDataPath;
@"WiFiAwarePairingConfig" _pairingConfig;
@"<WiFiAwarePairingDelegate>" _pairingDelegate;
@"NSMutableSet" _activePairingSessions;
@"NSObject<OS_os_log>" _logger;
@"<WiFiAwarePublisherDelegate>" _delegate;
@"WiFiAwarePublishConfiguration" _configuration;
@"WiFiAwarePairingSession" _pairingSession;
```

## Properties

```
@property (T@"WiFiAwarePairingSession",&,N,V_pairingSession) pairingSession;
@property (T@"<WiFiAwarePublisherDelegate>",W,N,V_delegate) delegate;
@property (T@"WiFiAwarePublishConfiguration",R,N,V_configuration) configuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwarePublisher handleError:];
-[WiFiAwarePublisher startConnectionUsingProxy:completionHandler:];
-[WiFiAwarePublisher stop];
-[WiFiAwarePublisher remoteObjectInterface];
-[WiFiAwarePublisher start];
-[WiFiAwarePublisher exportedInterface];
-[WiFiAwarePublisher initWithConfiguration:];
-[WiFiAwarePublisher setDelegate:];
-[WiFiAwarePublisher configuration];
-[WiFiAwarePublisher exportedObject];
-[WiFiAwarePublisher delegate];
-[WiFiAwarePublisher description];
-[WiFiAwarePublisher activatePairingModeWithConfig:delegate:completionHandler:];
-[WiFiAwarePublisher generateStatisticsReportForDataSession:completionHandler:];
-[WiFiAwarePublisher reportIssue:forDataSession:];
-[WiFiAwarePublisher sendMessage:toPeerAddress:withInstanceID:completionHandler:];
-[WiFiAwarePublisher terminateDataSession:completionHandler:];
-[WiFiAwarePublisher updateLinkStatus:forDataSession:];
-[WiFiAwarePublisher updateServiceSpecificInfo:completionHandler:];
-[WiFiAwarePublisher pairingSession];
-[WiFiAwarePublisher setPairingSession:];
-[WiFiAwarePublisher deactivatePairingMode];
-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:];
-[WiFiAwarePublisher terminateMulticastSession:completionHandler:];
-[WiFiAwarePublisher updateTimeout:completionHandler:];
-[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:];
-[WiFiAwarePublisher newPairingSessionFromInitiatorAddress:];
-[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:];
-[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:];
-[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:];
-[WiFiAwarePublisher publishDataTerminatedForHandle:reason:];
-[WiFiAwarePublisher publishDetectedMulticastError:fromMulticastReceiver:];
-[WiFiAwarePublisher publishFailedToStartWithError:];
-[WiFiAwarePublisher publishKeysBlobForMulticastSession:];
-[WiFiAwarePublisher publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalCompletion:];
-[WiFiAwarePublisher publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalHandler:];
-[WiFiAwarePublisher publishPairingDidSucceedWithPairingKeyStoreID:deviceID:];
-[WiFiAwarePublisher publishPairingRequestEndedWithSubscriber:reason:];
-[WiFiAwarePublisher publishPairingRequestIndicatedBySubscriber:withPairingMethod:pairingAuthenticationGeneratedCompletionHandler:];
-[WiFiAwarePublisher publishReceivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:];
-[WiFiAwarePublisher publishReceivedDataBlobForMulticastSession:fromPeer:];
-[WiFiAwarePublisher publishReceivedMessage:fromSubscriberID:subscriberAddress:];
-[WiFiAwarePublisher publishStartedWithInstanceID:maximumNANDataPath:];
-[WiFiAwarePublisher publishTerminatedWithReason:];
-[WiFiAwarePublisher receivedNewPairingSessionFromInitiatorAddress:withSubscriberInfo:];
-[WiFiAwarePublisher receivedNewPairingSessionFromInitiatorAddress:withSubscriberInfo:userApprovalHandler:];
-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:];
-[WiFiAwarePublisher updateDatapathServiceSpecificInfo:completionHandler:];
```
