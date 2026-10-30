# `_TtC5UIKit30NavigationBarTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UINavigationBarTransitionContextProtocol`
- 34 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
_$sSo25_UINavigationBarItemStackC stack;
UIKit.NavigationBarLayout fromLayout;
UIKit.NavigationBarLayout toLayout;
CoreGraphics.CGFloat twoPartAnimationBaseDuration;
CoreGraphics.CGFloat twoPartAnimationOverlapDuration;
_$sSo12NSMutableSetCSg clippingViews;
_$sSo36_UINavigationBarLargeTitleViewLayoutCSg fromLargeTitleLayout;
_$sSo36_UINavigationBarLargeTitleViewLayoutCSg toLargeTitleLayout;
UIKit.NavigationBarTransitionContext.LargeTitleTransitionType largeTitleTransitionType;
_$sySb_So35_UINavigationBarTransitionAssistantCSgtc completionHandler;
_$sSo15UINavigationBarCSgXu navigationBar;
Swift.Bool isPushOperation;
Swift.Bool compact;
Swift.Bool usesBarBackground;
Swift.Bool allowLargeTitles;
Swift.Bool twoPart;
__C._UIBarAppearanceAPI apiVersion;
CoreGraphics.CGFloat backgroundAlpha;
_$sSo32_UINavigationBarModernPromptViewCSg promptView;
UIKit.NavigationBarContentView ? contentView;
UIKit.NavigationBarExternalRepresentationOwner ? externalRepresentationOwner;
_$sSo16_UIBarBackgroundCSg backgroundView;
UIKit.NavigationBarLargeTitleView ? largeTitleView;
_$sSo6UIViewCSg tabBarHostedView;
Swift.Bool beginWithLargeTitle;
Swift.Bool endWithLargeTitle;
Swift.Bool beginWithTransparencyAllowed;
Swift.Bool endWithTransparencyAllowed;
__C.CGPoint startingContentOffsetForObservedScrollView;
Swift.Bool observedScrollViewOffsetIsApplicable;
Swift.Bool sharesContentViewLayouts;
_$sSo6UIViewCSg transitionOverlayView;
Swift.Bool wasFullyScrolledAway;
__C._UINavigationBarTransition transition;
```

## Properties

```
@property (T@"_UINavigationBarLargeTitleViewLayout",N,&) fromLargeTitleViewLayout;
@property (T@"_UINavigationBarLargeTitleViewLayout",N,&) toLargeTitleViewLayout;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_TtC5UIKit30NavigationBarTransitionContext init];
-[_TtC5UIKit30NavigationBarTransitionContext description];
-[_TtC5UIKit30NavigationBarTransitionContext fromLargeTitleViewLayout];
-[_TtC5UIKit30NavigationBarTransitionContext setFromLargeTitleViewLayout:];
-[_TtC5UIKit30NavigationBarTransitionContext setToLargeTitleViewLayout:];
-[_TtC5UIKit30NavigationBarTransitionContext toLargeTitleViewLayout];
```
