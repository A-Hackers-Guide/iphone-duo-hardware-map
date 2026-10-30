# `PKPencilObserverInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKHoverControllerDelegate`, `PKPencilObserverGestureRecognizerDelegate`, `UIPencilInteractionDelegate`, `UIInteraction`
- 14 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
{vector<PKInputPoint, std::allocator<PKInputPoint>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _inputPoints;
B _wantsShadowView;
B _isCheckingIfRollIsSupported;
@"<PKPencilObserverInteractionDelegate>" _delegate;
@"PKPencilShadowView" _shadowView;
@"PKPencilStatisticsManager" _statisticsManager;
@"PKHoverController" _hoverController;
@"PKPencilObserverGestureRecognizer" _pencilObserver;
d _timestampForHoverBegan;
d _timestampForPencilObserverBegan;
d _previousActivePencilMinuteTimestamp;
@"UIPencilInteraction" _pencilInteraction;
@"UIView" _view;
{CGPoint="x"d"y"d} _currentLocation;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPencilObserverInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[PKPencilObserverInteraction gestureRecognizer:shouldReceiveTouch:];
-[PKPencilObserverInteraction sceneDidEnterBackground:];
-[PKPencilObserverInteraction setView:];
-[PKPencilObserverInteraction view];
-[PKPencilObserverInteraction willMoveToView:];
-[PKPencilObserverInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[PKPencilObserverInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[PKPencilObserverInteraction didMoveToView:];
-[PKPencilObserverInteraction pencilInteractionDidTap:];
-[PKPencilObserverInteraction pencilObserver:didBeginAtPoint:];
-[PKPencilObserverInteraction hidePencilShadowViewIfNecessary];
-[PKPencilObserverInteraction hoverController:didBegin:];
-[PKPencilObserverInteraction hoverController:didUpdate:];
-[PKPencilObserverInteraction hoverController:intentionalHoverWithDuration:];
-[PKPencilObserverInteraction hoverControllerDidEnd:fromTouch:];
-[PKPencilObserverInteraction pencilObserver:didMoveToPoint:];
-[PKPencilObserverInteraction pencilObserverDidEnd:];
```
