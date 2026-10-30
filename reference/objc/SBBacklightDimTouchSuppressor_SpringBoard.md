# `SBBacklightDimTouchSuppressor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`, `BSInvalidatable`
- 5 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"SBBacklightController" _backlightController;
@"SBTouchSuppressionManager" _touchSuppressionManager;
@"<BSInvalidatable>" _touchSuppressionAssertion;
q _backlightState;
B _isVoiceOverRunning;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBacklightDimTouchSuppressor supportedForSurfaceType:];
```

## Instance methods

```
-[SBBacklightDimTouchSuppressor backlightController:didTransitionToBacklightState:source:];
-[SBBacklightDimTouchSuppressor dealloc];
-[SBBacklightDimTouchSuppressor invalidate];
-[SBBacklightDimTouchSuppressor _voiceOverStatusDidChange:];
-[SBBacklightDimTouchSuppressor _backlightStateDidChange:];
-[SBBacklightDimTouchSuppressor _initWithBacklightController:initialBacklightState:voiceOverRunning:touchSuppressionManager:];
-[SBBacklightDimTouchSuppressor _isActivelySuppressingTouches];
-[SBBacklightDimTouchSuppressor _updateTouchSuppressionAssertionForBacklightState:voiceOverRunning:];
-[SBBacklightDimTouchSuppressor _voiceOverStatusDidChangeNotification:];
-[SBBacklightDimTouchSuppressor initWithBacklightController:touchSuppressionManager:];
```
