# `SBLockScreenUnlockRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 12 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _wantsBiometricPresentation;
B _forceAlertAuthenticationUI;
B _confirmedNotInPocket;
i _source;
i _intent;
@"NSString" _name;
@"BSProcessHandle" _process;
@"SBApplication" _destinationApplication;
@"NSString" _title;
@"NSString" _subtitle;
@"NSString" _unlockDestination;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (Ti,N,V_source) source;
@property (Ti,N,V_intent) intent;
@property (T@"BSProcessHandle",&,N,V_process) process;
@property (T@"SBApplication",&,N,V_destinationApplication) destinationApplication;
@property (TB,N,V_wantsBiometricPresentation) wantsBiometricPresentation;
@property (TB,N,V_forceAlertAuthenticationUI) forceAlertAuthenticationUI;
@property (TB,N,V_confirmedNotInPocket) confirmedNotInPocket;
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_subtitle) subtitle;
@property (T@"NSString",&,N,V_unlockDestination) unlockDestination;
@property (T@"SBWindowScene",&,N,V_windowScene) windowScene;
```

## Instance methods

```
-[SBLockScreenUnlockRequest setProcess:];
-[SBLockScreenUnlockRequest setWindowScene:];
-[SBLockScreenUnlockRequest subtitle];
-[SBLockScreenUnlockRequest setIntent:];
-[SBLockScreenUnlockRequest forceAlertAuthenticationUI];
-[SBLockScreenUnlockRequest intent];
-[SBLockScreenUnlockRequest setConfirmedNotInPocket:];
-[SBLockScreenUnlockRequest process];
-[SBLockScreenUnlockRequest unlockDestination];
-[SBLockScreenUnlockRequest setSubtitle:];
-[SBLockScreenUnlockRequest setSource:];
-[SBLockScreenUnlockRequest setDestinationApplication:];
-[SBLockScreenUnlockRequest wantsBiometricPresentation];
-[SBLockScreenUnlockRequest title];
-[SBLockScreenUnlockRequest hash];
-[SBLockScreenUnlockRequest description];
-[SBLockScreenUnlockRequest setName:];
-[SBLockScreenUnlockRequest setTitle:];
-[SBLockScreenUnlockRequest setUnlockDestination:];
-[SBLockScreenUnlockRequest confirmedNotInPocket];
-[SBLockScreenUnlockRequest copyWithZone:];
-[SBLockScreenUnlockRequest setWantsBiometricPresentation:];
-[SBLockScreenUnlockRequest windowScene];
-[SBLockScreenUnlockRequest isEqual:];
-[SBLockScreenUnlockRequest setForceAlertAuthenticationUI:];
-[SBLockScreenUnlockRequest name];
-[SBLockScreenUnlockRequest destinationApplication];
-[SBLockScreenUnlockRequest source];
```
