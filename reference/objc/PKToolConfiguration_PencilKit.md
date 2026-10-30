# `PKToolConfiguration`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 29 instance variables, 25 properties, 51 instance methods, 12 class methods

## Instance variables

```
@"PKFloatRange" _cachedStrokeWeightRange;
B _wantsStrokeWeightControl;
B _wantsTopLevelOpacityControl;
B _supportsColor;
B _supportsOpacity;
B _supportsLassoToolEditingView;
B _isEraserTool;
B _shouldShowAzimuthInColorPicker;
@"NSString" _localizedName;
@"UIImage" _baseImage;
@"UIColor" _defaultColor;
@"NSDictionary" _strokeWeightsToButtonImages;
@"UIBezierPath" _shadowPath;
d _opacityLabelVerticalOffset;
@"UIImage" _bandMaskImage;
@"UIImage" _bandContourImage;
d _bandVerticalOffset;
@"UIImage" _tipMaskImage;
@"UIImage" _tipContourImage;
@"UIBezierPath" _shadowPathIncludingTip;
d _minimumBandThickness;
d _maximumBandThickness;
@"NSArray" _baseImagesForAzimuth;
@"NSArray" _tipMaskImagesForAzimuth;
@"NSArray" _tipContourImagesForAzimuth;
@"UIColor" _weightButtonTintColorOverride;
@? _viewControllerProvider;
q _inkVersion;
@? _imageProvider;
```

## Properties

```
@property (T@"NSString",C,N,V_localizedName) localizedName;
@property (T@"UIImage",C,N,V_baseImage) baseImage;
@property (T@"NSArray",C,N,V_baseImagesForAzimuth) baseImagesForAzimuth;
@property (T@"UIImage",C,N) image;
@property (T@"UIBezierPath",C,N,V_shadowPath) shadowPath;
@property (TB,R,N,V_supportsColor) supportsColor;
@property (T@"UIColor",R,N,V_defaultColor) defaultColor;
@property (TB,R,N,V_supportsOpacity) supportsOpacity;
@property (TB,R,N,V_isEraserTool) isEraserTool;
@property (Td,N,V_opacityLabelVerticalOffset) opacityLabelVerticalOffset;
@property (T@"UIImage",C,N,V_bandMaskImage) bandMaskImage;
@property (T@"UIImage",C,N,V_bandContourImage) bandContourImage;
@property (Td,N,V_bandVerticalOffset) bandVerticalOffset;
@property (T@"UIImage",R,N,V_tipMaskImage) tipMaskImage;
@property (T@"NSArray",C,N,V_tipMaskImagesForAzimuth) tipMaskImagesForAzimuth;
@property (T@"UIImage",C,N,V_tipContourImage) tipContourImage;
@property (T@"NSArray",C,N,V_tipContourImagesForAzimuth) tipContourImagesForAzimuth;
@property (T@"UIBezierPath",R,N,V_shadowPathIncludingTip) shadowPathIncludingTip;
@property (TB,R,N) supportsStrokeWeight;
@property (T@"NSDictionary",C,N,V_strokeWeightsToButtonImages) strokeWeightsToButtonImages;
@property (T{CGSize=dd},R,N) strokeWeightButtonSize;
@property (T@"UIColor",R,N,V_weightButtonTintColorOverride) weightButtonTintColorOverride;
@property (Td,R,N,V_minimumBandThickness) minimumBandThickness;
@property (Td,R,N,V_maximumBandThickness) maximumBandThickness;
@property (T@?,C,N,V_viewControllerProvider) viewControllerProvider;
```

## Class methods

```
+[PKToolConfiguration _assetNamesByAzimuthForToolWithIdentifier:];
+[PKToolConfiguration _assetNamesByWeightForToolWithIdentifier:];
+[PKToolConfiguration _deepCopyStrokeWeightDictionary:];
+[PKToolConfiguration _orderedAzimuthValuesForToolWithIdentifier:];
+[PKToolConfiguration _supportsAzimuthControlForToolWithIdentifier:];
+[PKToolConfiguration _weightsForToolWithIdentifier:];
+[PKToolConfiguration defaultConfigurationForToolWithIdentifier:];
+[PKToolConfiguration p_assetImageForToolIdentifier:assetNumber:bundle:];
+[PKToolConfiguration p_azimuthAssetNameForToolIdentifier:assetNumber:];
+[PKToolConfiguration p_bitmapEraserImageWithWeight:imageSize:];
+[PKToolConfiguration p_objectEraserImageWithWeight:imageSize:];
+[PKToolConfiguration p_widthAssetNameForToolIdentifier:assetNumber:];
```

## Instance methods

```
-[PKToolConfiguration setShadowPath:];
-[PKToolConfiguration setLocalizedName:];
-[PKToolConfiguration init];
-[PKToolConfiguration localizedName];
-[PKToolConfiguration shadowPath];
-[PKToolConfiguration defaultColor];
-[PKToolConfiguration hash];
-[PKToolConfiguration image];
-[PKToolConfiguration copyWithZone:];
-[PKToolConfiguration isEqual:];
-[PKToolConfiguration setImage:];
-[PKToolConfiguration setBaseImage:];
-[PKToolConfiguration baseImage];
-[PKToolConfiguration setStrokeWeightsToButtonImages:];
-[PKToolConfiguration supportsOpacity];
-[PKToolConfiguration tipContourImage];
-[PKToolConfiguration bandContourImage];
-[PKToolConfiguration bandMaskImage];
-[PKToolConfiguration bandVerticalOffset];
-[PKToolConfiguration baseImagesForAzimuth];
-[PKToolConfiguration clearTipMaskImageAndShadowPathIncludingTip];
-[PKToolConfiguration initWithLocalizedName:baseImage:shadowPath:];
-[PKToolConfiguration isEraserTool];
-[PKToolConfiguration maximumBandThickness];
-[PKToolConfiguration minimumBandThickness];
-[PKToolConfiguration opacityLabelVerticalOffset];
-[PKToolConfiguration p_strokeWeightRange];
-[PKToolConfiguration setBandContourImage:];
-[PKToolConfiguration setBandMaskImage:];
-[PKToolConfiguration setBandVerticalOffset:];
-[PKToolConfiguration setBaseImagesForAzimuth:];
-[PKToolConfiguration setMinimumBandThickness:andMaximumBandThickness:];
-[PKToolConfiguration setOpacityLabelVerticalOffset:];
-[PKToolConfiguration setSupportsColor:andOpacity:];
-[PKToolConfiguration setSupportsColor:andOpacity:defaultColor:];
-[PKToolConfiguration setTipContourImage:];
-[PKToolConfiguration setTipContourImagesForAzimuth:];
-[PKToolConfiguration setTipMaskImage:withShadowPathIncludingTip:];
-[PKToolConfiguration setTipMaskImagesForAzimuth:];
-[PKToolConfiguration setViewControllerProvider:];
-[PKToolConfiguration setWantsStrokeWeightControl:];
-[PKToolConfiguration shadowPathIncludingTip];
-[PKToolConfiguration strokeWeightButtonSize];
-[PKToolConfiguration strokeWeightsToButtonImages];
-[PKToolConfiguration supportsColor];
-[PKToolConfiguration supportsStrokeWeight];
-[PKToolConfiguration tipContourImagesForAzimuth];
-[PKToolConfiguration tipMaskImage];
-[PKToolConfiguration tipMaskImagesForAzimuth];
-[PKToolConfiguration viewControllerProvider];
-[PKToolConfiguration weightButtonTintColorOverride];
```
