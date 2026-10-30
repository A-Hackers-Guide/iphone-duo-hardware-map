# `_UINavigationBarTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UINavigationBarTransitionContextProtocol`
- 23 instance variables, 34 properties, 77 instance methods, 3 class methods

## Instance variables

```
@"UINavigationBar" _navigationBar;
@"_UINavigationBarItemStack" _stack;
@"_UINavigationBarModernPromptView" _promptView;
@"_UINavigationBarContentView" _contentView;
@"_UIBarBackground" _backgroundView;
@"_UINavigationBarLargeTitleView" _largeTitleView;
@"UIView" _tabBarHostedView;
@"UIView" _transitionOverlayView;
@"_UINavigationBarLayout" _fromLayout;
@"_UINavigationBarLayout" _toLayout;
@"_UINavigationBarContentViewLayout" _fromContentLayout;
@"_UINavigationBarContentViewLayout" _toContentLayout;
@"_UINavigationBarLargeTitleViewLayout" _fromLargeTitleLayout;
@"_UINavigationBarLargeTitleViewLayout" _toLargeTitleLayout;
d _backgroundAlpha;
d _twoPartAnimationBaseDuration;
d _twoPartAnimationOverlapDuration;
q _largeTitleTransitionType;
q _apiVersion;
{?="isPushOperation"b1"isRTL"b1"compact"b1"allowLargeTitles"b1"twoPart"b1"beginWithLargeTitle"b1"endWithLargeTitle"b1"observedScrollViewOffsetIsApplicable"b1"sharesContentViewLayouts"b1"beginWithTransparencyAllowed"b1"endWithTransparencyAllowed"b1"usesBarBackground"b1} _flags;
@"NSMutableSet" _clippingViews;
@? _completionHandler;
{CGPoint="x"d"y"d} _startingContentOffsetForObservedScrollView;
```

## Properties

```
@property (Tq,R,D,N) transition;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"UINavigationBar",N,V_navigationBar) navigationBar;
@property (T@"_UINavigationBarItemStack",&,N,V_stack) stack;
@property (TB,N,SsetRTL:) isRTL;
@property (TB,N,SsetPushOperation:) isPushOperation;
@property (TB,N) compact;
@property (TB,N) allowLargeTitles;
@property (TB,N) twoPart;
@property (Tq,N,V_apiVersion) apiVersion;
@property (Td,N,V_backgroundAlpha) backgroundAlpha;
@property (T@"_UINavigationBarModernPromptView",&,N,V_promptView) promptView;
@property (T@"_UINavigationBarContentView",&,N,V_contentView) contentView;
@property (T@"_UIBarBackground",R,N,V_backgroundView) backgroundView;
@property (T@"_UINavigationBarLargeTitleView",&,N,V_largeTitleView) largeTitleView;
@property (T@"UIView",&,N,V_tabBarHostedView) tabBarHostedView;
@property (T@"UIView",R,N) viewFadingInFromCustomAlpha;
@property (T@"UIView",R,N) viewUsingEaseInCurve;
@property (TB,N) beginWithLargeTitle;
@property (TB,N) endWithLargeTitle;
@property (TB,N) beginWithTransparencyAllowed;
@property (TB,N) endWithTransparencyAllowed;
@property (T{CGPoint=dd},N,V_startingContentOffsetForObservedScrollView) startingContentOffsetForObservedScrollView;
@property (TB,N) observedScrollViewOffsetIsApplicable;
@property (TB,N) sharesContentViewLayouts;
@property (T@"_UINavigationBarLayout",&,N,V_fromLayout) fromLayout;
@property (T@"_UINavigationBarLayout",&,N,V_toLayout) toLayout;
@property (T@"UIView",&,N,V_transitionOverlayView) transitionOverlayView;
@property (T@"_UINavigationBarLargeTitleViewLayout",&,N) fromLargeTitleViewLayout;
@property (T@"_UINavigationBarLargeTitleViewLayout",&,N) toLargeTitleViewLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationBarTransitionContext fadeOutFunction];
+[_UINavigationBarTransitionContext contextForTransition:withIdiom:completion:];
+[_UINavigationBarTransitionContext fadeInFunction];
```

## Instance methods

```
-[_UINavigationBarTransitionContext toLayout];
-[_UINavigationBarTransitionContext setCompact:];
-[_UINavigationBarTransitionContext setPromptView:];
-[_UINavigationBarTransitionContext setContentView:];
-[_UINavigationBarTransitionContext tabBarHostedView];
-[_UINavigationBarTransitionContext setCompletionHandler:];
-[_UINavigationBarTransitionContext navigationBar];
-[_UINavigationBarTransitionContext completionHandler];
-[_UINavigationBarTransitionContext setFromLayout:];
-[_UINavigationBarTransitionContext setBackgroundAlpha:];
-[_UINavigationBarTransitionContext fromLayout];
-[_UINavigationBarTransitionContext setTabBarHostedView:];
-[_UINavigationBarTransitionContext complete];
-[_UINavigationBarTransitionContext setRTL:];
-[_UINavigationBarTransitionContext backgroundAlpha];
-[_UINavigationBarTransitionContext setNavigationBar:];
-[_UINavigationBarTransitionContext prepare];
-[_UINavigationBarTransitionContext contentView];
-[_UINavigationBarTransitionContext backgroundView];
-[_UINavigationBarTransitionContext _animationOptions];
-[_UINavigationBarTransitionContext description];
-[_UINavigationBarTransitionContext animate];
-[_UINavigationBarTransitionContext compact];
-[_UINavigationBarTransitionContext setStack:];
-[_UINavigationBarTransitionContext setToLayout:];
-[_UINavigationBarTransitionContext cancel];
-[_UINavigationBarTransitionContext setLargeTitleView:];
-[_UINavigationBarTransitionContext promptView];
-[_UINavigationBarTransitionContext isRTL];
-[_UINavigationBarTransitionContext stack];
-[_UINavigationBarTransitionContext largeTitleView];
-[_UINavigationBarTransitionContext twoPart];
-[_UINavigationBarTransitionContext isPushOperation];
-[_UINavigationBarTransitionContext _animateAsTwoPartsWithOverlap:partOne:partTwo:];
-[_UINavigationBarTransitionContext _animateAsTwoPartsWithOverlapIfNecessaryPartOne:partTwo:];
-[_UINavigationBarTransitionContext _animateAsTwoPartsWithoutOverlap:partTwo:];
-[_UINavigationBarTransitionContext _animateBackgroundView];
-[_UINavigationBarTransitionContext _animateFromPalette:fromPaletteFrame:toPalette:toPaletteFrame:];
-[_UINavigationBarTransitionContext _animateInProcessAsTwoPartsWithKeyframeID:overlap:partOne:partTwo:];
-[_UINavigationBarTransitionContext _animateInProcessAsTwoPartsWithOverlapIfNecessaryWithKeyframeID:fractionComplete:partOne:partTwo:];
-[_UINavigationBarTransitionContext _prepareTransitionFromPalette:toPalette:toPaletteFrame:];
-[_UINavigationBarTransitionContext _resetContentAndLargeTitleViewCompleted:];
-[_UINavigationBarTransitionContext _updateIncomingLayoutWidthToMatchOutgoingLayout];
-[_UINavigationBarTransitionContext allowLargeTitles];
-[_UINavigationBarTransitionContext apiVersion];
-[_UINavigationBarTransitionContext beginWithLargeTitle];
-[_UINavigationBarTransitionContext beginWithTransparencyAllowed];
-[_UINavigationBarTransitionContext endWithLargeTitle];
-[_UINavigationBarTransitionContext endWithTransparencyAllowed];
-[_UINavigationBarTransitionContext fromLargeTitleViewLayout];
-[_UINavigationBarTransitionContext observedScrollViewOffsetIsApplicable];
-[_UINavigationBarTransitionContext prepareForInterruption];
-[_UINavigationBarTransitionContext recordUpdates:];
-[_UINavigationBarTransitionContext setAllLargeTitleLayoutsVisible];
-[_UINavigationBarTransitionContext setAllowLargeTitles:];
-[_UINavigationBarTransitionContext setApiVersion:];
-[_UINavigationBarTransitionContext setBackgroundView:isBarBackground:];
-[_UINavigationBarTransitionContext setBeginWithLargeTitle:];
-[_UINavigationBarTransitionContext setBeginWithTransparencyAllowed:];
-[_UINavigationBarTransitionContext setEndWithLargeTitle:];
-[_UINavigationBarTransitionContext setEndWithTransparencyAllowed:];
-[_UINavigationBarTransitionContext setFromLargeTitleViewLayout:];
-[_UINavigationBarTransitionContext setObservedScrollViewOffsetIsApplicable:];
-[_UINavigationBarTransitionContext setPushOperation:];
-[_UINavigationBarTransitionContext setSharesContentViewLayouts:];
-[_UINavigationBarTransitionContext setStartingContentOffsetForObservedScrollView:];
-[_UINavigationBarTransitionContext setToLargeTitleViewLayout:];
-[_UINavigationBarTransitionContext setTransitionOverlayView:];
-[_UINavigationBarTransitionContext setTwoPart:];
-[_UINavigationBarTransitionContext sharesContentViewLayouts];
-[_UINavigationBarTransitionContext shouldPerformTwoPartCrossfadeTransition];
-[_UINavigationBarTransitionContext shouldSlideBarBackground];
-[_UINavigationBarTransitionContext startingContentOffsetForObservedScrollView];
-[_UINavigationBarTransitionContext toLargeTitleViewLayout];
-[_UINavigationBarTransitionContext transitionOverlayView];
-[_UINavigationBarTransitionContext viewFadingInFromCustomAlpha];
-[_UINavigationBarTransitionContext viewUsingEaseInCurve];
```
