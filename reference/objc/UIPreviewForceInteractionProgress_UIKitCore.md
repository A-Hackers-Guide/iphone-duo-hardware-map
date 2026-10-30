# `UIPreviewForceInteractionProgress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInteractionProgress`
- Protocols: `_UIForceLevelClassifierDelegate`
- 12 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"_UITouchForceObservable" _observable;
q _targetState;
q _minimumState;
B _updateMinimumStateWithTargetState;
@"_UIForceLevelClassifier" _classifier;
@"NSObservation" _classifierObservation;
B _enteredMinimumState;
B _didEnd;
@"NSObservation" _progressObservation;
@"NSObservation" _targetStateUpdateObservation;
@"NSObservation" _gestureBeganObservation;
B _completesAtTargetState;
```

## Properties

```
@property (Tq,N,S_setTargetState:,V_targetState) _targetState;
@property (TB,N,S_setClassifierShouldRespectSystemGestureTouchFiltering:) _classifierShouldRespectSystemGestureTouchFiltering;
@property (TB,N,V_completesAtTargetState) completesAtTargetState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPreviewForceInteractionProgress didEnd];
-[UIPreviewForceInteractionProgress _classifierShouldRespectSystemGestureTouchFiltering];
-[UIPreviewForceInteractionProgress _forceLevelClassifier:currentForceLevelDidChange:];
-[UIPreviewForceInteractionProgress _forceLevelClassifierDidReset:];
-[UIPreviewForceInteractionProgress _gestureRecognizerBegan:];
-[UIPreviewForceInteractionProgress _initWithObservable:targetState:minimumRequiredState:];
-[UIPreviewForceInteractionProgress _initWithObservable:targetState:minimumRequiredState:useLinearClassifier:];
-[UIPreviewForceInteractionProgress _initWithView:targetState:minimumRequiredState:useLinearClassifier:];
-[UIPreviewForceInteractionProgress _installProgressObserver];
-[UIPreviewForceInteractionProgress _setClassifierShouldRespectSystemGestureTouchFiltering:];
-[UIPreviewForceInteractionProgress _setGestureBeginObservable:];
-[UIPreviewForceInteractionProgress _setTargetState:];
-[UIPreviewForceInteractionProgress _targetState];
-[UIPreviewForceInteractionProgress completesAtTargetState];
-[UIPreviewForceInteractionProgress enteredMinimumState];
-[UIPreviewForceInteractionProgress initWithGestureRecognizer:];
-[UIPreviewForceInteractionProgress initWithGestureRecognizer:minimumRequiredState:];
-[UIPreviewForceInteractionProgress initWithView:targetState:];
-[UIPreviewForceInteractionProgress initWithView:targetState:minimumRequiredState:];
-[UIPreviewForceInteractionProgress setCompletesAtTargetState:];
```
