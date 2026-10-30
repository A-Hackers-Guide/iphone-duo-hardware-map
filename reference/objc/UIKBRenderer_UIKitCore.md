# `UIKBRenderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 15 properties, 68 instance methods, 3 class methods

## Instance variables

```
^{CGContext=} _cachingContext;
@? _cachingContextCompletion;
q _forceColorFormat;
@"UIColor" _singleColor;
i _colorCount;
B _opaque;
B _colorDetectMode;
B _disableInternalCaching;
^{CGContext=} _ctx;
d _scale;
q _renderFlags;
@"NSString" _cacheKey;
@"UIImage" _renderedImage;
q _contentColorFormat;
q _assetIdiom;
d __layerRoundRectRadius;
{CGSize="width"d"height"d} _size;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __layerPaddedFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V__layerPaddedFrame) _layerPaddedFrame;
@property (Td,N,V__layerRoundRectRadius) _layerRoundRectRadius;
@property (T^{CGContext=},R,N,V_ctx) context;
@property (T@"NSData",R,N) contextData;
@property (T{CGSize=dd},R,N,V_size) size;
@property (Td,R,N,V_scale) scale;
@property (TB,R,N,V_opaque) opaque;
@property (Tq,R,N,V_renderFlags) renderFlags;
@property (T@"UIImage",R,N,V_renderedImage) renderedImage;
@property (Tq,R,N,V_contentColorFormat) contentColorFormat;
@property (T@"UIColor",R,N) singleColor;
@property (T@"NSString",&,N,V_cacheKey) cacheKey;
@property (TB,N,V_colorDetectMode) colorDetectMode;
@property (TB,N,V_disableInternalCaching) disableInternalCaching;
@property (Tq,R,N,V_assetIdiom) assetIdiom;
```

## Class methods

```
+[UIKBRenderer clearInternalCaches];
+[UIKBRenderer imageContextWithSize:scale:colorFormat:opaque:invert:];
+[UIKBRenderer rendererWithContext:withSize:withScale:opaque:renderFlags:assetIdiom:];
```

## Instance methods

```
-[UIKBRenderer assetIdiom];
-[UIKBRenderer opaque];
-[UIKBRenderer cacheKey];
-[UIKBRenderer renderFlags];
-[UIKBRenderer dealloc];
-[UIKBRenderer contextData];
-[UIKBRenderer renderedImage];
-[UIKBRenderer size];
-[UIKBRenderer scale];
-[UIKBRenderer description];
-[UIKBRenderer context];
-[UIKBRenderer colorDetectMode];
-[UIKBRenderer addPathForFlickPopupGeometries:];
-[UIKBRenderer _addDetectedColor:];
-[UIKBRenderer _completeCacheImageWithTraitsIfNecessary:];
-[UIKBRenderer _deleteGlyphPaths];
-[UIKBRenderer _drawKeyImage:inRect:withStyle:force1xImages:flipHorizontally:isRGBImage:];
-[UIKBRenderer _drawKeyString:inRect:withStyle:];
-[UIKBRenderer _drawLinearGradient:inRect:];
-[UIKBRenderer _drawSingleSymbol:inRect:withStyle:];
-[UIKBRenderer _layerPaddedFrame];
-[UIKBRenderer _layerRoundRectRadius];
-[UIKBRenderer _renderVariantsFromKeyContents:withTraits:];
-[UIKBRenderer _thickShiftGlyphPath];
-[UIKBRenderer _thinShiftGlyphPath];
-[UIKBRenderer addPathForFlickGeometry:];
-[UIKBRenderer addPathForRenderGeometry:];
-[UIKBRenderer addPathForSplitGeometry:];
-[UIKBRenderer addPathForTraits:displayRect:];
-[UIKBRenderer addRoundRect:radius:corners:];
-[UIKBRenderer centroidOfGlyph:];
-[UIKBRenderer contentColorFormat];
-[UIKBRenderer defaultPathForRenderGeometry:];
-[UIKBRenderer detectColorsForEffect:];
-[UIKBRenderer detectColorsForGradient:];
-[UIKBRenderer detectColorsForNamedColor:];
-[UIKBRenderer disableInternalCaching];
-[UIKBRenderer drawPath:weight:transform:color:fill:];
-[UIKBRenderer drawShiftPath:weight:transform:color:];
-[UIKBRenderer ensureContext];
-[UIKBRenderer forceColorFormat:];
-[UIKBRenderer initWithContext:withSize:withScale:opaque:renderFlags:assetIdiom:];
-[UIKBRenderer loadCachedImageForHashString:];
-[UIKBRenderer pathForConcaveCornerWithGeometry:];
-[UIKBRenderer pathForFlickGeometry:];
-[UIKBRenderer pathForFlickPopupGeometries:];
-[UIKBRenderer pathForFlickWidth:height:handleLength:keyMiddle:angle:radius:];
-[UIKBRenderer pathForRenderGeometry:];
-[UIKBRenderer pathForSplitGeometry:];
-[UIKBRenderer renderBackgroundTraits:];
-[UIKBRenderer renderBackgroundTraits:allowCaching:];
-[UIKBRenderer renderDivotEffect:withTraits:];
-[UIKBRenderer renderEdgeEffect:withTraits:];
-[UIKBRenderer renderKeyContents:withTraits:];
-[UIKBRenderer renderKeyImageContents:withTraits:status:];
-[UIKBRenderer renderKeyPathContents:withTraits:];
-[UIKBRenderer renderKeyStringContents:withTraits:status:];
-[UIKBRenderer renderNullEffect:withTraits:];
-[UIKBRenderer renderShadowEffect:withTraits:];
-[UIKBRenderer setCacheKey:];
-[UIKBRenderer setColorDetectMode:];
-[UIKBRenderer setDisableInternalCaching:];
-[UIKBRenderer set_layerPaddedFrame:];
-[UIKBRenderer set_layerRoundRectRadius:];
-[UIKBRenderer singleColor];
-[UIKBRenderer symbolImageConfigForKey:traitCollection:];
-[UIKBRenderer symbolImageRenderingModeForIdiom:];
-[UIKBRenderer watchPathForRenderGeometry:];
```
