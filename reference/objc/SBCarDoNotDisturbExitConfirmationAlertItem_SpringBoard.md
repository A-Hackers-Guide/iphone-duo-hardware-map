# `SBCarDoNotDisturbExitConfirmationAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertItem`
- Protocols: `SiriUICarDNDDelegate`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _showSiriHeaderViewController;
@? _notDrivingActionHandler;
@? _cancelActionHandler;
```

## Properties

```
@property (T@?,C,N,V_notDrivingActionHandler) notDrivingActionHandler;
@property (T@?,C,N,V_cancelActionHandler) cancelActionHandler;
@property (TB,N,V_showSiriHeaderViewController) showSiriHeaderViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCarDoNotDisturbExitConfirmationAlertItem reappearsAfterUnlock];
-[SBCarDoNotDisturbExitConfirmationAlertItem configure:requirePasscodeForActions:];
-[SBCarDoNotDisturbExitConfirmationAlertItem forcesModalAlertAppearance];
-[SBCarDoNotDisturbExitConfirmationAlertItem shouldShowInLockScreen];
-[SBCarDoNotDisturbExitConfirmationAlertItem setCancelActionHandler:];
-[SBCarDoNotDisturbExitConfirmationAlertItem controllerDidProvideContext:];
-[SBCarDoNotDisturbExitConfirmationAlertItem cancelActionHandler];
-[SBCarDoNotDisturbExitConfirmationAlertItem notDrivingActionHandler];
-[SBCarDoNotDisturbExitConfirmationAlertItem setNotDrivingActionHandler:];
-[SBCarDoNotDisturbExitConfirmationAlertItem setShowSiriHeaderViewController:];
-[SBCarDoNotDisturbExitConfirmationAlertItem showSiriHeaderViewController];
```
