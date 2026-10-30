# `_UIDragSetDownAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDragSetDownItemAnimationDelegate`
- 7 instance variables, 6 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"NSArray" _itemAnimations;
@"_UIGroupCompletion" _groupCompletion;
B _hasBegun;
@"UIView" _containerView;
@"CADisplayLink" _displayLink;
@"UIViewPropertyAnimator" _remainingItemsPropertyAnimator;
@"UIWindow" _coordinateContainerWindow;
```

## Properties

```
@property (T@"UIWindow",&,N,V_coordinateContainerWindow) coordinateContainerWindow;
@property (T@"UIView",R,N) containerView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDragSetDownAnimation canAnimateItems:forSource:policyDriven:];
+[_UIDragSetDownAnimation defaultDropAnimationForPlatterView:];
+[_UIDragSetDownAnimation defaultMultiItemAnimationForPlatterView:];
+[_UIDragSetDownAnimation defaultSetDownPropertyAnimator];
+[_UIDragSetDownAnimation defaultSingleItemAnimationForPlatterView:];
```

## Instance methods

```
-[_UIDragSetDownAnimation addCompletion:];
-[_UIDragSetDownAnimation begin];
-[_UIDragSetDownAnimation containerView];
-[_UIDragSetDownAnimation _allItemAnimationsCompleted];
-[_UIDragSetDownAnimation _targetLayerDescriptor];
-[_UIDragSetDownAnimation coordinateContainerWindow];
-[_UIDragSetDownAnimation dirtyTargetedDragPreviewForDragItem:];
-[_UIDragSetDownAnimation initWithVisibleDroppedItems:items:forSource:policyDriven:completion:];
-[_UIDragSetDownAnimation itemAnimationCompleted:];
-[_UIDragSetDownAnimation itemAnimationReachedTarget:];
-[_UIDragSetDownAnimation previewContainerAnimationDidCompleteForDragItem:];
-[_UIDragSetDownAnimation setCoordinateContainerWindow:];
-[_UIDragSetDownAnimation updateInFlightAnimationTick:];
-[_UIDragSetDownAnimation updateTargetedDragPreview:forDragItem:];
-[_UIDragSetDownAnimation updateVisibleDroppedItems:];
```
