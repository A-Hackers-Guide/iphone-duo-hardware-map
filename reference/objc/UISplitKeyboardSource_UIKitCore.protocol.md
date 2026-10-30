# `UISplitKeyboardSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UIRemoteKeyboardViewSource`, `UIInputViewSetPlacementOwner`
- 0 instance variables, 7 properties, 17 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",R,N) view;
@property (TB,R,N) isChangingPlacement;
@property (T{CGPoint=dd},R,N) positionConstraintConstant;
@property (T@"UIViewController",R,N) _inputViewController;
@property (T@"UIInputViewSetPlacement",R,N) placement;
@property (T@"<UIInputViewSetPlacementApplicator>",R,N) applicator;
@property (TB,R,N) usesKeyboardState;
```

## Instance methods

```
-[UISplitKeyboardSource removeMatchMoveAnimationIfNeeded];
-[UISplitKeyboardSource draggableView];
-[UISplitKeyboardSource prepareForSplitTransition];
-[UISplitKeyboardSource isChangingPlacement];
-[UISplitKeyboardSource setInterfaceAutorotationDisabled:];
-[UISplitKeyboardSource _inputViewController];
-[UISplitKeyboardSource finishSplitTransition];
-[UISplitKeyboardSource placement];
-[UISplitKeyboardSource scrollTrackingView];
-[UISplitKeyboardSource positionConstraintConstant];
-[UISplitKeyboardSource trackingCoordinatorFrame];
-[UISplitKeyboardSource applicator];
-[UISplitKeyboardSource view];
-[UISplitKeyboardSource usesKeyboardState];
-[UISplitKeyboardSource offsetForSplitTransition];
-[UISplitKeyboardSource constructNotificationInfoForScrollWithMode:];
-[UISplitKeyboardSource isVisibleForScrollToDismiss];
```
