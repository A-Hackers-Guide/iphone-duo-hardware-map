# `UIUserInterfaceStyleArbiter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISUserInterfaceStyleModeDelegate`, `BLSBacklightStateObserving`, `BSDescriptionProviding`
- 14 instance variables, 5 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"UISUserInterfaceStyleMode" _styleMode;
q _currentModeValue;
q _currentStyle;
q _lastProposedAutomaticStyle;
{?="style"q"timing"q} _lastOverride;
B _isAddingBacklightStateObserver;
B _isObservingBacklightState;
B _isDim;
@"_UISunScheduleController" _sunScheduleController;
@"_UICustomScheduleController" _customScheduleController;
@"NSDate" _lastUpdateDate;
@"NSBackgroundActivityScheduler" _backgroundActivityScheduler;
i _notificationToken;
@"<BSInvalidatable>" _stateCaptureToken;
```

## Properties

```
@property (Tq,R,N) currentStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIUserInterfaceStyleArbiter sharedInstance];
```

## Instance methods

```
-[UIUserInterfaceStyleArbiter currentStyle];
-[UIUserInterfaceStyleArbiter debugDescription];
-[UIUserInterfaceStyleArbiter succinctDescriptionBuilder];
-[UIUserInterfaceStyleArbiter backlight:didCompleteUpdateToState:forEvent:];
-[UIUserInterfaceStyleArbiter descriptionWithMultilinePrefix:];
-[UIUserInterfaceStyleArbiter _init];
-[UIUserInterfaceStyleArbiter succinctDescription];
-[UIUserInterfaceStyleArbiter description];
-[UIUserInterfaceStyleArbiter descriptionBuilderWithMultilinePrefix:];
-[UIUserInterfaceStyleArbiter _backlightStateUpdated:updateStyle:];
-[UIUserInterfaceStyleArbiter _logArbiterDecisionToBiomeWithNewStyle:reason:];
-[UIUserInterfaceStyleArbiter _logChangeEventWithNewMode:oldMode:newStyle:oldStyle:reason:];
-[UIUserInterfaceStyleArbiter _logPeriodicEvent];
-[UIUserInterfaceStyleArbiter _proposedStyleForCurrentMode];
-[UIUserInterfaceStyleArbiter _setWatchesScreenDim:];
-[UIUserInterfaceStyleArbiter _updateControllersWithOldModeValue:newModeValue:];
-[UIUserInterfaceStyleArbiter _updateCurrentStyleAndNotify:forReason:];
-[UIUserInterfaceStyleArbiter _updateCurrentStyleForReason:];
-[UIUserInterfaceStyleArbiter nextTransition];
-[UIUserInterfaceStyleArbiter toggleCurrentStyle];
-[UIUserInterfaceStyleArbiter toggleCurrentStyleWithOverrideTiming:];
-[UIUserInterfaceStyleArbiter userInterfaceStyleModeDidChange:];
```
