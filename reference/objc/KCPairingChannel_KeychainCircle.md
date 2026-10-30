# `KCPairingChannel`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 27 properties, 107 instance methods, 7 class methods

## Instance variables

```
B _needInitialSync;
B _initiator;
B _acceptorWillSendInitialSyncCredentials;
B _acceptorWillSendPCSData;
B _initiatorExpectPCSData;
B _grabbedLockAssertion;
B _testFailSOS;
B _testFailOctagon;
B _sessionSupportsSOS;
B _sessionSupportsOctagon;
I _counter;
I _acceptorInitialSyncCredentialsFlags;
@"KCPairingChannelContext" _peerVersionContext;
@"NSString" _dsidForTest;
@"NSNumber" _ackNumber;
@"NSArray" _allPCSItemPersistentRefs;
Q _itemIndex;
@"NSNumber" _countOfReceivedItems;
@"NSNumber" _countOfSentItems;
@"NSNumber" _sizeOfPacket;
@"NSXPCConnection" _connection;
@"OTControl" _otControl;
@? _nextOctagonState;
@? _nextState;
@"OTJoiningConfiguration" _joiningConfiguration;
@"OTControlArguments" _controlArguments;
@"NSString" _altDSID;
```

## Properties

```
@property (T@"KCPairingChannelContext",&,N,V_peerVersionContext) peerVersionContext;
@property (TB,V_initiator) initiator;
@property (TI,V_counter) counter;
@property (TB,V_acceptorWillSendInitialSyncCredentials) acceptorWillSendInitialSyncCredentials;
@property (TI,V_acceptorInitialSyncCredentialsFlags) acceptorInitialSyncCredentialsFlags;
@property (TB,V_acceptorWillSendPCSData) acceptorWillSendPCSData;
@property (TB,V_initiatorExpectPCSData) initiatorExpectPCSData;
@property (T@"NSString",&,N,V_dsidForTest) dsidForTest;
@property (T@"NSNumber",&,N,V_ackNumber) ackNumber;
@property (T@"NSArray",&,N,V_allPCSItemPersistentRefs) allPCSItemPersistentRefs;
@property (TQ,N,V_itemIndex) itemIndex;
@property (TB,N,V_grabbedLockAssertion) grabbedLockAssertion;
@property (T@"NSNumber",&,N,V_countOfReceivedItems) countOfReceivedItems;
@property (T@"NSNumber",&,N,V_countOfSentItems) countOfSentItems;
@property (T@"NSNumber",&,N,V_sizeOfPacket) sizeOfPacket;
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (T@"OTControl",&,V_otControl) otControl;
@property (T@?,C,V_nextOctagonState) nextOctagonState;
@property (T@?,C,V_nextState) nextState;
@property (T@"OTJoiningConfiguration",&,N,V_joiningConfiguration) joiningConfiguration;
@property (T@"OTControlArguments",&,N,V_controlArguments) controlArguments;
@property (TB,N,V_testFailSOS) testFailSOS;
@property (TB,N,V_testFailOctagon) testFailOctagon;
@property (T@"NSString",C,N,V_altDSID) altDSID;
@property (TB,V_sessionSupportsSOS) sessionSupportsSOS;
@property (TB,V_sessionSupportsOctagon) sessionSupportsOctagon;
@property (TB,R,V_needInitialSync) needInitialSync;
```

## Class methods

```
+[KCPairingChannel pairingChannelAcceptor:];
+[KCPairingChannel pairingChannelInitiator:];
+[KCPairingChannel _isRetryableNSURLError:];
+[KCPairingChannel isSupportedPlatform];
+[KCPairingChannel pairingChannelCompressData:];
+[KCPairingChannel pairingChannelDecompressData:];
+[KCPairingChannel retryable:];
```

## Instance methods

```
-[KCPairingChannel nextState];
-[KCPairingChannel setInitiator:];
-[KCPairingChannel updateItem:];
-[KCPairingChannel initiator];
-[KCPairingChannel setAltDSID:];
-[KCPairingChannel altDSID];
-[KCPairingChannel setConfiguration:];
-[KCPairingChannel connection];
-[KCPairingChannel setConnection:];
-[KCPairingChannel itemIndex];
-[KCPairingChannel setItemIndex:];
-[KCPairingChannel counter];
-[KCPairingChannel otControl];
-[KCPairingChannel setCounter:];
-[KCPairingChannel setOtControl:];
-[KCPairingChannel fetchCountOfSentItemsForTesting];
-[KCPairingChannel initiatorFourthPacket:complete:];
-[KCPairingChannel needInitialSync];
-[KCPairingChannel setDsidForTest:];
-[KCPairingChannel acceptorPCSDataPacket:complete:];
-[KCPairingChannel fetchPrepare:application:error:];
-[KCPairingChannel initiatorSecondPacket:complete:];
-[KCPairingChannel setDSIDForTest:];
-[KCPairingChannel setTestFailSOS:];
-[KCPairingChannel testFailOctagon];
-[KCPairingChannel acceptorFirstOctagonPacket:reply:complete:];
-[KCPairingChannel acceptorFirstPacket:complete:];
-[KCPairingChannel acceptorInitialSyncCredentialsFlags];
-[KCPairingChannel acceptorSecondOctagonPacket:reply:complete:];
-[KCPairingChannel acceptorSecondPacket:complete:];
-[KCPairingChannel acceptorThirdPacket:complete:];
-[KCPairingChannel acceptorWaitForAck:complete:];
-[KCPairingChannel acceptorWillSendInitialSyncCredentials];
-[KCPairingChannel acceptorWillSendPCSData];
-[KCPairingChannel ackNumber];
-[KCPairingChannel allPCSItemPersistentRefs];
-[KCPairingChannel controlArguments];
-[KCPairingChannel copySubsetFrom:begin:end:];
-[KCPairingChannel countOfReceivedItems];
-[KCPairingChannel countOfSentItems];
-[KCPairingChannel createPacket:results:endSession:];
-[KCPairingChannel createTempPacket:pcsItem:octagonData:keyForItem:];
-[KCPairingChannel createTempPacketAndCheckSize:pcsItem:octagonData:keyForItem:error:];
-[KCPairingChannel dsidForTest];
-[KCPairingChannel ensureControlChannel];
-[KCPairingChannel evaluateResults:];
-[KCPairingChannel exchangePacket:complete:];
-[KCPairingChannel exchangePacket:complete:error:];
-[KCPairingChannel fetchAcceptorWillSendPCSData];
-[KCPairingChannel fetchCountOfReceivedItemsForTesting];
-[KCPairingChannel fetchEpoch:error:];
-[KCPairingChannel fetchItemForPersistentRef:error:];
-[KCPairingChannel fetchNumberOfPCSKeychainItems];
-[KCPairingChannel fetchPCSItemPersistentRefs:error:];
-[KCPairingChannel fetchSizeOfPacketForTesting];
-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:];
-[KCPairingChannel formNextPacket];
-[KCPairingChannel grabbedLockAssertion];
-[KCPairingChannel initAsInitiator:version:];
-[KCPairingChannel initiatorCompleteSecondPacketOctagon:application:complete:];
-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:];
-[KCPairingChannel initiatorExpectPCSData];
-[KCPairingChannel initiatorFirstPacket:complete:];
-[KCPairingChannel initiatorPCSDataPacket:complete:];
-[KCPairingChannel initiatorThirdPacket:complete:];
-[KCPairingChannel isPacketSizeAcceptable:error:];
-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:];
-[KCPairingChannel joiningConfiguration];
-[KCPairingChannel nextOctagonState];
-[KCPairingChannel oneStepTooMany:complete:];
-[KCPairingChannel peerVersionContext];
-[KCPairingChannel populateKeychainForTestingWithNumberOfKeychainItems:];
-[KCPairingChannel populateKeychainWithEscrowIdentity];
-[KCPairingChannel populateKeychainWithLargeItemsForTestingWithCount:];
-[KCPairingChannel populateKeychainWithMixedLargeItemsForTestingWithCount:];
-[KCPairingChannel populateKeychainWithTooLargeItemsForTestingWithCount:];
-[KCPairingChannel sessionSupportsOctagon];
-[KCPairingChannel sessionSupportsSOS];
-[KCPairingChannel setAcceptorInitialSyncCredentialsFlags:];
-[KCPairingChannel setAcceptorWillSendInitialSyncCredentials:];
-[KCPairingChannel setAcceptorWillSendPCSData:];
-[KCPairingChannel setAckNumber:];
-[KCPairingChannel setAllPCSItemPersistentRefs:];
-[KCPairingChannel setControlArguments:];
-[KCPairingChannel setControlObject:];
-[KCPairingChannel setCountOfReceivedItems:];
-[KCPairingChannel setCountOfSentItems:];
-[KCPairingChannel setGrabbedLockAssertion:];
-[KCPairingChannel setInitiatorExpectPCSData:];
-[KCPairingChannel setJoiningConfiguration:];
-[KCPairingChannel setNextOctagonState:];
-[KCPairingChannel setNextState:];
-[KCPairingChannel setNextStateError:complete:];
-[KCPairingChannel setOctagonMessageFailForTesting:];
-[KCPairingChannel setPeerVersionContext:];
-[KCPairingChannel setSOSMessageFailForTesting:];
-[KCPairingChannel setSessionControlArguments:];
-[KCPairingChannel setSessionSupportsOctagon:];
-[KCPairingChannel setSessionSupportsOctagonForTesting:];
-[KCPairingChannel setSessionSupportsSOS:];
-[KCPairingChannel setSizeOfPacket:];
-[KCPairingChannel setTestFailOctagon:];
-[KCPairingChannel setXPCConnectionObject:];
-[KCPairingChannel sizeOfPacket];
-[KCPairingChannel testFailSOS];
-[KCPairingChannel validateStart:];
-[KCPairingChannel waitForOctagonUpgrade];
```
