# `SBTestAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertItem`
- 9 instance variables, 9 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _shouldShowInLockScreen;
B _forcesModalAlertAppearance;
B _behavesSuperModally;
B _allowMenuButtonDismissal;
B _allowLockScreenDismissal;
B _reappearsAfterUnlock;
B _reappearsAfterLock;
@"NSString" _title;
@"NSString" _message;
```

## Properties

```
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_message) message;
@property (TB,N,V_shouldShowInLockScreen) shouldShowInLockScreen;
@property (TB,N,V_forcesModalAlertAppearance) forcesModalAlertAppearance;
@property (TB,N,V_behavesSuperModally) behavesSuperModally;
@property (TB,N,V_allowMenuButtonDismissal) allowMenuButtonDismissal;
@property (TB,N,V_allowLockScreenDismissal) allowLockScreenDismissal;
@property (TB,N,V_reappearsAfterUnlock) reappearsAfterUnlock;
@property (TB,N,V_reappearsAfterLock) reappearsAfterLock;
```

## Class methods

```
+[SBTestAlertItem alertItemWithShowInLockScreen:forcesModal:superModal:];
```

## Instance methods

```
-[SBTestAlertItem allowMenuButtonDismissal];
-[SBTestAlertItem setMessage:];
-[SBTestAlertItem reappearsAfterUnlock];
-[SBTestAlertItem reappearsAfterLock];
-[SBTestAlertItem message];
-[SBTestAlertItem configure:requirePasscodeForActions:];
-[SBTestAlertItem forcesModalAlertAppearance];
-[SBTestAlertItem title];
-[SBTestAlertItem shouldShowInLockScreen];
-[SBTestAlertItem description];
-[SBTestAlertItem allowLockScreenDismissal];
-[SBTestAlertItem setTitle:];
-[SBTestAlertItem behavesSuperModally];
-[SBTestAlertItem setAllowLockScreenDismissal:];
-[SBTestAlertItem setAllowMenuButtonDismissal:];
-[SBTestAlertItem setBehavesSuperModally:];
-[SBTestAlertItem setForcesModalAlertAppearance:];
-[SBTestAlertItem setReappearsAfterLock:];
-[SBTestAlertItem setReappearsAfterUnlock:];
-[SBTestAlertItem setShouldShowInLockScreen:];
```
