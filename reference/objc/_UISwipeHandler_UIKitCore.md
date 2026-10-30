# `_UISwipeHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UISwipeDismissalGestureRecognizerDelegate`
- 11 instance variables, 10 properties, 30 instance methods, 0 class methods

## Instance variables

```
{?="didProcessBegan"b1"beganSuccessfully"b1} _flags;
@"_UISwipeDismissalGestureRecognizer" _dismissalGestureRecognizer;
@"_UISwipeActionPanGestureRecognizer" _swipeActionPanRecognizer;
{?="direction"Q"primaryActionIsDestructive"B"primaryActionCanBeTriggeredBySwipe"B"openThreshold"d"confirmationThreshold"d} _currentSwipeConfig;
Q _currentSwipeState;
B _resetSwipeWhileInitiating;
d _initialTranslation;
d _confirmationTranslationAdjustment;
B _active;
@"_UIStatesFeedbackGenerator" _swipeFeedbackGenerator;
@"UISwipeActionController" _swipeController;
```

## Properties

```
@property (T@"UISwipeActionController",W,N,V_swipeController) swipeController;
@property (T{?=QBBdd},R,N) currentSwipeConfig;
@property (TQ,R,N,V_currentSwipeState) currentSwipeState;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_swipeFeedbackGenerator) swipeFeedbackGenerator;
@property (TB,N,GisActive,V_active) active;
@property (TB,R,N,GisInteracting) interacting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISwipeHandler gestureRecognizerShouldDismissForTouchDown:];
-[_UISwipeHandler _swipeRecognizerEnded:wasCancelled:];
-[_UISwipeHandler swipeFeedbackGenerator];
-[_UISwipeHandler _swipeRecognizerBegan:];
-[_UISwipeHandler _directionForGestureRecognizer:];
-[_UISwipeHandler setSwipeFeedbackGenerator:];
-[_UISwipeHandler _cancelExistingSwipe];
-[_UISwipeHandler updateCurrentSwipeConfig:];
-[_UISwipeHandler dealloc];
-[_UISwipeHandler _swipeRecognizerDidRecognize:];
-[_UISwipeHandler _cancelExistingSwipeForGestureBeganIfNecessary:];
-[_UISwipeHandler _dismissalRecognizerDidRecognize:];
-[_UISwipeHandler setActive:];
-[_UISwipeHandler _swipeRecognizerChanged:];
-[_UISwipeHandler _delegateWantsToDismissOnTouchDownForGestureRecognizer:];
-[_UISwipeHandler isInteracting];
-[_UISwipeHandler gestureRecognizerShouldBegin:];
-[_UISwipeHandler gestureRecognizerShouldDismissForTouchUp:];
-[_UISwipeHandler setSwipeController:];
-[_UISwipeHandler resetSwipe];
-[_UISwipeHandler gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UISwipeHandler currentSwipeConfig];
-[_UISwipeHandler initWithSwipeController:];
-[_UISwipeHandler initiateSwipeWithDirection:configuration:location:userInitiated:];
-[_UISwipeHandler isActive];
-[_UISwipeHandler swipeController];
-[_UISwipeHandler _moveSwipedItemToOffset:animated:usingSpringWithStiffness:isTracking:];
-[_UISwipeHandler currentSwipeState];
-[_UISwipeHandler _currentSwipeInfoWithTargetOffset:animated:usingSpringWithStiffness:];
-[_UISwipeHandler _setUp];
```
