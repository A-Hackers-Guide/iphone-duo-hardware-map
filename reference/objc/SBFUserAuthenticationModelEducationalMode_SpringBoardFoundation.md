# `SBFUserAuthenticationModelEducationalMode`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFUserAuthenticationModel`
- 3 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBFMobileKeyBag" _keybag;
B _pendingWipe;
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
-[SBFUserAuthenticationModelEducationalMode synchronize];
-[SBFUserAuthenticationModelEducationalMode notePasscodeEntryBegan];
-[SBFUserAuthenticationModelEducationalMode setDelegate:];
-[SBFUserAuthenticationModelEducationalMode notePasscodeEntryCancelled];
-[SBFUserAuthenticationModelEducationalMode delegate];
-[SBFUserAuthenticationModelEducationalMode initWithKeyBag:];
-[SBFUserAuthenticationModelEducationalMode _refreshStateAndNotify:];
-[SBFUserAuthenticationModelEducationalMode _refreshStateForMkbState:notify:];
-[SBFUserAuthenticationModelEducationalMode isPermanentlyBlocked];
-[SBFUserAuthenticationModelEducationalMode isTemporarilyBlocked];
-[SBFUserAuthenticationModelEducationalMode isUserRequestedEraseEnabled];
-[SBFUserAuthenticationModelEducationalMode noteNewMkbDeviceLockState:];
-[SBFUserAuthenticationModelEducationalMode notePasscodeUnlockFailedWithError:];
-[SBFUserAuthenticationModelEducationalMode notePasscodeUnlockSucceeded];
-[SBFUserAuthenticationModelEducationalMode performPasswordTest:];
-[SBFUserAuthenticationModelEducationalMode timeUntilUnblockedSinceReferenceDate];
```
