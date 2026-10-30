# `_UIPopoverStandardChromeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPopoverBackgroundView`
- 10 instance variables, 8 properties, 33 instance methods, 4 class methods

## Instance variables

```
B useShortMode;
B _debugMode;
@"UIView" viewToMaskWhenContentExtendsOverArrow;
Q _arrowDirection;
d _arrowOffset;
@"UIColor" _arrowBackgroundColor;
@"UIColor" _popoverBackgroundColor;
@"UIVisualEffect" _backgroundEffect;
q _backgroundStyle;
@"UIColor" _contentBlendingColor;
```

## Properties

```
@property (Tq,N,V_backgroundStyle) backgroundStyle;
@property (TB,N,VuseShortMode) useShortMode;
@property (TB,N,GisDebugModeEnabled,V_debugMode) debugModeEnabled;
@property (T@"UIVisualEffect",C,N,V_backgroundEffect) backgroundEffect;
@property (T@"UIColor",C,N,V_popoverBackgroundColor) popoverBackgroundColor;
@property (T@"UIColor",C,N,V_arrowBackgroundColor) arrowBackgroundColor;
@property (T@"UIColor",R,N,V_contentBlendingColor) contentBlendingColor;
@property (T@"UIView",W,N,VviewToMaskWhenContentExtendsOverArrow) viewToMaskWhenContentExtendsOverArrow;
```

## Class methods

```
+[_UIPopoverStandardChromeView arrowHeight];
+[_UIPopoverStandardChromeView contentViewInsets];
+[_UIPopoverStandardChromeView legacyChromeViewClass];
+[_UIPopoverStandardChromeView standardChromeViewClass];
```

## Instance methods

```
-[_UIPopoverStandardChromeView _contentViewFrame];
-[_UIPopoverStandardChromeView setBackgroundEffect:];
-[_UIPopoverStandardChromeView isPinned];
-[_UIPopoverStandardChromeView setArrowDirection:];
-[_UIPopoverStandardChromeView popoverBackgroundColor];
-[_UIPopoverStandardChromeView backgroundEffect];
-[_UIPopoverStandardChromeView backgroundStyle];
-[_UIPopoverStandardChromeView setArrowOffset:];
-[_UIPopoverStandardChromeView arrowDirection];
-[_UIPopoverStandardChromeView setPopoverBackgroundColor:];
-[_UIPopoverStandardChromeView initWithFrame:];
-[_UIPopoverStandardChromeView setBackgroundStyle:animated:];
-[_UIPopoverStandardChromeView setBackgroundStyle:];
-[_UIPopoverStandardChromeView arrowOffset];
-[_UIPopoverStandardChromeView _resolvedBackgroundStyle];
-[_UIPopoverStandardChromeView _shouldUseEqualContentInsetsOnAllSides];
-[_UIPopoverStandardChromeView _updateArrowImages];
-[_UIPopoverStandardChromeView arrowBackgroundColor];
-[_UIPopoverStandardChromeView contentBlendingColor];
-[_UIPopoverStandardChromeView isDebugModeEnabled];
-[_UIPopoverStandardChromeView isRightArrowPinnedToBottom];
-[_UIPopoverStandardChromeView isRightArrowPinnedToTop];
-[_UIPopoverStandardChromeView maxNonPinnedOffset];
-[_UIPopoverStandardChromeView minNonPinnedOffset];
-[_UIPopoverStandardChromeView safeAreaInsetsForContentView];
-[_UIPopoverStandardChromeView setArrowBackgroundColor:];
-[_UIPopoverStandardChromeView setDebugModeEnabled:];
-[_UIPopoverStandardChromeView setUseShortMode:];
-[_UIPopoverStandardChromeView setViewToMaskWhenContentExtendsOverArrow:];
-[_UIPopoverStandardChromeView useShortMode];
-[_UIPopoverStandardChromeView usesImagesForShapeMasking];
-[_UIPopoverStandardChromeView viewToMaskWhenContentExtendsOverArrow];
-[_UIPopoverStandardChromeView wouldPinForOffset:];
```
