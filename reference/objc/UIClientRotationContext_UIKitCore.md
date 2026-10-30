# `UIClientRotationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIView" _headerView;
@"UIView" _footerView;
@"UIView" _contentView;
@"UIView" _snapshotTargetView;
@"UIView" _rotatingSnapshotView;
@"UIView" _footerStartSnapshotView;
@"UIView" _footerEndSnapshotView;
B _headerWasHidden;
B _footerWasHidden;
B _contentWasHidden;
B _snapshotTargetWasHidden;
B _orderKeyboardInAfterRotating;
q _fromOrientation;
q _toOrientation;
d _duration;
@"UISnapshotView" _headerSnapshotViewStart;
@"UISnapshotView" _footerSnapshotViewStart;
@"UISnapshotView" _contentSnapshotViewStart;
@ _rotatingClient;
{?="animateContentRotation"B"preserveHeight"B"avoidFadingBottomOfContent"B"skipSnapshotOfEndState"B"preventAdditveAnimations"B"contentStretchRightEdgeInset"d"edgeClip"i} _rotationSettings;
d contentBottomInset;
@"UIWindow" _window;
B _skipClientRotationCallbacks;
```

## Properties

```
@property (T@,R,N,V_rotatingClient) rotatingClient;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (Td,R,N,V_duration) duration;
@property (TB,N,V_skipClientRotationCallbacks) skipClientRotationCallbacks;
@property (Tq,R,N,V_fromOrientation) fromOrientation;
@property (Tq,R,N,V_toOrientation) toOrientation;
```

## Instance methods

```
-[UIClientRotationContext dealloc];
-[UIClientRotationContext duration];
-[UIClientRotationContext contentView];
-[UIClientRotationContext fromOrientation];
-[UIClientRotationContext rotateSnapshots];
-[UIClientRotationContext setSkipClientRotationCallbacks:];
-[UIClientRotationContext _isFooterTranslucent];
-[UIClientRotationContext _isHeaderTranslucent];
-[UIClientRotationContext _positionHeaderView:andFooterView:outsideContentViewForInterfaceOrientation:];
-[UIClientRotationContext _slideHeaderView:andFooterView:offScreen:forInterfaceOrientation:];
-[UIClientRotationContext finishFirstHalfRotation];
-[UIClientRotationContext finishFullRotateUsingOnePartAnimation:];
-[UIClientRotationContext initWithClient:toOrientation:duration:andWindow:];
-[UIClientRotationContext rotatingClient];
-[UIClientRotationContext setupRotationOrderingKeyboardInAfterRotation:];
-[UIClientRotationContext skipClientRotationCallbacks];
-[UIClientRotationContext slideHeaderViewAndFooterViewOffScreen:forInterfaceOrientation:];
-[UIClientRotationContext toOrientation];
```
