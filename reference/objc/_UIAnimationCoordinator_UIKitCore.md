# `_UIAnimationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 11 instance variables, 14 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _stash;
@"_UIViewControllerOneToOneTransitionContext" _transitionContext;
@"UIPercentDrivenInteractiveTransition" _interactiveTransition;
d _duration;
@? _preperation;
@? _animator;
@? _completion;
@"UIView" _containerView;
@"UIViewController" _viewController;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endFrame;
```

## Properties

```
@property (T@"_UIViewControllerOneToOneTransitionContext",R,&,N) transitionContext;
@property (Td,N,V_duration) duration;
@property (T@?,C,N,V_preperation) preperation;
@property (T@?,C,N,V_animator) animator;
@property (T@?,C,N,V_completion) completion;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIViewController",&,N,V_viewController) viewController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_startFrame) startFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_endFrame) endFrame;
@property (T@"NSMutableDictionary",R,&,N) stash;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIAnimationCoordinator setCompletion:];
-[_UIAnimationCoordinator setViewController:];
-[_UIAnimationCoordinator setContainerView:];
-[_UIAnimationCoordinator completion];
-[_UIAnimationCoordinator endFrame];
-[_UIAnimationCoordinator animateTransition:];
-[_UIAnimationCoordinator transitionDuration:];
-[_UIAnimationCoordinator transitionContext];
-[_UIAnimationCoordinator dealloc];
-[_UIAnimationCoordinator setEndFrame:];
-[_UIAnimationCoordinator setAnimator:];
-[_UIAnimationCoordinator animator];
-[_UIAnimationCoordinator animationEnded:];
-[_UIAnimationCoordinator duration];
-[_UIAnimationCoordinator viewController];
-[_UIAnimationCoordinator containerView];
-[_UIAnimationCoordinator startFrame];
-[_UIAnimationCoordinator animate];
-[_UIAnimationCoordinator setDuration:];
-[_UIAnimationCoordinator setPreperation:];
-[_UIAnimationCoordinator _updateTransitionContext];
-[_UIAnimationCoordinator animateInteractively];
-[_UIAnimationCoordinator cancelInteractiveAnimation];
-[_UIAnimationCoordinator finishInteractiveAnimation];
-[_UIAnimationCoordinator preperation];
-[_UIAnimationCoordinator setStartFrame:];
-[_UIAnimationCoordinator stash];
-[_UIAnimationCoordinator updateInteractiveProgress:];
```
