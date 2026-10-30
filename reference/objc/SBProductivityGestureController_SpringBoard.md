# `SBProductivityGestureController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 11 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBSystemGestureManager" _systemGestureManager;
@"<SBKeyboardFocusControlling>" _focusController;
@"SBGestureDefaults" _gestureDefaults;
@"<BSDefaultObserver>" _gestureDefaultsObserver;
@"SBProductivityGestureEducationController" _educationController;
@"_UIKBProductivitySingleTapGesture" _threeFingerSingleTap;
@"_UIKBProductivityDoubleTapGesture" _threeFingerDoubleTap;
@"_UIKBProductivityPanGestureRecognizer" _threeFingerSlide;
@"_UIKBProductivityLongPressGestureRecognizer" _threeFingerLongPress;
@"_UIKBProductivityPinchGestureRecognizer" _threeFingerPinch;
d _initPinchableDistance;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProductivityGestureController _setupGestureRecognizers];
-[SBProductivityGestureController gestureRecognizer:shouldReceiveTouch:];
-[SBProductivityGestureController _orientationOfFocusedSceneForGesture:];
-[SBProductivityGestureController _focusedSceneForAction];
-[SBProductivityGestureController _enabledForCurrentAppScenes];
-[SBProductivityGestureController gestureRecognizerShouldBegin:];
-[SBProductivityGestureController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBProductivityGestureController _isIntegratedDisplayIdentity:];
-[SBProductivityGestureController handleProductivityGesture:];
-[SBProductivityGestureController _evaluateEnablement];
-[SBProductivityGestureController _tearDownGestureRecognizers];
-[SBProductivityGestureController _educationTypeForGesture:direction:];
-[SBProductivityGestureController initWithSystemGestureManager:focusController:gestureDefaults:gestureEducationController:];
-[SBProductivityGestureController slideDirectionWithGesture:];
```
