# `_UIPageCurlState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITransitionState`
- Protocols: `CAAnimationDelegate`
- 13 instance variables, 14 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"_UIPageCurl" _pageCurl;
q _curlType;
{CGPoint="x"d"y"d} _initialLocation;
{CGPoint="x"d"y"d} _referenceLocation;
@"UIView" _frontPageView;
@"UIView" _backPageView;
@"UIView" _frontView;
@"UIView" _backView;
q _completionCount;
q _curlState;
B _finished;
B _willComplete;
@? _finally;
```

## Properties

```
@property (T@"_UIPageCurl",R,N,V_pageCurl) pageCurl;
@property (Tq,R,N,V_curlType) curlType;
@property (T{CGPoint=dd},R,N,V_initialLocation) initialLocation;
@property (T{CGPoint=dd},R,N,V_referenceLocation) referenceLocation;
@property (T@"UIView",R,N) frontPageView;
@property (T@"UIView",R,N) backPageView;
@property (T@"UIView",R,N,V_frontView) frontView;
@property (T@"UIView",R,N,V_backView) backView;
@property (Tq,R,N,V_curlState) curlState;
@property (TB,R,N,GhasPendingAnimations) pendingAnimations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPageCurlState cleanup];
-[_UIPageCurlState animationDidStop:finished:];
-[_UIPageCurlState initialLocation];
-[_UIPageCurlState dealloc];
-[_UIPageCurlState referenceLocation];
-[_UIPageCurlState backView];
-[_UIPageCurlState finally];
-[_UIPageCurlState _effectiveTransitionDirection];
-[_UIPageCurlState _pageViewFrame];
-[_UIPageCurlState addBackPageContent];
-[_UIPageCurlState addFrontPageContent];
-[_UIPageCurlState backPageView];
-[_UIPageCurlState cleanupWithFinishedState:completedState:];
-[_UIPageCurlState curlState];
-[_UIPageCurlState curlType];
-[_UIPageCurlState frontPageView];
-[_UIPageCurlState frontView];
-[_UIPageCurlState hasPendingAnimations];
-[_UIPageCurlState incrementCompletionCount];
-[_UIPageCurlState initWithPageCurl:andCurlType:fromLocation:withReferenceLocation:inDirection:withView:revealingView:completion:finally:];
-[_UIPageCurlState invalidatePageCurl];
-[_UIPageCurlState isCompatibleWithCurlOfType:inDirection:];
-[_UIPageCurlState pageCurl];
-[_UIPageCurlState setCurlState:willComplete:];
```
