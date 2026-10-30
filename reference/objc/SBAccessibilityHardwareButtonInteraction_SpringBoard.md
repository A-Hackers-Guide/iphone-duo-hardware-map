# `SBAccessibilityHardwareButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SBHardwareButtonInteraction`
- 1 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
Q _buttonType;
```

## Properties

```
@property (TQ,R,N,V_buttonType) buttonType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAccessibilityHardwareButtonInteraction hardwareButtonInteractionForHomeButton];
+[SBAccessibilityHardwareButtonInteraction hardwareButtonInteractionForLockButton];
```

## Instance methods

```
-[SBAccessibilityHardwareButtonInteraction buttonType];
-[SBAccessibilityHardwareButtonInteraction dealloc];
-[SBAccessibilityHardwareButtonInteraction hardwareButtonGestureParameters];
-[SBAccessibilityHardwareButtonInteraction initWithButtonType:];
-[SBAccessibilityHardwareButtonInteraction _registerAsNotificationObserver];
-[SBAccessibilityHardwareButtonInteraction _accessibilityPrefsDidChange];
-[SBAccessibilityHardwareButtonInteraction _downToDownInterval];
-[SBAccessibilityHardwareButtonInteraction _presentMigrationAlertIfNeeded];
-[SBAccessibilityHardwareButtonInteraction _speedChangedNotificationName];
-[SBAccessibilityHardwareButtonInteraction _supportsTripleClick];
-[SBAccessibilityHardwareButtonInteraction _unregisterAsNotificationObserver];
-[SBAccessibilityHardwareButtonInteraction consumeTriplePressUp];
```
