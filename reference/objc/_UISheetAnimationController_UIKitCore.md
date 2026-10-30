# `_UISheetAnimationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning_Internal`, `UIViewControllerAnimatedTransitioning`
- 14 instance variables, 26 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _isReversed;
B _isInInitialLayout;
@"UIView" _sourceView;
@"<UIViewControllerContextTransitioning>" _transitionContext;
@"UIView" _forwardView;
@"UIViewPropertyAnimator" _propertyAnimator;
@"_UISheetPresentationMetrics" _metrics;
@"NSMutableArray" _allNoninteractiveAnimations;
@"NSMutableArray" _allNoninteractiveCompletions;
@? _defaultSourceFrameProvider;
{CGPoint="x"d"y"d} _attachmentPoint;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _forwardViewFullFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _interactiveFrame;
```

## Properties

```
@property (T@"<UIViewControllerContextTransitioning>",W,N,V_transitionContext) transitionContext;
@property (TB,R,N) isForward;
@property (T@"UIView",&,N,V_forwardView) forwardView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_forwardViewFullFrame) forwardViewFullFrame;
@property (TB,N,V_isInInitialLayout) isInInitialLayout;
@property (T@"UIViewPropertyAnimator",&,N,V_propertyAnimator) propertyAnimator;
@property (T@"_UISheetPresentationMetrics",&,N,V_metrics) metrics;
@property (T@"NSMutableArray",&,N,V_allNoninteractiveAnimations) allNoninteractiveAnimations;
@property (T@"NSMutableArray",&,N,V_allNoninteractiveCompletions) allNoninteractiveCompletions;
@property (T@?,C,N,V_defaultSourceFrameProvider) defaultSourceFrameProvider;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_interactiveFrame) interactiveFrame;
@property (T{CGPoint=dd},N,V_attachmentPoint) attachmentPoint;
@property (TB,N,V_isReversed) isReversed;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceFrame) sourceFrame;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (T@?,C,N) noninteractiveAnimations;
@property (T@?,C,N) noninteractiveCompletion;
@property (Tq,?,R,N) _navigationBarTransitionVariant;
@property (T@"UIView",?,R,N) _navigationBarTransitionOverlay;
@property (TB,?,R,N) _shouldCrossFadeNavigationBarVisibility;
@property (TB,?,R,N) _shouldCrossFadeBottomBars;
@property (TB,?,R,N) _shouldAnimateBottomBarVisibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISheetAnimationController isReversed];
-[_UISheetAnimationController setMetrics:];
-[_UISheetAnimationController animateTransition:];
-[_UISheetAnimationController transitionDuration:];
-[_UISheetAnimationController transitionContext];
-[_UISheetAnimationController init];
-[_UISheetAnimationController setTransitionContext:];
-[_UISheetAnimationController interruptibleAnimatorForTransition:];
-[_UISheetAnimationController attachmentPoint];
-[_UISheetAnimationController setSourceView:];
-[_UISheetAnimationController metrics];
-[_UISheetAnimationController sourceView];
-[_UISheetAnimationController setAllNoninteractiveAnimations:];
-[_UISheetAnimationController setSourceFrame:];
-[_UISheetAnimationController setForwardView:];
-[_UISheetAnimationController _allowKeyboardToAnimateAlongside:];
-[_UISheetAnimationController addNoninteractiveAnimations:];
-[_UISheetAnimationController addNoninteractiveCompletion:];
-[_UISheetAnimationController allNoninteractiveAnimations];
-[_UISheetAnimationController allNoninteractiveCompletions];
-[_UISheetAnimationController defaultSourceFrameProvider];
-[_UISheetAnimationController forwardView];
-[_UISheetAnimationController forwardViewFullFrame];
-[_UISheetAnimationController interactiveFrame];
-[_UISheetAnimationController isForward];
-[_UISheetAnimationController isInInitialLayout];
-[_UISheetAnimationController layoutTransitionViews];
-[_UISheetAnimationController noninteractiveAnimations];
-[_UISheetAnimationController noninteractiveCompletion];
-[_UISheetAnimationController propertyAnimator];
-[_UISheetAnimationController runNoninteractiveAnimationsIfPossible];
-[_UISheetAnimationController setAllNoninteractiveCompletions:];
-[_UISheetAnimationController setAttachmentPoint:];
-[_UISheetAnimationController setDefaultSourceFrameProvider:];
-[_UISheetAnimationController setForwardViewFullFrame:];
-[_UISheetAnimationController setInteractiveFrame:];
-[_UISheetAnimationController setIsInInitialLayout:];
-[_UISheetAnimationController setIsReversed:];
-[_UISheetAnimationController setNoninteractiveAnimations:];
-[_UISheetAnimationController setNoninteractiveCompletion:];
-[_UISheetAnimationController setPropertyAnimator:];
-[_UISheetAnimationController sourceFrame];
```
