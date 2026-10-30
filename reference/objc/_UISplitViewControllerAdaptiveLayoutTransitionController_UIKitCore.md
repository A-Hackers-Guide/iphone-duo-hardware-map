# `_UISplitViewControllerAdaptiveLayoutTransitionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 31 instance methods, 0 class methods

## Instance variables

```
mutablePreviousLayout;
mutableScheduledTransition;
mutableInteractiveTransition;
mutableUpcomingTransition;
updates;
```

## Properties

```
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,R) previousLayout;
@property (T@"_UISplitViewControllerAdaptiveLayoutTransition",N,R) scheduledTransition;
@property (T@"_UISplitViewControllerAdaptiveLayoutTransition",N,R) currentTransition;
@property (T@"<UIViewControllerTransitionCoordinator>",N,R) transitionCoordinator;
@property (T@"_UISplitViewControllerAdaptiveLayoutTransition",N,R) upcomingTransition;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveLayoutTransitionController transitionCoordinator];
-[_UISplitViewControllerAdaptiveLayoutTransitionController previousLayout];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleTransitionVelocity:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleSplitViewControllerColumnModeWillChangeHandler:didChangeHandler:splitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController init];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleTransitionToLayout:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController performWithTransition:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController beginTransitionAnimated:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleSnapshot:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController beginTransitionAlongsideTransitionCoordinator:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController currentTransition];
-[_UISplitViewControllerAdaptiveLayoutTransitionController upcomingTransition];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleCompletion:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleInteractionHandler:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController updateInteractiveTransitionWithProgress:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleTransition];
-[_UISplitViewControllerAdaptiveLayoutTransitionController startWithTransition:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleContainerView:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController commitWithTransition:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduledTransition];
-[_UISplitViewControllerAdaptiveLayoutTransitionController completeWithTransition:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleDisplayModeWillChangeHandler:didChangeHandler:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController beginInteractiveTransition];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleSplitViewControllerColumnVisibilityWillChangeHandler:didChangeHandler:splitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleCollapsedWillChangeHandler:didChangeHandler:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleAnimations:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleSplitViewControllerColumnSizeWillChangeHandler:didChangeHandler:splitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController animateWithTransition:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController endInteractiveTransition:velocity:animated:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController scheduleSplitViewControllerColumnSuspendingDelegateUpdates:];
-[_UISplitViewControllerAdaptiveLayoutTransitionController defaultAnimationWithAnimations:initialSpringVelocity:completion:];
```
