# `OTControl`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 101 instance methods, 2 class methods

## Instance variables

```
B _synchronous;
B _sync;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (TB,V_sync) sync;
@property (TB,V_synchronous) synchronous;
```

## Class methods

```
+[OTControl controlObject:];
+[OTControl controlObject:error:];
```

## Instance methods

```
-[OTControl setSync:];
-[OTControl reroll:reply:];
-[OTControl reset:];
-[OTControl generateInheritanceKey:uuid:reply:];
-[OTControl fetchEgoPeerID:reply:];
-[OTControl performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:];
-[OTControl setSynchronous:];
-[OTControl setCDPEnabled:reply:];
-[OTControl launchBottledPeer:bottleID:reply:];
-[OTControl trustedFullPeers:reply:];
-[OTControl status:context:reply:];
-[OTControl removeInheritanceKey:uuid:reply:];
-[OTControl scrubBottledPeer:bottleID:reply:];
-[OTControl simulateReceivePush:reply:];
-[OTControl createCustodianRecoveryKey:uuid:reply:];
-[OTControl removeLocalSecureElementIdentityPeerID:secureElementIdentityPeerID:reply:];
-[OTControl enableWalrus:preRecords:isDBRv2:pdpState:reply:];
-[OTControl resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:];
-[OTControl status:xpcFd:reply:];
-[OTControl fetchTrustedDeviceList:reply:];
-[OTControl checkCustodianRecoveryKey:uuid:reply:];
-[OTControl fetchCliqueStatus:configuration:reply:];
-[OTControl fetchAllViableBottles:source:reply:];
-[OTControl dealloc];
-[OTControl setLocalSecureElementIdentity:secureElementIdentity:reply:];
-[OTControl waitForOctagonUpgrade:reply:];
-[OTControl preflightRecoverOctagonUsingRecoveryKey:recoveryKey:reply:];
-[OTControl storeInheritanceKey:ik:reply:];
-[OTControl getAccountMetadata:reply:];
-[OTControl appleAccountSignedOut:reply:];
-[OTControl fetchEscrowContents:reply:];
-[OTControl leaveClique:reply:];
-[OTControl preflightBottledPeer:dsid:reply:];
-[OTControl notifyIDMSTrustLevelChangeForAltDSID:reply:];
-[OTControl removeCustodianRecoveryKey:uuid:reply:];
-[OTControl startOctagonStateMachine:reply:];
-[OTControl isRecoveryKeySet:reply:];
-[OTControl establish:reply:];
-[OTControl status:reply:];
-[OTControl escrowCheck:isBackgroundCheck:reply:];
-[OTControl tapToRadar:description:radar:reply:];
-[OTControl fetchTrustStatus:configuration:reply:];
-[OTControl rpcPrepareIdentityAsApplicantWithArguments:configuration:reply:];
-[OTControl icscRepairInvalidateCacheVersion:reply:];
-[OTControl recreateInheritanceKey:uuid:oldIK:reply:];
-[OTControl setAccountSetting:setting:reply:];
-[OTControl fetchEscrowRecords:source:reply:];
-[OTControl fetchTrustedSecureElementIdentities:reply:];
-[OTControl disableWalrus:preRecords:isDBRv2:pdpState:reply:];
-[OTControl clearCliqueFromAccount:resetReason:isDBRv2:reply:];
-[OTControl rpcEpochWithArguments:configuration:reply:];
-[OTControl encryptionKey:];
-[OTControl createInheritanceKey:uuid:claimTokenData:wrappingKeyData:reply:];
-[OTControl rpcVoucherWithArguments:configuration:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:maxCapability:reply:];
-[OTControl peerDeviceNamesByPeerID:reply:];
-[OTControl appleAccountSignedIn:reply:];
-[OTControl checkInheritanceKey:uuid:reply:];
-[OTControl setMachineIDOverride:machineID:reply:];
-[OTControl invalidateEscrowCache:reply:];
-[OTControl tlkRecoverabilityForEscrowRecordData:recordData:source:reply:];
-[OTControl connection];
-[OTControl icscRepairReset:reply:];
-[OTControl signingKey:];
-[OTControl resetAccountCDPContents:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:reply:];
-[OTControl listOfEligibleBottledPeerRecords:];
-[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:forceStableTrustedDeviceIDReroll:reply:];
-[OTControl setConnection:];
-[OTControl getConnection:];
-[OTControl fetchAccountWideSettingsWithForceFetch:arguments:reply:];
-[OTControl postCDPFollowupResult:success:type:error:reply:];
-[OTControl getAsyncConnection:];
-[OTControl setUserControllableViewsSyncStatus:enabled:reply:];
-[OTControl rpcJoinWithArguments:configuration:vouchData:vouchSig:reply:];
-[OTControl refetchCKKSPolicy:reply:];
-[OTControl preflightJoinWithInheritanceKey:inheritanceKey:reply:];
-[OTControl preflightJoinWithCustodianRecoveryKey:custodianRecoveryKey:reply:];
-[OTControl restore:dsid:secret:escrowRecordID:reply:];
-[OTControl restoreFromBottle:entropy:bottleID:reply:];
-[OTControl joinWithRecoveryKey:recoveryKey:reply:];
-[OTControl totalTrustedPeers:reply:];
-[OTControl octagonSigningPublicKey:];
-[OTControl fetchAccountSettings:reply:];
-[OTControl joinWithCustodianRecoveryKey:custodianRecoveryKey:reply:];
-[OTControl fetchStableTrustedDeviceID:reply:];
-[OTControl getCDPStatus:reply:];
-[OTControl removeFriendsInClique:peerIDs:reply:];
-[OTControl sync];
-[OTControl createRecoveryKey:recoveryKey:reply:];
-[OTControl joinWithInheritanceKey:inheritanceKey:reply:];
-[OTControl recoverWithRecoveryKey:recoveryKey:reply:];
-[OTControl initWithConnection:sync:];
-[OTControl synchronous];
-[OTControl simulateReceiveTDLChangePush:reply:];
-[OTControl removeRecoveryKey:reply:];
-[OTControl createInheritanceKey:uuid:reply:];
-[OTControl areRecoveryKeysDistrusted:reply:];
-[OTControl octagonEncryptionPublicKey:];
-[OTControl fetchUserControllableViewsSyncStatus:reply:];
-[OTControl fetchUserControllableViewsSyncStatusAsync:reply:];
-[OTControl listOfRecords:];
-[OTControl waitForPriorityViewKeychainDataRecovery:reply:];
```
