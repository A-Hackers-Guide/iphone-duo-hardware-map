# `_UIPointerInteractionHoverDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIPointerInteractionDriver`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<_UIPointerInteractionDriverSink>" _sink;
@"_UIPointerInteractionHoverGestureRecognizer" _hoverGestureRecognizer;
@"_UIPointerInteractionPressGestureRecognizer" _pressGestureRecognizer;
{?="invalid"B"receivedUpdateWhilePointerDisabled"B"observing"B} _flags;
@"UIView" _view;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",W,N,V_view) view;
```

## Instance methods

```
-[_UIPointerInteractionHoverDriver gestureRecognizer:shouldReceiveTouch:];
-[_UIPointerInteractionHoverDriver _handlePressGesture:];
-[_UIPointerInteractionHoverDriver setView:];
-[_UIPointerInteractionHoverDriver locationInView:];
-[_UIPointerInteractionHoverDriver allowsUpdatesWhilePrimaryButtonIsPressed];
-[_UIPointerInteractionHoverDriver _currentTouchForce];
-[_UIPointerInteractionHoverDriver invalidate];
-[_UIPointerInteractionHoverDriver view];
-[_UIPointerInteractionHoverDriver type];
-[_UIPointerInteractionHoverDriver _trackpadFingerDownCount];
-[_UIPointerInteractionHoverDriver initWithSink:];
-[_UIPointerInteractionHoverDriver _pointerStateDidChange:];
-[_UIPointerInteractionHoverDriver _currentButtonMask];
-[_UIPointerInteractionHoverDriver _handleHoverGesture:];
-[_UIPointerInteractionHoverDriver _updateHover:forced:];
-[_UIPointerInteractionHoverDriver _uninstallFromView:];
-[_UIPointerInteractionHoverDriver _installToView:];
-[_UIPointerInteractionHoverDriver isActive];
```
