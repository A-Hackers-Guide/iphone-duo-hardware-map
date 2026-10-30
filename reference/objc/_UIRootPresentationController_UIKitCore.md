# `_UIRootPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISheetPresentationController`
- Protocols: `_UIStatusBarAnimationProviding`
- 2 instance variables, 11 properties, 17 instance methods, 1 class methods

## Instance variables

```
B __shouldDisableAppearanceCallbacksForPresentedViewController;
@"UIWindow" _presentingWindow;
```

## Properties

```
@property (T@"UIWindow",R,W,N,V_presentingWindow) presentingWindow;
@property (Tq,R,N) preferredStatusBarStyle;
@property (TB,N,V__shouldDisableAppearanceCallbacksForPresentedViewController) _shouldDisableAppearanceCallbacksForPresentedViewController;
@property (T@"UIStatusBarStyleAnimationParameters",R,N,G_preferredStatusBarStyleAnimationParameters) preferredStatusBarStyleAnimationParameters;
@property (T@"UIStatusBarHideAnimationParameters",R,N,G_preferredStatusBarHideAnimationParameters) preferredStatusBarHideAnimationParameters;
@property (T@"UIStatusBarAnimationParameters",R,N,G_preferredStatusBarAxisAnimationParameters) _preferredStatusBarAxisAnimationParameters;
@property (Tq,R,N) preferredStatusBarUpdateAnimation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIRootPresentationController _allowsDeferredTransitions];
```

## Instance methods

```
-[_UIRootPresentationController preferredStatusBarUpdateAnimation];
-[_UIRootPresentationController willTransitionToTraitCollection:withTransitionCoordinator:];
-[_UIRootPresentationController _preferredStatusBarHideAnimationParameters];
-[_UIRootPresentationController presentingWindow];
-[_UIRootPresentationController _parentTraitEnvironment];
-[_UIRootPresentationController _statusBarPreferencesForPresentationDidChange];
-[_UIRootPresentationController _isRootPresentation];
-[_UIRootPresentationController initWithPresentedViewController:presentingWindow:];
-[_UIRootPresentationController set_shouldDisableAppearanceCallbacksForPresentedViewController:];
-[_UIRootPresentationController _mayChildGrabPresentedViewControllerView];
-[_UIRootPresentationController _shouldDisableAppearanceCallbacksForPresentedViewController];
-[_UIRootPresentationController _transitionCoordinator];
-[_UIRootPresentationController _preferredStatusBarAxisAnimationParameters];
-[_UIRootPresentationController _preferredStatusBarStyleAnimationParameters];
-[_UIRootPresentationController _fullscreenPresentationSuperview];
-[_UIRootPresentationController _createVisualStyleForProvider:];
-[_UIRootPresentationController preferredStatusBarStyle];
```
