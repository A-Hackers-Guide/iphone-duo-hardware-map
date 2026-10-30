# `SBFUserAuthenticationModelSEP`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFUserAuthenticationModel`
- 8 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBFMobileKeyBag" _keybag;
d _unblockTime;
B _permanentlyBlocked;
B _pendingWipe;
B _userRequestedEraseEnabled;
@"SBSecurityDefaults" _securityDefaults;
@"MCProfileConnection" _profileConnection;
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

## Instance methods

```
-[SBFUserAuthenticationModelSEP synchronize];
-[SBFUserAuthenticationModelSEP notePasscodeEntryBegan];
-[SBFUserAuthenticationModelSEP setDelegate:];
-[SBFUserAuthenticationModelSEP notePasscodeEntryCancelled];
-[SBFUserAuthenticationModelSEP delegate];
-[SBFUserAuthenticationModelSEP description];
-[SBFUserAuthenticationModelSEP descriptionBuilder];
-[SBFUserAuthenticationModelSEP initWithKeyBag:];
-[SBFUserAuthenticationModelSEP _initWithKeyBag:profileConnection:];
-[SBFUserAuthenticationModelSEP _isDeviceWipePreferenceEnabled];
-[SBFUserAuthenticationModelSEP _refreshStateAndNotify:];
-[SBFUserAuthenticationModelSEP _refreshStateForMkbState:notify:];
-[SBFUserAuthenticationModelSEP clearBlockedState];
-[SBFUserAuthenticationModelSEP isPermanentlyBlocked];
-[SBFUserAuthenticationModelSEP isTemporarilyBlocked];
-[SBFUserAuthenticationModelSEP isUserRequestedEraseEnabled];
-[SBFUserAuthenticationModelSEP noteNewMkbDeviceLockState:];
-[SBFUserAuthenticationModelSEP notePasscodeUnlockFailedWithError:];
-[SBFUserAuthenticationModelSEP notePasscodeUnlockSucceeded];
-[SBFUserAuthenticationModelSEP performPasswordTest:];
-[SBFUserAuthenticationModelSEP refreshBlockedState];
-[SBFUserAuthenticationModelSEP timeUntilUnblockedSinceReferenceDate];
```
