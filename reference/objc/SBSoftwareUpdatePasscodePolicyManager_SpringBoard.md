# `SBSoftwareUpdatePasscodePolicyManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSoftLockoutControllerDelegate`, `SBWindowSceneAttachmentObserving`
- 4 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _softwareUpdatePasscodePolicy;
@"NSMapTable" _softLockoutControllers;
@"SBFMobileKeyBag" _mobileKeyBag;
B _passcodeAuthenticationSuccessPending;
```

## Properties

```
@property (Tq,N) softwareUpdatePasscodePolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSoftwareUpdatePasscodePolicyManager init];
-[SBSoftwareUpdatePasscodePolicyManager windowSceneDidDisconnect:];
-[SBSoftwareUpdatePasscodePolicyManager dealloc];
-[SBSoftwareUpdatePasscodePolicyManager windowSceneDidConnect:];
-[SBSoftwareUpdatePasscodePolicyManager _authRequestCompleted:];
-[SBSoftwareUpdatePasscodePolicyManager _effectiveSoftwareUpdatePasscodePolicy];
-[SBSoftwareUpdatePasscodePolicyManager consumePendingUnlockForSoftLockoutController:];
-[SBSoftwareUpdatePasscodePolicyManager initWithMobileKeyBag:];
-[SBSoftwareUpdatePasscodePolicyManager noteAuthenticationSucceededWithPasscode:];
-[SBSoftwareUpdatePasscodePolicyManager setSoftwareUpdatePasscodePolicy:];
-[SBSoftwareUpdatePasscodePolicyManager softLockoutControllerRequiresLockout:];
-[SBSoftwareUpdatePasscodePolicyManager softwareUpdatePasscodePolicy];
```
