# `_UIDismissInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`
- 12 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
_view;
? delegate;
B isEnabled;
Q styles;
subInteractions;
trackingView;
_isActive;
trackingViewDidBecomeVisible;
originalTrackingViewPosition;
originalTouchPosition;
touchAdjustment;
translation;
```

## Properties

```
@property (T@"UIView",N,R) view;
@property (T@"<_UIDismissInteractionDelegate>",N,W,Vdelegate) delegate;
@property (TB,N,VisEnabled) isEnabled;
@property (TQ,N,Vstyles) styles;
@property (TB,N,R) isActive;
```

## Instance methods

```
-[_UIDismissInteraction setStyles:];
-[_UIDismissInteraction styles];
-[_UIDismissInteraction init];
-[_UIDismissInteraction setIsEnabled:];
-[_UIDismissInteraction isEnabled];
-[_UIDismissInteraction view];
-[_UIDismissInteraction setDelegate:];
-[_UIDismissInteraction willMoveToView:];
-[_UIDismissInteraction delegate];
-[_UIDismissInteraction isActive];
-[_UIDismissInteraction didMoveToView:];
```
