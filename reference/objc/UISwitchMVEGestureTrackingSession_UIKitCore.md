# `UISwitchMVEGestureTrackingSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _displayedOnValue;
B _pendingDisplayedOnValue;
B _lastCommitedOnValue;
@"UIView<UISwitchMVEGestureTrackingSessionElement>" _visualElement;
d _naturalLayoutDirection;
d _movementVectorForPanInitiatedChangeY;
d _movementVectorForPanInitiatedChangeTargetOnValue;
@"UIGestureRecognizer" _pendingDisplayedOnValueInitiatingGesture;
```

## Properties

```
@property (Td,R,N,V_naturalLayoutDirection) naturalLayoutDirection;
@property (Td,R,N,V_movementVectorForPanInitiatedChangeY) movementVectorForPanInitiatedChangeY;
@property (Td,R,N,V_movementVectorForPanInitiatedChangeTargetOnValue) movementVectorForPanInitiatedChangeTargetOnValue;
@property (T@"UIGestureRecognizer",R,N,V_pendingDisplayedOnValueInitiatingGesture) pendingDisplayedOnValueInitiatingGesture;
@property (TB,R,N,V_pendingDisplayedOnValue) pendingDisplayedOnValue;
@property (TB,R,N,V_lastCommitedOnValue) lastCommitedOnValue;
@property (T@"UIView<UISwitchMVEGestureTrackingSessionElement>",W,N,V_visualElement) visualElement;
@property (TB,N,V_displayedOnValue) displayedOnValue;
```

## Class methods

```
+[UISwitchMVEGestureTrackingSession gestureIsInEndState:];
```

## Instance methods

```
-[UISwitchMVEGestureTrackingSession reset];
-[UISwitchMVEGestureTrackingSession _applyPendingChangesIfNecessary];
-[UISwitchMVEGestureTrackingSession _isMovementDirectionAndMagnitudeEnoughToPerformOnOffChange:];
-[UISwitchMVEGestureTrackingSession _isMovementDirectionTrackableForPossibleOnOffChange:];
-[UISwitchMVEGestureTrackingSession _sendStateChangeActionsIfNecessary];
-[UISwitchMVEGestureTrackingSession _updateMovementVectorForPanInitiatedChanges];
-[UISwitchMVEGestureTrackingSession applyPendingDisplayedOnValueAndSendActions];
-[UISwitchMVEGestureTrackingSession applyPendingDisplayedOnValueWithoutSendingActions];
-[UISwitchMVEGestureTrackingSession canApplyPendingOnValueForGesture:];
-[UISwitchMVEGestureTrackingSession displayedOnValue];
-[UISwitchMVEGestureTrackingSession initWithVisualElement:];
-[UISwitchMVEGestureTrackingSession invalidatePendingOnValue];
-[UISwitchMVEGestureTrackingSession lastCommitedOnValue];
-[UISwitchMVEGestureTrackingSession movementVectorForPanInitiatedChangeTargetOnValue];
-[UISwitchMVEGestureTrackingSession movementVectorForPanInitiatedChangeY];
-[UISwitchMVEGestureTrackingSession naturalLayoutDirection];
-[UISwitchMVEGestureTrackingSession pendingDisplayedOnValue];
-[UISwitchMVEGestureTrackingSession pendingDisplayedOnValueInitiatingGesture];
-[UISwitchMVEGestureTrackingSession pendingDisplayedOnValueIsValid];
-[UISwitchMVEGestureTrackingSession setDisplayedOnValue:];
-[UISwitchMVEGestureTrackingSession setPendingDisplayedOnValue:forGesture:];
-[UISwitchMVEGestureTrackingSession setVisualElement:];
-[UISwitchMVEGestureTrackingSession updatePendingDisplayedOnValueIfMovementIsEnoughToInitiateChange:forGesture:];
-[UISwitchMVEGestureTrackingSession visualElement];
```
