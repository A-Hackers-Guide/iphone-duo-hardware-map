# `_UISplitViewControllerAdaptiveLayoutTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitionCoordinator`, `UIViewControllerTransitionCoordinatorContext`
- 25 instance variables, 30 properties, 51 instance methods, 0 class methods

## Instance variables

```
animations;
completion;
interactionHandler;
suspendedDelegateUpdateColumns;
mutableViewControllersWithSuspendedAppearanceTransitions;
mutablePreviousLayoutSnapshotView;
hasStarted;
hasCompleted;
isCommitted;
isCoordinated;
@"_UISplitViewControllerAdaptiveTransitionLayout" mutableTransitionLayout;
@"<_UISplitViewControllerAdaptiveLayout>" mutablePreviousLayout;
@"<_UISplitViewControllerAdaptiveLayout>" mutableNewLayout;
? identifier;
transitionCoordinatorAnimations;
transitionCoordinatorCompletions;
transitionCoordinatorInteractionChanges;
@"UIView" mutableContainerView;
B mutableIsAnimated;
B mutableIsCancelled;
B mutableIsInteractive;
B mutableInitiallyInteractive;
d mutableInteractiveProgress;
d mutableCompletionVelocity;
d mutableTransitionDuration;
```

## Properties

```
@property (T@"_UISplitViewControllerAdaptiveTransitionLayout",N,&,VmutableTransitionLayout) mutableTransitionLayout;
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,&,VmutablePreviousLayout) mutablePreviousLayout;
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,&,VmutableNewLayout) mutableNewLayout;
@property (T@"NSString",N,R) identifier;
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,R) previousLayout;
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,R) newLayout;
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,R) currentLayout;
@property (T@"UIView",N,R) previousLayoutSnapshotView;
@property (T@"NSSet",N,R) viewControllersWithSuspendedAppearanceTransitions;
@property (T@"UIView",N,&,VmutableContainerView) mutableContainerView;
@property (TB,N,VmutableIsAnimated) mutableIsAnimated;
@property (TB,N,VmutableIsCancelled) mutableIsCancelled;
@property (TB,N,VmutableIsInteractive) mutableIsInteractive;
@property (TB,N,VmutableInitiallyInteractive) mutableInitiallyInteractive;
@property (Td,N,VmutableInteractiveProgress) mutableInteractiveProgress;
@property (Td,N,VmutableCompletionVelocity) mutableCompletionVelocity;
@property (Td,N,VmutableTransitionDuration) mutableTransitionDuration;
@property (TB,N,R) animated;
@property (Tq,N,R) presentationStyle;
@property (TB,N,R) initiallyInteractive;
@property (TB,N,R) isInterruptible;
@property (TB,N,R) interactive;
@property (TB,N,R) cancelled;
@property (Td,N,R) transitionDuration;
@property (Td,N,R) percentComplete;
@property (Td,N,R) completionVelocity;
@property (Tq,N,R) completionCurve;
@property (T@"UIView",N,R) containerView;
@property (T{CGAffineTransform=dddddd},N,R) targetTransform;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveLayoutTransition previousLayout];
-[_UISplitViewControllerAdaptiveLayoutTransition viewControllersWithSuspendedAppearanceTransitions];
-[_UISplitViewControllerAdaptiveLayoutTransition completionVelocity];
-[_UISplitViewControllerAdaptiveLayoutTransition initWithPreviousLayout:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableIsAnimated:];
-[_UISplitViewControllerAdaptiveLayoutTransition percentComplete];
-[_UISplitViewControllerAdaptiveLayoutTransition animateAlongsideTransitionInView:animation:completion:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableNewLayout:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableInitiallyInteractive:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableIsCancelled:];
-[_UISplitViewControllerAdaptiveLayoutTransition viewControllerForKey:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableInteractiveProgress:];
-[_UISplitViewControllerAdaptiveLayoutTransition animateAlongsideTransition:completion:];
-[_UISplitViewControllerAdaptiveLayoutTransition viewForKey:];
-[_UISplitViewControllerAdaptiveLayoutTransition identifier];
-[_UISplitViewControllerAdaptiveLayoutTransition mutablePreviousLayout];
-[_UISplitViewControllerAdaptiveLayoutTransition init];
-[_UISplitViewControllerAdaptiveLayoutTransition isAnimated];
-[_UISplitViewControllerAdaptiveLayoutTransition notifyWhenInteractionEndsUsingBlock:];
-[_UISplitViewControllerAdaptiveLayoutTransition initiallyInteractive];
-[_UISplitViewControllerAdaptiveLayoutTransition notifyWhenInteractionChangesUsingBlock:];
-[_UISplitViewControllerAdaptiveLayoutTransition isInteractive];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableCompletionVelocity];
-[_UISplitViewControllerAdaptiveLayoutTransition presentationStyle];
-[_UISplitViewControllerAdaptiveLayoutTransition isCancelled];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableCompletionVelocity:];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableContainerView];
-[_UISplitViewControllerAdaptiveLayoutTransition newLayout];
-[_UISplitViewControllerAdaptiveLayoutTransition transitionDuration];
-[_UISplitViewControllerAdaptiveLayoutTransition currentLayout];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableNewLayout];
-[_UISplitViewControllerAdaptiveLayoutTransition isInterruptible];
-[_UISplitViewControllerAdaptiveLayoutTransition hasSuspendedDelegateUpdatesForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableIsInteractive:];
-[_UISplitViewControllerAdaptiveLayoutTransition containerView];
-[_UISplitViewControllerAdaptiveLayoutTransition addViewControllerWithSuspendedAppearanceTransitions:];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableTransitionLayout];
-[_UISplitViewControllerAdaptiveLayoutTransition targetTransform];
-[_UISplitViewControllerAdaptiveLayoutTransition completionCurve];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableInteractiveProgress];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableIsInteractive];
-[_UISplitViewControllerAdaptiveLayoutTransition previousLayoutSnapshotView];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableContainerView:];
-[_UISplitViewControllerAdaptiveLayoutTransition description];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableIsAnimated];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableTransitionDuration];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableTransitionLayout:];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutableTransitionDuration:];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableIsCancelled];
-[_UISplitViewControllerAdaptiveLayoutTransition setMutablePreviousLayout:];
-[_UISplitViewControllerAdaptiveLayoutTransition mutableInitiallyInteractive];
```
