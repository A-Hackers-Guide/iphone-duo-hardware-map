# `_UITabBarTVTransitioner`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITabBarControllerInterruptibleTransitioning`
- 9 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _fromViewOriginalShouldRasterize;
d _fromViewLayerOriginalRasterizationScale;
B _toViewOriginalShouldRasterize;
d _toViewLayerOriginalRasterizationScale;
B _transitionFromRight;
q _transitionStyle;
@"<UIViewControllerContextTransitioning>" _transitionContext;
@"UISpringTimingParameters" _slideTimingParameters;
@"UIView" _toViewXFlippedScreenShot;
```

## Properties

```
@property (T@"UISpringTimingParameters",&,N,V_slideTimingParameters) slideTimingParameters;
@property (T@"UIView",&,N,V_toViewXFlippedScreenShot) toViewXFlippedScreenShot;
@property (Tq,N,V_transitionStyle) transitionStyle;
@property (TB,N,V_transitionFromRight) transitionFromRight;
@property (T@"<UIViewControllerContextTransitioning>",&,N,V_transitionContext) transitionContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITabBarTVTransitioner animateTransition:];
-[_UITabBarTVTransitioner transitionDuration:];
-[_UITabBarTVTransitioner transitionContext];
-[_UITabBarTVTransitioner init];
-[_UITabBarTVTransitioner setTransitionContext:];
-[_UITabBarTVTransitioner finishTransition];
-[_UITabBarTVTransitioner transitionStyle];
-[_UITabBarTVTransitioner setTransitionStyle:];
-[_UITabBarTVTransitioner interruptTabBarControllerTransition];
-[_UITabBarTVTransitioner setSlideTimingParameters:];
-[_UITabBarTVTransitioner setToViewXFlippedScreenShot:];
-[_UITabBarTVTransitioner setTransitionFromRight:];
-[_UITabBarTVTransitioner slideTimingParameters];
-[_UITabBarTVTransitioner toViewXFlippedScreenShot];
-[_UITabBarTVTransitioner transitionFromRight];
```
