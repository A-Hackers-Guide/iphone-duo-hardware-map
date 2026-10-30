# `SBUIFullscreenAnimationView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<SBUIFullscreenAnimationViewDelegate>" _delegate;
B _animating;
```

## Properties

```
@property (T@"<SBUIFullscreenAnimationViewDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,V_animating) animating;
```

## Instance methods

```
-[SBUIFullscreenAnimationView beginTransition];
-[SBUIFullscreenAnimationView animating];
-[SBUIFullscreenAnimationView _animationEnded];
-[SBUIFullscreenAnimationView setToView:];
-[SBUIFullscreenAnimationView setDelegate:];
-[SBUIFullscreenAnimationView endTransition];
-[SBUIFullscreenAnimationView delegate];
-[SBUIFullscreenAnimationView setFromView:];
-[SBUIFullscreenAnimationView _animationBegan];
-[SBUIFullscreenAnimationView _notifyDelegateAnimationBeganWithDuration:delay:];
-[SBUIFullscreenAnimationView _notifyDelegateThatAnimationIsDone];
```
