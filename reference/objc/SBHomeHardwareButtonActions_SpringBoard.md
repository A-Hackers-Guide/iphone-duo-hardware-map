# `SBHomeHardwareButtonActions`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SBHardwareButtonGestureParametersObserver`
- 14 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _screenWasDimOnMenuDown;
B _dontUnlockOnButtonUp;
q _homeButtonType;
@"SBHardwareButtonActionList" _buttonUpActions;
@"SBHardwareButtonActionList" _buttonUpPostActions;
d _menuButtonHoldStartAbsoluteTime;
@"SBHardwareButtonService" _hardwareButtonService;
@"<SBHardwareButtonInteraction><SBHardwareButtonGestureParametersProvider>" _accessibilityButtonInteraction;
@"<SBHardwareButtonInteraction><SBHardwareButtonGestureParametersProvider>" _siriButtonInteraction;
@"SBHardwareButtonGestureParameters" _accessibilityGestureParameters;
@"SBHardwareButtonGestureParameters" _siriGestureParameters;
B _buttonDown;
d _currentLongPressDuration;
@"SBWindowScene" _targetWindowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_targetWindowScene) targetWindowScene;
@property (TB,N,GisButtonDown,V_buttonDown) buttonDown;
@property (Td,N,V_currentLongPressDuration) currentLongPressDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHomeHardwareButtonActions performLongPressActions];
-[SBHomeHardwareButtonActions performInitialButtonDownActions];
-[SBHomeHardwareButtonActions performWhenMenuButtonIsUpUsingBlock:];
-[SBHomeHardwareButtonActions setTargetWindowScene:];
-[SBHomeHardwareButtonActions performAfterMenuButtonUpIsHandledUsingBlock:];
-[SBHomeHardwareButtonActions performFinalButtonUpActions];
-[SBHomeHardwareButtonActions hardwareButtonGestureParameters];
-[SBHomeHardwareButtonActions provider:didUpdateButtonGestureParameters:];
-[SBHomeHardwareButtonActions isButtonDown];
-[SBHomeHardwareButtonActions performInitialButtonUpActions];
-[SBHomeHardwareButtonActions targetWindowScene];
-[SBHomeHardwareButtonActions performLongPressCancelledActions];
-[SBHomeHardwareButtonActions setButtonDown:];
-[SBHomeHardwareButtonActions _logMenuButtonHoldTime];
-[SBHomeHardwareButtonActions _performButtonPreflightActions];
-[SBHomeHardwareButtonActions _proximitySensorManager];
-[SBHomeHardwareButtonActions _shouldIgnorePressesDueToProxOrIdle:];
-[SBHomeHardwareButtonActions configureForwardingToLockButtonActions:];
-[SBHomeHardwareButtonActions currentLongPressDuration];
-[SBHomeHardwareButtonActions initWitHomeButtonType:];
-[SBHomeHardwareButtonActions performDoublePressDownActions];
-[SBHomeHardwareButtonActions performDoubleTapUpActions];
-[SBHomeHardwareButtonActions performSinglePressUpActions];
-[SBHomeHardwareButtonActions performSinglePressUpActionsWithSourceType:];
-[SBHomeHardwareButtonActions performTriplePressUpActions];
-[SBHomeHardwareButtonActions setCurrentLongPressDuration:];
```
