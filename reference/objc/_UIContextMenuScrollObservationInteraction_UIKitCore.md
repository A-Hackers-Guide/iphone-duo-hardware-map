# `_UIContextMenuScrollObservationInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScrollViewScrollableAncestor`, `UIInteraction`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _currentTranslation;
{CGPoint="x"d"y"d} _consumedTranslation;
{CGPoint="x"d"y"d} _currentLocation;
B _isActive;
@"UIView" _view;
@"<_UIContextMenuScrollObservationInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIContextMenuScrollObservationInteractionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[_UIContextMenuScrollObservationInteraction interactionWithDelegate:];
```

## Instance methods

```
-[_UIContextMenuScrollObservationInteraction _descendentScrollView:shouldPreserveStartOffset:];
-[_UIContextMenuScrollObservationInteraction _descendentScrollViewShouldScrollVertically:];
-[_UIContextMenuScrollObservationInteraction view];
-[_UIContextMenuScrollObservationInteraction _descendentScrollViewDidEndDragging:];
-[_UIContextMenuScrollObservationInteraction setDelegate:];
-[_UIContextMenuScrollObservationInteraction _shouldBeFoundByDescendentScrollView:];
-[_UIContextMenuScrollObservationInteraction _scrollView:adjustedUnconstrainedOffsetForUnconstrainedOffset:startOffset:horizontalVelocity:verticalVelocity:animator:];
-[_UIContextMenuScrollObservationInteraction willMoveToView:];
-[_UIContextMenuScrollObservationInteraction _descendentScrollViewShouldMaintainRelativeDistanceFromSafeArea:];
-[_UIContextMenuScrollObservationInteraction delegate];
-[_UIContextMenuScrollObservationInteraction _descendentScrollViewDidCancelDragging:];
-[_UIContextMenuScrollObservationInteraction _descendentScrollViewShouldScrollHorizontally:];
-[_UIContextMenuScrollObservationInteraction didMoveToView:];
-[_UIContextMenuScrollObservationInteraction _endInteractionWithTranslation:location:];
```
