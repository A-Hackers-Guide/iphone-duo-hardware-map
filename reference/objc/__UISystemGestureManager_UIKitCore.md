# `__UISystemGestureManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIExclusiveTouchGestureRecognizerDelegate`
- 15 instance variables, 13 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayIdentity" _displayIdentity;
@"_UISystemGestureWindow" _systemGestureWindow;
@"NSMutableSet" _recognizingGestures;
@"NSMutableSet" _externalEdgeSwipeGestures;
@"NSMutableSet" _internalGestures;
@"NSMutableSet" _externalGestures;
@"<BSInvalidatable>" _stateCaptureToken;
B _achievedMaximumMovement;
B _didSeeExclusiveTouchBegan;
B _didProcessPendingSwipeBegan;
@"UIGestureRecognizer" _exclusiveTouchGesture;
@"UIGestureRecognizer" _pendingSwipeGesture;
@"UIGestureRecognizer" _catchEdgeSwipeFailureGesture;
@"UIGestureRecognizer" _directTouchGesture;
@"BKSTouchStream" _touchStream;
```

## Properties

```
@property (T@"UIGestureRecognizer",&,N,V_exclusiveTouchGesture) exclusiveTouchGesture;
@property (T@"UIGestureRecognizer",&,N,V_pendingSwipeGesture) pendingSwipeGesture;
@property (T@"UIGestureRecognizer",&,N,V_catchEdgeSwipeFailureGesture) catchEdgeSwipeFailureGesture;
@property (T@"UIGestureRecognizer",&,N,V_directTouchGesture) directTouchGesture;
@property (TB,N,V_achievedMaximumMovement) achievedMaximumMovement;
@property (TB,N,V_didSeeExclusiveTouchBegan) didSeeExclusiveTouchBegan;
@property (TB,N,V_didProcessPendingSwipeBegan) didProcessPendingSwipeBegan;
@property (T@"BKSTouchStream",&,N,V_touchStream) touchStream;
@property (T@"NSSet",R,C,N) gestureRecognizers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__UISystemGestureManager _catchSwipeFailureGestureChanged:];
-[__UISystemGestureManager _exclusiveTouchGestureChanged:];
-[__UISystemGestureManager directTouchGesture];
-[__UISystemGestureManager gestureRecognizers];
-[__UISystemGestureManager gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[__UISystemGestureManager exclusiveTouchGestureRecognizer:achievedMaximumAbsoluteAccumulatedMovement:timestamp:];
-[__UISystemGestureManager addGestureRecognizer:recognitionEvent:];
-[__UISystemGestureManager addGestureRecognizer:];
-[__UISystemGestureManager achievedMaximumMovement];
-[__UISystemGestureManager initWithDisplayIdentity:];
-[__UISystemGestureManager catchEdgeSwipeFailureGesture];
-[__UISystemGestureManager _pendingSwipeGestureChanged:];
-[__UISystemGestureManager dealloc];
-[__UISystemGestureManager _removeInternalGestures];
-[__UISystemGestureManager setTransform:];
-[__UISystemGestureManager touchStream];
-[__UISystemGestureManager didProcessPendingSwipeBegan];
-[__UISystemGestureManager setDidSeeExclusiveTouchBegan:];
-[__UISystemGestureManager pendingSwipeGesture];
-[__UISystemGestureManager setDirectTouchGesture:];
-[__UISystemGestureManager setAchievedMaximumMovement:];
-[__UISystemGestureManager _pendingSwipeGestureDidTerminate:];
-[__UISystemGestureManager _exclusiveTouchGestureDidTerminate:];
-[__UISystemGestureManager removeGestureRecognizer:];
-[__UISystemGestureManager _externalGestureRecognizerChanged:];
-[__UISystemGestureManager setDidProcessPendingSwipeBegan:];
-[__UISystemGestureManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[__UISystemGestureManager windowForSystemGestures];
-[__UISystemGestureManager description];
-[__UISystemGestureManager setPendingSwipeGesture:];
-[__UISystemGestureManager setCatchEdgeSwipeFailureGesture:];
-[__UISystemGestureManager _directTouchDown:];
-[__UISystemGestureManager _pendingSwipeGestureDidBegin:];
-[__UISystemGestureManager exclusiveTouchGesture];
-[__UISystemGestureManager _handleTooMuchMovementWithLastTouchTimestamp:];
-[__UISystemGestureManager setExclusiveTouchGesture:];
-[__UISystemGestureManager clearTransform];
-[__UISystemGestureManager _addInternalGesturesToView:];
-[__UISystemGestureManager _dispatchModeForExternalGestureCompletion];
-[__UISystemGestureManager _failedPendingSwipe];
-[__UISystemGestureManager didSeeExclusiveTouchBegan];
-[__UISystemGestureManager setTouchStream:];
```
