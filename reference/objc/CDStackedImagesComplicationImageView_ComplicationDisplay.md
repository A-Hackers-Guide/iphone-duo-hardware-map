# `CDStackedImagesComplicationImageView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CDComplicationImageView`, `CLKUILegibilityView`, `CLKMonochromeComplicationView`
- 19 instance variables, 15 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"CLKDevice" _device;
@"CLKUIColoringImageView" _foregroundImageView;
@"CLKUIColoringImageView" _backgroundImageView;
@"UIImageView" _foregroundAccentImageView;
@"CLKUIColoringImageView" _monochromeImageView;
@"UIImageView" _monochromeShadowView;
@"UIImageView" _multipartShadowView;
@"UIImage" _multipartShadowViewSource;
@"_CDComplicationImageViewProviderImageView" _layerMaskImageView;
B _isUsingLegibility;
B _isShadowImagesStale;
d _shadowBlur;
@"UIColor" _shadowColor;
@"CLKImageProvider" _imageProvider;
@"<CLKMonochromeFilterProvider>" _filterProvider;
@"UIColor" _color;
@"UIColor" _overrideColor;
d _multicolorAlpha;
@"UIColor" _foregroundColor;
```

## Properties

```
@property (Td,N,V_multicolorAlpha) multicolorAlpha;
@property (T@"UIColor",&,N,V_foregroundColor) foregroundColor;
@property (T@"CLKImageProvider",&,N,V_imageProvider) imageProvider;
@property (T@"UIColor",&,N,V_color) color;
@property (TB,D,N) usesLegibility;
@property (T@"UIColor",&,N,V_overrideColor) overrideColor;
@property (T@"UIColor",?,R,N) contentColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,D,N) legibilityEnabled;
@property (Td,N,V_shadowBlur) shadowBlur;
@property (T@"UIColor",&,N,V_shadowColor) shadowColor;
@property (T@"<CLKMonochromeFilterProvider>",W,N,V_filterProvider) filterProvider;
```

## Instance methods

```
-[CDStackedImagesComplicationImageView setShadowBlur:];
-[CDStackedImagesComplicationImageView setForegroundColor:];
-[CDStackedImagesComplicationImageView shadowBlur];
-[CDStackedImagesComplicationImageView setColor:];
-[CDStackedImagesComplicationImageView _updateColors];
-[CDStackedImagesComplicationImageView layoutSubviews];
-[CDStackedImagesComplicationImageView setOverrideColor:];
-[CDStackedImagesComplicationImageView contentColor];
-[CDStackedImagesComplicationImageView _updateShadow];
-[CDStackedImagesComplicationImageView _updateImages];
-[CDStackedImagesComplicationImageView shadowColor];
-[CDStackedImagesComplicationImageView color];
-[CDStackedImagesComplicationImageView sizeThatFits:];
-[CDStackedImagesComplicationImageView imageProvider];
-[CDStackedImagesComplicationImageView setShadowColor:];
-[CDStackedImagesComplicationImageView foregroundColor];
-[CDStackedImagesComplicationImageView overrideColor];
-[CDStackedImagesComplicationImageView setImageProvider:];
-[CDStackedImagesComplicationImageView initWithFrame:];
-[CDStackedImagesComplicationImageView _updateAlpha];
-[CDStackedImagesComplicationImageView multicolorAlpha];
-[CDStackedImagesComplicationImageView _backgroundFilterStyle];
-[CDStackedImagesComplicationImageView _foregroundFilterStyle];
-[CDStackedImagesComplicationImageView _hasMultipartImages];
-[CDStackedImagesComplicationImageView filterProvider];
-[CDStackedImagesComplicationImageView hasMonochromeImage];
-[CDStackedImagesComplicationImageView legibilityEnabled];
-[CDStackedImagesComplicationImageView setFilterProvider:];
-[CDStackedImagesComplicationImageView setLegibilityEnabled:];
-[CDStackedImagesComplicationImageView setMulticolorAlpha:];
-[CDStackedImagesComplicationImageView setUsesLegibility:];
-[CDStackedImagesComplicationImageView transitionToMonochromeWithFraction:];
-[CDStackedImagesComplicationImageView updateMonochromeColor];
-[CDStackedImagesComplicationImageView usesLegibility];
-[CDStackedImagesComplicationImageView _hasShadowViews];
-[CDStackedImagesComplicationImageView _enumerateImageViewsWithBlock:];
-[CDStackedImagesComplicationImageView _enumerateMultipartImageViewsWithBlock:];
-[CDStackedImagesComplicationImageView _loadImageViewsIfNecessary];
-[CDStackedImagesComplicationImageView _shouldIgnoreTwoPieceImage];
-[CDStackedImagesComplicationImageView _updateImageSubviewsMaxSize];
-[CDStackedImagesComplicationImageView _updateShadowViewImages];
```
