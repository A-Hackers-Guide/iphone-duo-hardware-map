# `UIScrollToDismissSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardMotionSupport`
- Protocols: `UIScrollViewIntersectionDelegate`
- 6 instance variables, 1 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollViewForTransition;
B _scrollViewShowsHorizontalScrollIndicator;
B _scrollViewTransitionFinishing;
@"BSSimpleAssertion" _interfaceAutorotationDisabledAssertion;
{CGPoint="x"d"y"d} _scrollViewTransitionPreviousPoint;
@"UIInputViewSetNotificationInfo" _scrollViewNotificationInfo;
```

## Properties

```
@property (TB,R,N) isFinishingDismissTransition;
```

## Instance methods

```
-[UIScrollToDismissSupport isFinishingDismissTransition];
-[UIScrollToDismissSupport setInterfaceAutorotationDisabled:forController:];
-[UIScrollToDismissSupport _updateKeyboardLayoutGuideForScrollTransitionWithSize:hostFrame:duration:];
-[UIScrollToDismissSupport updateScrollViewContentInsetBottom:];
-[UIScrollToDismissSupport _updateTrackingCoordinatorForScrollTransitionWithSize:hostFrame:duration:interactive:];
-[UIScrollToDismissSupport scrollView:didPanWithGesture:];
-[UIScrollToDismissSupport cancelNotificationsForMode:];
-[UIScrollToDismissSupport completedPlacementFrom:to:forController:];
-[UIScrollToDismissSupport hideScrollViewHorizontalScrollIndicator:];
-[UIScrollToDismissSupport completeKeyboardDismiss:withDuration:];
-[UIScrollToDismissSupport finishScrollViewTransition];
-[UIScrollToDismissSupport scrollView:didFinishPanGesture:];
-[UIScrollToDismissSupport finishScrollViewTransitionForController:];
-[UIScrollToDismissSupport addPaddingToFrame:inView:];
-[UIScrollToDismissSupport _infoForMatchMove];
```
