# `OTClique`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 43 instance methods, 21 class methods

## Instance variables

```
@"NSString" _cliqueMemberIdentifier;
@"OTConfigurationContext" _ctx;
```

## Properties

```
@property (T@"NSString",C,N,V_cliqueMemberIdentifier) cliqueMemberIdentifier;
@property (T@"OTConfigurationContext",R,N,V_ctx) ctx;
```

## Class methods

```
+[OTClique generateInheritanceKey:uuid:reply:];
+[OTClique createCustodianRecoveryKey:uuid:reply:];
+[OTClique storeInheritanceKey:ik:reply:];
+[OTClique recreateInheritanceKey:uuid:oldIK:reply:];
+[OTClique createInheritanceKey:uuid:claimTokenData:wrappingKeyData:reply:];
+[OTClique platformSupportsSOS];
+[OTClique createInheritanceKey:uuid:reply:];
+[OTClique checkCustodianRecoveryKey:custodianRecoveryKeyUUID:reply:];
+[OTClique checkInheritanceKey:inheritanceKeyUUID:reply:];
+[OTClique fetchEscrowRecordsInternal:error:];
+[OTClique findOptimalBottleIDsWithContextData:error:];
+[OTClique getCDPStatus:error:];
+[OTClique preflightRecoverOctagonUsingCustodianRecoveryKey:custodianRecoveryKey:reply:];
+[OTClique preflightRecoverOctagonUsingInheritanceKey:inheritanceKey:reply:];
+[OTClique recoverOctagonUsingCustodianRecoveryKey:custodianRecoveryKey:reply:];
+[OTClique recoverOctagonUsingInheritanceKey:inheritanceKey:reply:];
+[OTClique recoverWithContextData:bottleID:escrowedEntropy:error:];
+[OTClique removeCustodianRecoveryKey:custodianRecoveryKeyUUID:reply:];
+[OTClique removeInheritanceKey:inheritanceKeyUUID:reply:];
+[OTClique setCDPEnabled:error:];
+[OTClique setNewRecoveryKeyWithData:recoveryKey:reply:];
```

## Instance methods

```
-[OTClique fetchUserControllableViewsSyncingEnabled:];
-[OTClique waitForInitialSync:];
-[OTClique setUserControllableViewsSyncStatus:error:];
-[OTClique description];
-[OTClique requestToJoinCircle:];
-[OTClique setupPairingChannelAsInitiator:];
-[OTClique ctx];
-[OTClique disableWalrus:preRecords:reply:];
-[OTClique _fetchCliqueStatus:error:];
-[OTClique accountUserKeyAvailable];
-[OTClique cachedCliqueStatus:error:];
-[OTClique cliqueMemberIdentifier];
-[OTClique cliqueMemberIdentifier:];
-[OTClique copyPeerPeerInfo:];
-[OTClique copyViewUnawarePeerInfo:];
-[OTClique enableWalrus:preRecords:reply:];
-[OTClique establish:];
-[OTClique establish:error:];
-[OTClique fetchCliqueStatus:];
-[OTClique fetchCliqueStatus:error:];
-[OTClique fetchEscrowContents:];
-[OTClique fetchUserControllableViewsSyncingEnabledAsync:];
-[OTClique initWithContextData:];
-[OTClique joinAfterRestore:];
-[OTClique leaveClique:];
-[OTClique makeOTControl:];
-[OTClique peerDeviceNamesByPeerID:];
-[OTClique peersHaveViewsEnabled:error:];
-[OTClique performedCDPStateMachineRun:success:error:reply:];
-[OTClique performedFailureCDPStateMachineRun:error:reply:];
-[OTClique performedSuccessfulCDPStateMachineRun:reply:];
-[OTClique removeFriendsInClique:error:];
-[OTClique resetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:altDSID:flowID:deviceSessionID:canSendMetrics:error:];
-[OTClique setCliqueMemberIdentifier:];
-[OTClique setOctagonUserControllableViewsSyncEnabled:error:];
-[OTClique setUserCredentialsAndDSID:password:error:];
-[OTClique setUserCredentialsWithLabel:password:dsid:error:];
-[OTClique setupPairingChannelAsAcceptor:];
-[OTClique setupPairingChannelAsAcceptor:error:];
-[OTClique setupPairingChannelAsInitator:error:];
-[OTClique tryUserCredentialsAndDSID:password:error:];
-[OTClique tryUserCredentialsWithLabel:password:dsid:error:];
-[OTClique waitForOctagonUpgrade:];
```
