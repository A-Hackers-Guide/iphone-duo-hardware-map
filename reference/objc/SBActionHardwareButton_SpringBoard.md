# `SBActionHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDButtonStateDelegate`, `SBSystemActionControlObserver`, `SBSystemActionSuppressionManagerObserver`, `PTSettingsKeyObserver`, `SBHardwareButtonColluding`
- 11 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"SBActionButtonParameters" _parameters;
@"SBActionHardwareButtonSettings" _settings;
@"SBSystemActionControl" _systemActionControl;
@"SBSystemActionSuppressionManager" _suppressionManager;
B _inhibitActions;
@"<SBPhysicalButtonCompletionHandling>" _overrideButtonUpHandler;
@"<BSInvalidatable>" _buttonActiveAssertion;
@"<BSInvalidatable>" _systemActionPreviewingAssertion;
@"<BSInvalidatable>" _systemActionPerformedInteractionAssertion;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"SBHIDButtonStateArbiter" _buttonArbiter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
```

## Class methods

```
+[SBActionHardwareButton new];
```

## Instance methods

```
-[SBActionHardwareButton init];
-[SBActionHardwareButton hardwareButtonIdentifier];
-[SBActionHardwareButton cancelHardwareButtonPress];
-[SBActionHardwareButton settings:changedValueForKey:];
-[SBActionHardwareButton performActionsForButtonUp:];
-[SBActionHardwareButton performActionsForButtonDown:];
-[SBActionHardwareButton setHardwareButtonCoordinator:];
-[SBActionHardwareButton performActionsForButtonLongPress:];
-[SBActionHardwareButton hardwareButtonCoordinator];
-[SBActionHardwareButton systemActionControlDidUpdateActionInteractionConfiguration:];
-[SBActionHardwareButton systemActionSuppressionManager:didUpdateSuppressionStatus:];
```
