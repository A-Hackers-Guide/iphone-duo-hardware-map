# `SBFLockScreenActionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSString" _lockLabel;
@"NSString" _shortLockLabel;
@"NSString" _unlockDestination;
@? _action;
@"NSString" _identifier;
d _fontSize;
B _requiresUIUnlock;
B _deactivateAwayController;
B _canBypassPinLock;
B _wantsBiometricPresentation;
i _source;
i _intent;
B _confirmedNotInPocket;
B _requiresAuthentication;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSString",&,N,V_lockLabel) lockLabel;
@property (T@"NSString",&,N,V_shortLockLabel) shortLockLabel;
@property (T@"NSString",C,N,V_unlockDestination) unlockDestination;
@property (T@?,C,N,V_action) action;
@property (TB,N,V_requiresUIUnlock) requiresUIUnlock;
@property (TB,N,V_deactivateAwayController) deactivateAwayController;
@property (TB,N,V_canBypassPinLock) canBypassPinLock;
@property (TB,N,V_requiresAuthentication) requiresAuthentication;
@property (TB,N,V_wantsBiometricPresentation) wantsBiometricPresentation;
@property (TB,N,V_confirmedNotInPocket) confirmedNotInPocket;
@property (Ti,N,V_source) source;
@property (Ti,N,V_intent) intent;
@property (TB,R,N) hasCustomUnlockLabel;
```

## Instance methods

```
-[SBFLockScreenActionContext setRequiresAuthentication:];
-[SBFLockScreenActionContext canBypassPinLock];
-[SBFLockScreenActionContext setIntent:];
-[SBFLockScreenActionContext identifier];
-[SBFLockScreenActionContext requiresAuthentication];
-[SBFLockScreenActionContext intent];
-[SBFLockScreenActionContext setConfirmedNotInPocket:];
-[SBFLockScreenActionContext unlockDestination];
-[SBFLockScreenActionContext setCanBypassPinLock:];
-[SBFLockScreenActionContext setAction:];
-[SBFLockScreenActionContext action];
-[SBFLockScreenActionContext setSource:];
-[SBFLockScreenActionContext setIdentifier:];
-[SBFLockScreenActionContext wantsBiometricPresentation];
-[SBFLockScreenActionContext setUnlockDestination:];
-[SBFLockScreenActionContext confirmedNotInPocket];
-[SBFLockScreenActionContext setWantsBiometricPresentation:];
-[SBFLockScreenActionContext source];
-[SBFLockScreenActionContext deactivateAwayController];
-[SBFLockScreenActionContext hasCustomUnlockLabel];
-[SBFLockScreenActionContext initWithLockLabel:shortLockLabel:action:identifier:];
-[SBFLockScreenActionContext lockLabel];
-[SBFLockScreenActionContext requiresUIUnlock];
-[SBFLockScreenActionContext setDeactivateAwayController:];
-[SBFLockScreenActionContext setLockLabel:];
-[SBFLockScreenActionContext setRequiresUIUnlock:];
-[SBFLockScreenActionContext setShortLockLabel:];
-[SBFLockScreenActionContext shortLockLabel];
```
