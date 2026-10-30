# `UIViewControllerContextTransitioning` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",R,N) containerView;
@property (TB,R,N,GisAnimated) animated;
@property (TB,R,N,GisInteractive) interactive;
@property (TB,R,N) transitionWasCancelled;
@property (Tq,R,N) presentationStyle;
@property (T{CGAffineTransform=dddddd},R,N) targetTransform;
```

## Instance methods

```
-[UIViewControllerContextTransitioning updateInteractiveTransition:];
-[UIViewControllerContextTransitioning viewControllerForKey:];
-[UIViewControllerContextTransitioning viewForKey:];
-[UIViewControllerContextTransitioning isAnimated];
-[UIViewControllerContextTransitioning finalFrameForViewController:];
-[UIViewControllerContextTransitioning transitionWasCancelled];
-[UIViewControllerContextTransitioning completeTransition:];
-[UIViewControllerContextTransitioning isInteractive];
-[UIViewControllerContextTransitioning presentationStyle];
-[UIViewControllerContextTransitioning initialFrameForViewController:];
-[UIViewControllerContextTransitioning cancelInteractiveTransition];
-[UIViewControllerContextTransitioning pauseInteractiveTransition];
-[UIViewControllerContextTransitioning containerView];
-[UIViewControllerContextTransitioning finishInteractiveTransition];
-[UIViewControllerContextTransitioning targetTransform];
```
