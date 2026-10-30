# `SBFUserAuthenticationModelJournaledDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFUserAuthenticationModel`
- 10 instance variables, 9 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"MCProfileConnection" _profileConnection;
@"SBSecurityDefaults" _securityDefaults;
@"NSString" _journalPath;
@"NSObject<OS_dispatch_queue>" _persistentStateQueue;
B _speculativePasscodeFailureChargeOutstanding;
@"NSDictionary" _originalDefaultsForRollback;
B _pendingWipe;
B _permanentlyBlocked;
d _unblockTime;
@"<SBFUserAuthenticationModelDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBFUserAuthenticationModelDelegate>",N,V_delegate) delegate;
@property (TB,R,N,GisTemporarilyBlocked) temporarilyBlocked;
@property (TB,R,N,GisPermanentlyBlocked) permanentlyBlocked;
@property (TB,R,N,GisUserRequestedEraseEnabled) userRequestedEraseEnabled;
@property (Td,R,N) timeUntilUnblockedSinceReferenceDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFUserAuthenticationModelJournaledDefaults _journaledDefaultsAndTypes];
```

## Instance methods

```
-[SBFUserAuthenticationModelJournaledDefaults synchronize];
-[SBFUserAuthenticationModelJournaledDefaults init];
-[SBFUserAuthenticationModelJournaledDefaults notePasscodeEntryBegan];
-[SBFUserAuthenticationModelJournaledDefaults setDelegate:];
-[SBFUserAuthenticationModelJournaledDefaults notePasscodeEntryCancelled];
-[SBFUserAuthenticationModelJournaledDefaults delegate];
-[SBFUserAuthenticationModelJournaledDefaults _copyLockControllerDefaults];
-[SBFUserAuthenticationModelJournaledDefaults _evaluatePendingWipe];
-[SBFUserAuthenticationModelJournaledDefaults _initWithJournalPath:securityDefaults:profileConnection:];
-[SBFUserAuthenticationModelJournaledDefaults _isDeviceWipePreferenceEnabled];
-[SBFUserAuthenticationModelJournaledDefaults _loadLockControllerDefaults:];
-[SBFUserAuthenticationModelJournaledDefaults _loadLockControllerDefaultsJournalIfNecessary];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_beginSpeculativeFailureCharge];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_cancelSpeculativeFailureCharge];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_clearBlockedState];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_evaluatePendingWipe];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_loadLockState];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_unlockFailedWithError:];
-[SBFUserAuthenticationModelJournaledDefaults _persistentStateQueue_unlockSucceeded];
-[SBFUserAuthenticationModelJournaledDefaults _updateLockControllerDefaultsJournal];
-[SBFUserAuthenticationModelJournaledDefaults clearBlockedState];
-[SBFUserAuthenticationModelJournaledDefaults isPermanentlyBlocked];
-[SBFUserAuthenticationModelJournaledDefaults isTemporarilyBlocked];
-[SBFUserAuthenticationModelJournaledDefaults isUserRequestedEraseEnabled];
-[SBFUserAuthenticationModelJournaledDefaults notePasscodeUnlockFailedWithError:];
-[SBFUserAuthenticationModelJournaledDefaults notePasscodeUnlockSucceeded];
-[SBFUserAuthenticationModelJournaledDefaults performPasswordTest:];
-[SBFUserAuthenticationModelJournaledDefaults test_reloadState];
-[SBFUserAuthenticationModelJournaledDefaults timeUntilUnblockedSinceReferenceDate];
-[SBFUserAuthenticationModelJournaledDefaults updateLockControllerDefaultsWithBlock:journaled:];
```
