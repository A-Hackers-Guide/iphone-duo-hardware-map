# `CAMZoomButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 21 instance variables, 24 properties, 80 instance methods, 6 class methods

## Instance variables

```
B _shouldHideBackground;
B _overPlatter;
B _enlargeText;
B _showZoomFactorSymbol;
q _contentType;
d _zoomFactor;
q _zoomSymbol;
q _focalLength;
q _accessoryState;
q _accessoryPosition;
q _orientation;
@"UIView" __contentContainerView;
@"CAMZoomFactorLabel" __zoomFactorLabel;
@"UIImageView" __zoomSymbolView;
@"CAMFocalLengthLabel" __focalLengthLabel;
@"UIView" __backgroundEffectContainerView;
@"UIVisualEffectView" __backgroundVisualEffectView;
@"UIView" __accessoryBackgroundView;
@"UIImageView" __accessoryImageView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _tappableEdgeInsets;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _highlightingTransform;
```

## Properties

```
@property (T@"UIView",R,N,V__contentContainerView) _contentContainerView;
@property (T@"CAMZoomFactorLabel",R,N,V__zoomFactorLabel) _zoomFactorLabel;
@property (T@"UIImageView",R,N,V__zoomSymbolView) _zoomSymbolView;
@property (T@"CAMFocalLengthLabel",&,N,V__focalLengthLabel) _focalLengthLabel;
@property (T@"UIView",&,N,V__backgroundEffectContainerView) _backgroundEffectContainerView;
@property (T@"UIVisualEffectView",&,N,V__backgroundVisualEffectView) _backgroundVisualEffectView;
@property (T{CGAffineTransform=dddddd},N,S_setHighlightingTransform:,V_highlightingTransform) highlightingTransform;
@property (T@"UIView",&,N,V__accessoryBackgroundView) _accessoryBackgroundView;
@property (T@"UIImageView",&,N,V__accessoryImageView) _accessoryImageView;
@property (Tq,N,V_contentType) contentType;
@property (Td,N,V_zoomFactor) zoomFactor;
@property (Tq,N,V_zoomSymbol) zoomSymbol;
@property (Tq,N,V_focalLength) focalLength;
@property (Tq,N,V_accessoryState) accessoryState;
@property (Tq,N,V_accessoryPosition) accessoryPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) accessoryFrame;
@property (T{UIEdgeInsets=dddd},N,V_tappableEdgeInsets) tappableEdgeInsets;
@property (Tq,N,V_orientation) orientation;
@property (TB,N,V_shouldHideBackground) shouldHideBackground;
@property (TB,N,GisOverPlatter,V_overPlatter) overPlatter;
@property (TB,N,V_enlargeText) enlargeText;
@property (TB,N,V_showZoomFactorSymbol) showZoomFactorSymbol;
@property (TB,N) useLeadingZero;
@property (Tq,N) textShadowStrength;
```

## Class methods

```
+[CAMZoomButton circleDiameterForContentSize:];
+[CAMZoomButton fontSizeForContentSize:];
+[CAMZoomButton shouldUseLargeButtonSizeForContentSize:];
+[CAMZoomButton zoomFactorFormatter];
+[CAMZoomButton textForZoomFactor:showZoomFactorSymbol:];
+[CAMZoomButton textForZoomFactor:showZoomFactorSymbol:useLeadingZero:];
```

## Instance methods

```
-[CAMZoomButton setContentType:];
-[CAMZoomButton setOrientation:animated:];
-[CAMZoomButton accessoryState];
-[CAMZoomButton setOrientation:];
-[CAMZoomButton focalLength];
-[CAMZoomButton textShadowStrength];
-[CAMZoomButton _layoutFocalLengthLabel];
-[CAMZoomButton zoomFactor];
-[CAMZoomButton setZoomFactor:];
-[CAMZoomButton intrinsicContentSize];
-[CAMZoomButton _accessoryBackgroundView];
-[CAMZoomButton _updateAccessoryAlphas];
-[CAMZoomButton _zoomSymbolView];
-[CAMZoomButton highlightingTransform];
-[CAMZoomButton _ensureBackgroundViewOrdering];
-[CAMZoomButton setEnlargeText:];
-[CAMZoomButton setFocalLength:];
-[CAMZoomButton _focalLengthLabel];
-[CAMZoomButton _setHighlightingTransform:];
-[CAMZoomButton setAccessoryPosition:animated:];
-[CAMZoomButton alignmentRectInsets];
-[CAMZoomButton _backgroundEffectContainerView];
-[CAMZoomButton _highlightingTransformForHighlighted:];
-[CAMZoomButton orientation];
-[CAMZoomButton _imageForZoomSymbol:];
-[CAMZoomButton enlargeText];
-[CAMZoomButton contentType];
-[CAMZoomButton shouldHideBackground];
-[CAMZoomButton useLeadingZero];
-[CAMZoomButton _updateBackgroundView];
-[CAMZoomButton layoutSubviews];
-[CAMZoomButton _layoutFocalLengthLabelForAlignmentRectBounds:contentTransform:];
-[CAMZoomButton set_accessoryImageView:];
-[CAMZoomButton _accessoryImageView];
-[CAMZoomButton set_backgroundEffectContainerView:];
-[CAMZoomButton zoomSymbol];
-[CAMZoomButton initForPlatter:];
-[CAMZoomButton tintColorDidChange];
-[CAMZoomButton accessoryPosition];
-[CAMZoomButton setHighlighted:];
-[CAMZoomButton setOverPlatter:];
-[CAMZoomButton setZoomSymbol:animated:];
-[CAMZoomButton _zoomFactorLabel];
-[CAMZoomButton showZoomFactorSymbol];
-[CAMZoomButton isOverPlatter];
-[CAMZoomButton _contentContainerView];
-[CAMZoomButton _transformForEnlargeText:orientation:];
-[CAMZoomButton setTappableEdgeInsets:];
-[CAMZoomButton setAccessoryPosition:];
-[CAMZoomButton setFocalLength:animated:];
-[CAMZoomButton _updateBackgroundViewDeferRemovalForAnimations:];
-[CAMZoomButton _backgroundVisualEffectView];
-[CAMZoomButton setShowZoomFactorSymbol:];
-[CAMZoomButton _updateZoomFactorLabelIfNeeded];
-[CAMZoomButton set_backgroundVisualEffectView:];
-[CAMZoomButton _commonCAMZoomButtonInitializationForPlatter:];
-[CAMZoomButton setTextShadowStrength:];
-[CAMZoomButton setZoomSymbol:];
-[CAMZoomButton set_focalLengthLabel:];
-[CAMZoomButton setShouldHideBackground:animationDuration:];
-[CAMZoomButton _updateZoomSymbolViewAnimated:];
-[CAMZoomButton setContentType:animated:];
-[CAMZoomButton initWithCoder:];
-[CAMZoomButton setAccessoryState:animated:];
-[CAMZoomButton setUseLeadingZero:];
-[CAMZoomButton _preferredContentSizeCategoryChanged];
-[CAMZoomButton _performHighlightAnimation];
-[CAMZoomButton setShouldHideBackground:];
-[CAMZoomButton _installBackgroundEffectContainerView];
-[CAMZoomButton tappableEdgeInsets];
-[CAMZoomButton _updateBackgroundEffectViewContents];
-[CAMZoomButton accessoryFrame];
-[CAMZoomButton _updateAlphaForBackgroundViews];
-[CAMZoomButton _commonCAMZoomButtonInitialization];
-[CAMZoomButton initWithFrame:];
-[CAMZoomButton _createFocalLengthLabelIfNeeded];
-[CAMZoomButton _updateBackgroundEffectContainerViewAlpha];
-[CAMZoomButton _createZoomSymbolViewIfNecessary];
-[CAMZoomButton set_accessoryBackgroundView:];
-[CAMZoomButton setAccessoryState:];
```
