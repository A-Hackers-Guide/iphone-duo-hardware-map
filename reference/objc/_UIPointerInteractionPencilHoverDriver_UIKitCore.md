# `_UIPointerInteractionPencilHoverDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPointerInteractionDriver`
- 4 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<_UIPointerInteractionDriverSink>" _sink;
@"_UIPointerInteractionHoverGestureRecognizer" _hoverGestureRecognizer;
{?="invalid"B} _flags;
@"UIView" _view;
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
-[_UIPointerInteractionPencilHoverDriver setView:];
-[_UIPointerInteractionPencilHoverDriver locationInView:];
-[_UIPointerInteractionPencilHoverDriver allowsUpdatesWhilePrimaryButtonIsPressed];
-[_UIPointerInteractionPencilHoverDriver invalidate];
-[_UIPointerInteractionPencilHoverDriver view];
-[_UIPointerInteractionPencilHoverDriver type];
-[_UIPointerInteractionPencilHoverDriver initWithSink:];
-[_UIPointerInteractionPencilHoverDriver _handleHoverGesture:];
-[_UIPointerInteractionPencilHoverDriver _updateHover:forced:];
-[_UIPointerInteractionPencilHoverDriver _uninstallFromView:];
-[_UIPointerInteractionPencilHoverDriver _installToView:];
-[_UIPointerInteractionPencilHoverDriver isActive];
```
