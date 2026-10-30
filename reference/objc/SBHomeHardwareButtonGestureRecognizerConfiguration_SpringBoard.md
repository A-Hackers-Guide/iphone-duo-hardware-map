# `SBHomeHardwareButtonGestureRecognizerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBSystemGestureManager" _systemGestureManager;
@"UIHBClickGestureRecognizer" _initialButtonDownGestureRecognizer;
@"UIHBClickGestureRecognizer" _initialButtonUpGestureRecognizer;
@"UIHBClickGestureRecognizer" _singlePressUpGestureRecognizer;
@"UIHBClickGestureRecognizer" _acceleratedSinglePressUpGestureRecognizer;
@"UIHBLongClickGestureRecognizer" _longPressGestureRecognizer;
@"UIHBClickGestureRecognizer" _doublePressDownGestureRecognizer;
@"UIHBClickGestureRecognizer" _doublePressUpGestureRecognizer;
@"UIHBClickGestureRecognizer" _triplePressUpGestureRecognizer;
@"UIHBClickGestureRecognizer" _doubleTapUpGestureRecognizer;
```

## Properties

```
@property (T@"SBSystemGestureManager",&,N,V_systemGestureManager) systemGestureManager;
@property (T@"UIHBClickGestureRecognizer",&,N,V_initialButtonDownGestureRecognizer) initialButtonDownGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_initialButtonUpGestureRecognizer) initialButtonUpGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_singlePressUpGestureRecognizer) singlePressUpGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_acceleratedSinglePressUpGestureRecognizer) acceleratedSinglePressUpGestureRecognizer;
@property (T@"UIHBLongClickGestureRecognizer",&,N,V_longPressGestureRecognizer) longPressGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_doublePressDownGestureRecognizer) doublePressDownGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_doublePressUpGestureRecognizer) doublePressUpGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_triplePressUpGestureRecognizer) triplePressUpGestureRecognizer;
@property (T@"UIHBClickGestureRecognizer",&,N,V_doubleTapUpGestureRecognizer) doubleTapUpGestureRecognizer;
@property (TB,R,N) shouldConfigureDependencies;
@property (T@"NSArray",R,N) allGestureRecognizers;
```

## Instance methods

```
-[SBHomeHardwareButtonGestureRecognizerConfiguration setSystemGestureManager:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration longPressGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration systemGestureManager];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setLongPressGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration acceleratedSinglePressUpGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration allGestureRecognizers];
-[SBHomeHardwareButtonGestureRecognizerConfiguration doublePressDownGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration doublePressUpGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration doubleTapUpGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration initialButtonDownGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration initialButtonUpGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setAcceleratedSinglePressUpGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setDoublePressDownGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setDoublePressUpGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setDoubleTapUpGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setInitialButtonDownGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setInitialButtonUpGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setSinglePressUpGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration setTriplePressUpGestureRecognizer:];
-[SBHomeHardwareButtonGestureRecognizerConfiguration shouldConfigureDependencies];
-[SBHomeHardwareButtonGestureRecognizerConfiguration singlePressUpGestureRecognizer];
-[SBHomeHardwareButtonGestureRecognizerConfiguration triplePressUpGestureRecognizer];
```
