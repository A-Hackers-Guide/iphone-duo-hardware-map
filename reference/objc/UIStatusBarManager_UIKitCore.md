# `UIStatusBarManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 12 instance variables, 19 properties, 39 instance methods, 2 class methods

## Instance variables

```
i _preferredStatusBarVisibility;
B _prefersStatusBarHidden;
B _overriddingStatusBarHidden;
B _statusBarHidden;
B _inStatusBarFadeAnimation;
q _statusBarStyle;
@"UIWindowScene" _windowScene;
q _statusBarResolvedStyle;
@"NSDictionary" _statusBarPartStyles;
d _statusBarAlpha;
q _statusBarAxis;
@? _debugMenuHandler;
```

## Properties

```
@property (T@"UIWindowScene",&,N,V_windowScene) windowScene;
@property (Tq,R,N,V_statusBarResolvedStyle) statusBarResolvedStyle;
@property (T@"NSDictionary",R,N,V_statusBarPartStyles) statusBarPartStyles;
@property (TB,R,N,GisInStatusBarFadeAnimation,V_inStatusBarFadeAnimation) inStatusBarFadeAnimation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _statusBarFrameIgnoringVisibility;
@property (TB,N,G_isOverridingStatusBarHidden,S_setOverridingStatusBarHidden:,V_overriddingStatusBarHidden) _overriddingStatusBarHidden;
@property (Td,R,N,V_statusBarAlpha) statusBarAlpha;
@property (Td,R,N) statusBarHeight;
@property (Td,R,N) defaultStatusBarHeight;
@property (Tq,R,N,V_statusBarAxis) statusBarAxis;
@property (T@?,C,N,V_debugMenuHandler) debugMenuHandler;
@property (Tq,R,N,V_statusBarStyle) statusBarStyle;
@property (TB,R,N,GisStatusBarHidden,V_statusBarHidden) statusBarHidden;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) statusBarFrame;
@property (T@"UIScene",W,N,G_scene,S_setScene:) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIStatusBarManager _stringForStatusBarAxis:];
+[UIStatusBarManager _implicitStatusBarAnimationParametersWithClass:];
```

## Instance methods

```
-[UIStatusBarManager statusBarAlpha];
-[UIStatusBarManager statusBarHeight];
-[UIStatusBarManager setWindowScene:];
-[UIStatusBarManager _scene];
-[UIStatusBarManager statusBarHidden];
-[UIStatusBarManager initWithScene:];
-[UIStatusBarManager _settingsDiffActionsForScene:];
-[UIStatusBarManager _setScene:];
-[UIStatusBarManager statusBarFrame];
-[UIStatusBarManager windowScene];
-[UIStatusBarManager statusBarAxis];
-[UIStatusBarManager statusBarStyle];
-[UIStatusBarManager _updateAlpha];
-[UIStatusBarManager _adjustedLocationForXPosition:];
-[UIStatusBarManager _handleScrollToTopAtXPosition:];
-[UIStatusBarManager _isOverridingStatusBarHidden];
-[UIStatusBarManager _setOverridingStatusBarHidden:];
-[UIStatusBarManager _setOverridingStatusBarHidden:animationParameters:];
-[UIStatusBarManager _statusBarFrameIgnoringVisibility];
-[UIStatusBarManager _updateAxisForWindow:targetOrientation:animationParameters:];
-[UIStatusBarManager _updateStatusBarAppearanceWithClientSettings:transitionContext:animationParameters:];
-[UIStatusBarManager _updateStyleForWindow:animationParameters:shouldAnimate:shouldFence:];
-[UIStatusBarManager _updateVisibilityForWindow:targetOrientation:animationParameters:];
-[UIStatusBarManager _visibilityChangedWithOriginalOrientation:targetOrientation:animationParameters:];
-[UIStatusBarManager createLocalStatusBar];
-[UIStatusBarManager debugMenuHandler];
-[UIStatusBarManager defaultStatusBarHeight];
-[UIStatusBarManager defaultStatusBarHeightInOrientation:];
-[UIStatusBarManager handleTapAction:];
-[UIStatusBarManager isInStatusBarFadeAnimation];
-[UIStatusBarManager isStatusBarHidden];
-[UIStatusBarManager setDebugMenuHandler:];
-[UIStatusBarManager statusBarFrameForStatusBarHeight:];
-[UIStatusBarManager statusBarFrameForStatusBarHeight:inOrientation:];
-[UIStatusBarManager statusBarPartStyles];
-[UIStatusBarManager statusBarResolvedStyle];
-[UIStatusBarManager updateStatusBarAppearance];
-[UIStatusBarManager updateStatusBarAppearanceWithAnimationParameters:];
-[UIStatusBarManager updateStatusBarAppearanceWithClientSettings:transitionContext:];
```
