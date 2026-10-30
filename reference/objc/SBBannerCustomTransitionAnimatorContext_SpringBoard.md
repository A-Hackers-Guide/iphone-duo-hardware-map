# `SBBannerCustomTransitionAnimatorContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _presentationTransition;
@"<UIViewControllerContextTransitioning>" _transitionContext;
```

## Properties

```
@property (T@"<UIViewControllerContextTransitioning>",&,N,V_transitionContext) transitionContext;
@property (TB,N,GisPresentationTransition,V_presentationTransition) presentationTransition;
@property (T@"UIView",R,N) transitionView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) initialFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) initialContentFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) finalFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) finalContentFrame;
```

## Instance methods

```
-[SBBannerCustomTransitionAnimatorContext transitionContext];
-[SBBannerCustomTransitionAnimatorContext setTransitionContext:];
-[SBBannerCustomTransitionAnimatorContext transitionView];
-[SBBannerCustomTransitionAnimatorContext finalFrame];
-[SBBannerCustomTransitionAnimatorContext initialFrame];
-[SBBannerCustomTransitionAnimatorContext targetViewController];
-[SBBannerCustomTransitionAnimatorContext setPresentationTransition:];
-[SBBannerCustomTransitionAnimatorContext finalContentFrame];
-[SBBannerCustomTransitionAnimatorContext initialContentFrame];
-[SBBannerCustomTransitionAnimatorContext isPresentationTransition];
```
