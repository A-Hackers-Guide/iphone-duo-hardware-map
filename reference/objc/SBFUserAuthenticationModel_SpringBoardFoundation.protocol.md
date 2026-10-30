# `SBFUserAuthenticationModel` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"<SBFUserAuthenticationModelDelegate>",N) delegate;
@property (TB,R,N,GisTemporarilyBlocked) temporarilyBlocked;
@property (TB,R,N,GisPermanentlyBlocked) permanentlyBlocked;
@property (TB,R,N,GisUserRequestedEraseEnabled) userRequestedEraseEnabled;
@property (Td,R,N) timeUntilUnblockedSinceReferenceDate;
```

## Instance methods

```
-[SBFUserAuthenticationModel synchronize];
-[SBFUserAuthenticationModel notePasscodeEntryBegan];
-[SBFUserAuthenticationModel setDelegate:];
-[SBFUserAuthenticationModel notePasscodeEntryCancelled];
-[SBFUserAuthenticationModel delegate];
-[SBFUserAuthenticationModel isPermanentlyBlocked];
-[SBFUserAuthenticationModel isTemporarilyBlocked];
-[SBFUserAuthenticationModel isUserRequestedEraseEnabled];
-[SBFUserAuthenticationModel notePasscodeUnlockFailedWithError:];
-[SBFUserAuthenticationModel notePasscodeUnlockSucceeded];
-[SBFUserAuthenticationModel performPasswordTest:];
-[SBFUserAuthenticationModel timeUntilUnblockedSinceReferenceDate];
-[SBFUserAuthenticationModel clearBlockedState];
-[SBFUserAuthenticationModel noteNewMkbDeviceLockState:];
-[SBFUserAuthenticationModel refreshBlockedState];
```
