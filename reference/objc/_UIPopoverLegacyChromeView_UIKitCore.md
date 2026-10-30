# `_UIPopoverLegacyChromeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIPopoverStandardChromeView`
- 11 instance variables, 4 properties, 40 instance methods, 2 class methods

## Instance variables

```
@"UIView" _arrowBackgroundView;
@"UIVisualEffectView" _effectView;
@"UIView" _maskView;
q _requestedBackgroundStyle;
q _backgroundStyle;
B _popoverBackgroundColorIsOpaque;
B _arrowVisible;
B _wasPinned;
@"UIView" _arrowView;
@"UIView" _leftCapView;
@"UIView" _rightCapView;
```

## Properties

```
@property (T@"UIView",R,N,V_arrowView) arrowView;
@property (T@"UIView",R,N,V_leftCapView) leftCapView;
@property (T@"UIView",R,N,V_rightCapView) rightCapView;
@property (TB,R,N) hasComponentViews;
```

## Class methods

```
+[_UIPopoverLegacyChromeView arrowBase];
+[_UIPopoverLegacyChromeView arrowHeight];
```

## Instance methods

```
-[_UIPopoverLegacyChromeView _shadowRadius];
-[_UIPopoverLegacyChromeView touchesEnded:withEvent:];
-[_UIPopoverLegacyChromeView didMoveToWindow];
-[_UIPopoverLegacyChromeView _shadowOpacity];
-[_UIPopoverLegacyChromeView touchesCancelled:withEvent:];
-[_UIPopoverLegacyChromeView isPinned];
-[_UIPopoverLegacyChromeView layoutSubviews];
-[_UIPopoverLegacyChromeView touchesBegan:withEvent:];
-[_UIPopoverLegacyChromeView touchesMoved:withEvent:];
-[_UIPopoverLegacyChromeView backgroundStyle];
-[_UIPopoverLegacyChromeView setArrowOffset:];
-[_UIPopoverLegacyChromeView setPopoverBackgroundColor:];
-[_UIPopoverLegacyChromeView setBackgroundStyle:];
-[_UIPopoverLegacyChromeView arrowOffset];
-[_UIPopoverLegacyChromeView _configureEffectView];
-[_UIPopoverLegacyChromeView _effectiveBackgroundEffect];
-[_UIPopoverLegacyChromeView _layoutArrowViewsLeftOrRight];
-[_UIPopoverLegacyChromeView _layoutArrowViewsNone];
-[_UIPopoverLegacyChromeView _layoutArrowViewsUpOrDown];
-[_UIPopoverLegacyChromeView _loadNecessaryViews];
-[_UIPopoverLegacyChromeView _removeEffectView];
-[_UIPopoverLegacyChromeView _resetComponentViews];
-[_UIPopoverLegacyChromeView _resolvedBackgroundStyle];
-[_UIPopoverLegacyChromeView _shadowInsets];
-[_UIPopoverLegacyChromeView _shadowOffset];
-[_UIPopoverLegacyChromeView _shadowPath];
-[_UIPopoverLegacyChromeView _updateBackgroundStyle];
-[_UIPopoverLegacyChromeView _updateChrome];
-[_UIPopoverLegacyChromeView arrowView];
-[_UIPopoverLegacyChromeView hasComponentViews];
-[_UIPopoverLegacyChromeView leftCapView];
-[_UIPopoverLegacyChromeView legacyBackgroundEffect];
-[_UIPopoverLegacyChromeView maxNonPinnedOffset];
-[_UIPopoverLegacyChromeView minNonPinnedOffset];
-[_UIPopoverLegacyChromeView motionBegan:withEvent:];
-[_UIPopoverLegacyChromeView motionCancelled:withEvent:];
-[_UIPopoverLegacyChromeView motionEnded:withEvent:];
-[_UIPopoverLegacyChromeView rightCapView];
-[_UIPopoverLegacyChromeView setArrowBackgroundColor:];
-[_UIPopoverLegacyChromeView useShortMode];
```
