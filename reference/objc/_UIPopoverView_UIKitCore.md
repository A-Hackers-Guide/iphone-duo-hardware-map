# `_UIPopoverView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIPopoverShapeLayerChromeViewDelegate`
- 20 instance variables, 26 properties, 75 instance methods, 1 class methods

## Instance variables

```
@"UIView" _contentView;
@"UIPopoverBackgroundView" _backgroundView;
@"UIView" _clipView;
# _backgroundViewClass;
B _showsBackgroundComponentHighlights;
B _showsBackgroundViewHighlight;
B _showsContentViewHighlight;
B _contentExtendsOverArrow;
B _chromeHidden;
B _chromeHiddenForSizeTransition;
B _useZoomTransition;
B __contentOverflowsPlatter;
d _customCornerRadius;
@"UIActionSheet" _presentedActionSheet;
@"UIPopoverController" _popoverController;
q _backgroundBlurEffectStyle;
@"UIVisualEffect" _backgroundEffect;
@"_UIRoundedRectShadowView" _shadowView;
d _animationOvershootHeight;
{CGSize="width"d"height"d} _contentSize;
```

## Properties

```
@property (TB,N,V__contentOverflowsPlatter) _contentOverflowsPlatter;
@property (TB,N,V_showsBackgroundComponentHighlights) showsBackgroundComponentHighlights;
@property (TB,N,V_showsBackgroundViewHighlight) showsBackgroundViewHighlight;
@property (TB,N,V_showsContentViewHighlight) showsContentViewHighlight;
@property (TB,R,N,V_contentExtendsOverArrow) contentExtendsOverArrow;
@property (Td,N,S_setCustomCornerRadius:,V_customCornerRadius) _customCornerRadius;
@property (T@"UITraitCollection",R,N) _traitCollectionForGlassContent;
@property (Td,N) arrowOffset;
@property (TQ,N) arrowDirection;
@property (Tq,N) backgroundStyle;
@property (Tq,N,V_backgroundBlurEffectStyle) backgroundBlurEffectStyle;
@property (T@"UIColor",C,N) popoverBackgroundColor;
@property (T@"UIColor",C,N) arrowBackgroundColor;
@property (T@"UIVisualEffect",C,N,V_backgroundEffect) backgroundEffect;
@property (TB,N,V_chromeHidden) chromeHidden;
@property (TB,N,V_chromeHiddenForSizeTransition) chromeHiddenForSizeTransition;
@property (TB,N,V_useZoomTransition) useZoomTransition;
@property (T@"_UIRoundedRectShadowView",&,N,V_shadowView) shadowView;
@property (T{CGSize=dd},N,V_contentSize) contentSize;
@property (Td,N,V_animationOvershootHeight) animationOvershootHeight;
@property (T@"UIActionSheet",&,N,V_presentedActionSheet) presentedActionSheet;
@property (T@"UIPopoverController",N,V_popoverController) popoverController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPopoverView popoverViewContainingView:];
```

## Instance methods

```
-[_UIPopoverView _traitCollectionForChildEnvironment:];
-[_UIPopoverView touchesEnded:withEvent:];
-[_UIPopoverView _setCornerRadius:];
-[_UIPopoverView setBackgroundEffect:];
-[_UIPopoverView touchesCancelled:withEvent:];
-[_UIPopoverView setUseZoomTransition:];
-[_UIPopoverView setArrowDirection:];
-[_UIPopoverView layoutSubviews];
-[_UIPopoverView contentSize];
-[_UIPopoverView popoverBackgroundColor];
-[_UIPopoverView touchesBegan:withEvent:];
-[_UIPopoverView touchesMoved:withEvent:];
-[_UIPopoverView _normalInheritedTintColor];
-[_UIPopoverView backgroundEffect];
-[_UIPopoverView backgroundStyle];
-[_UIPopoverView willMoveToWindow:];
-[_UIPopoverView shadowView];
-[_UIPopoverView contentView];
-[_UIPopoverView setContentSize:];
-[_UIPopoverView backgroundView];
-[_UIPopoverView _style];
-[_UIPopoverView setArrowOffset:];
-[_UIPopoverView arrowDirection];
-[_UIPopoverView setPopoverBackgroundColor:];
-[_UIPopoverView setShadowView:];
-[_UIPopoverView useZoomTransition];
-[_UIPopoverView initWithFrame:];
-[_UIPopoverView setBackgroundStyle:];
-[_UIPopoverView arrowOffset];
-[_UIPopoverView _snapshotBounds];
-[_UIPopoverView _traitCollectionForGlassContent];
-[_UIPopoverView _adjustViewHierarchy];
-[_UIPopoverView _allowsCustomizationOfContent];
-[_UIPopoverView _contentOverflowsPlatter];
-[_UIPopoverView _customCornerRadius];
-[_UIPopoverView _definesTintColor];
-[_UIPopoverView _hideArrow];
-[_UIPopoverView _installContentView];
-[_UIPopoverView _installGlass:];
-[_UIPopoverView _needsLayoutOnAnimatedFrameChangeForNewFrame:];
-[_UIPopoverView _performBlockCheckingDefinesTintColor:];
-[_UIPopoverView _popoverShapeLayerChromeViewWillConfigureBackgroundView];
-[_UIPopoverView _setCustomCornerRadius:];
-[_UIPopoverView _setFrame:arrowOffset:];
-[_UIPopoverView _setPopoverContentView:];
-[_UIPopoverView _shapeLayerChromeView];
-[_UIPopoverView _shouldInstallContentViewInChromeViewGlass];
-[_UIPopoverView _showArrow];
-[_UIPopoverView _updateAlphaForChromeHidden];
-[_UIPopoverView animationOvershootHeight];
-[_UIPopoverView arrowBackgroundColor];
-[_UIPopoverView backgroundBlurEffectStyle];
-[_UIPopoverView chromeHidden];
-[_UIPopoverView chromeHiddenForSizeTransition];
-[_UIPopoverView contentExtendsOverArrow];
-[_UIPopoverView initWithFrame:backgroundViewClass:];
-[_UIPopoverView initWithFrame:backgroundViewClass:embeddedInView:contentExtendsOverArrow:useZoomTransition:presentationController:];
-[_UIPopoverView popoverController];
-[_UIPopoverView presentedActionSheet];
-[_UIPopoverView safeAreaInsetsForContentView];
-[_UIPopoverView setAnimationOvershootHeight:];
-[_UIPopoverView setArrowBackgroundColor:];
-[_UIPopoverView setBackgroundBlurEffectStyle:];
-[_UIPopoverView setChromeHidden:];
-[_UIPopoverView setChromeHiddenForSizeTransition:];
-[_UIPopoverView setPopoverController:];
-[_UIPopoverView setPresentedActionSheet:];
-[_UIPopoverView setShowsBackgroundComponentHighlights:];
-[_UIPopoverView setShowsBackgroundViewHighlight:];
-[_UIPopoverView setShowsContentViewHighlight:];
-[_UIPopoverView set_contentOverflowsPlatter:];
-[_UIPopoverView showsBackgroundComponentHighlights];
-[_UIPopoverView showsBackgroundViewHighlight];
-[_UIPopoverView showsContentViewHighlight];
-[_UIPopoverView standardChromeView];
```
