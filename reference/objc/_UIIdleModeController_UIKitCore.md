# `_UIIdleModeController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 3 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _didApplyVisualEffects;
Q _dismissalTransactionID;
@"UIWindow" _backgroundWindow;
@"UIImageView" _vignetteView;
B _keyWindowAllowedGroupBlending;
@"UIWindow" _keyWindow;
@"NSMapTable" _viewsToCAFilters;
@"NSMapTable" _viewsToAttributes;
@"NSMapTable" _viewsToOriginalAttributes;
B _idleModeEnabled;
@"UIScreen" _screen;
Q _style;
```

## Properties

```
@property (TB,N,GisIdleModeEnabled,V_idleModeEnabled) idleModeEnabled;
@property (T@"UIScreen",R,N,V_screen) screen;
@property (TQ,N,V_style) style;
```

## Instance methods

```
-[_UIIdleModeController initWithScreen:];
-[_UIIdleModeController screen];
-[_UIIdleModeController dealloc];
-[_UIIdleModeController style];
-[_UIIdleModeController setStyle:];
-[_UIIdleModeController _animateDismissal];
-[_UIIdleModeController _animatePresentation];
-[_UIIdleModeController _applyDismissalLayoutAttributesToViews];
-[_UIIdleModeController _applyLayoutAttributes:toView:];
-[_UIIdleModeController _applyPresentationLayoutAttributesToViews];
-[_UIIdleModeController _completeDismissal];
-[_UIIdleModeController _dimmingOverlayWhiteValueForUserInterfaceStyle:];
-[_UIIdleModeController _dismissalAnimationDuration];
-[_UIIdleModeController _enterIdleMode];
-[_UIIdleModeController _enterIdleModeWithOptions:];
-[_UIIdleModeController _exitIdleMode];
-[_UIIdleModeController _exitIdleModeWithOptions:];
-[_UIIdleModeController _imageForTraitCollection:];
-[_UIIdleModeController _originalAttributesForView:comparedToIdleModeAttributes:];
-[_UIIdleModeController _postWillEnterNotification];
-[_UIIdleModeController _postWillExitNotification];
-[_UIIdleModeController _prepareForPresentationWithKeyWindow:focusedView:];
-[_UIIdleModeController _presentationAnimationDuration];
-[_UIIdleModeController _recordLayoutAttributesStartingAtView:];
-[_UIIdleModeController _vignetteAlphaForUserInterfaceStyle:];
-[_UIIdleModeController _vignetteImageAroundFocusedFrame:];
-[_UIIdleModeController isIdleModeEnabled];
-[_UIIdleModeController setIdleModeEnabled:];
```
