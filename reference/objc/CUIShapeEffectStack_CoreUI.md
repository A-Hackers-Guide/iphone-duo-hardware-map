# `CUIShapeEffectStack`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 23 properties, 98 instance methods, 28 class methods

## Instance variables

```
f _shapeOpacity;
f _outputOpacity;
I _outputBlendMode;
Q _hueSaturationCount;
^{?=fffffBB} _hueSaturation;
Q _colorOverlayCount;
^{?=IffffB} _colorOverlay;
Q _innerGradientCount;
^{?=Ifffffff} _innerGradient;
Q _innerGlowCount;
^{?=Ifffff} _innerGlow;
Q _innerShadowCount;
^{?=Ifffffff{CGPoint=dd}} _innerShadow;
Q _outerGlowCount;
^{?=ffffff} _outerGlow;
Q _engraveShadowCount;
^{?=ffffffff{CGPoint=dd}} _engraveShadow;
Q _extraShadowCount;
^{?=ffffffff{CGPoint=dd}} _extraShadow;
Q _bevelEmbossCount;
^{?=ffffffffffffI} _emboss;
f _scalefactor;
i _renderStrategy;
B _bypassColorFills;
```

## Properties

```
@property (Tf,R,N,V_shapeOpacity) shapeOpacity;
@property (Tf,R,N,V_outputOpacity) outputOpacity;
@property (TQ,R,N,V_hueSaturationCount) hueSaturationCount;
@property (T^{?=fffffBB},R,N,V_hueSaturation) hueSaturation;
@property (TQ,N,V_colorOverlayCount) colorOverlayCount;
@property (T^{?=IffffB},R,N,V_colorOverlay) colorOverlay;
@property (TQ,N,V_innerGradientCount) innerGradientCount;
@property (T^{?=Ifffffff},R,N,V_innerGradient) innerGradient;
@property (TQ,N,V_innerGlowCount) innerGlowCount;
@property (T^{?=Ifffff},R,N,V_innerGlow) innerGlow;
@property (TQ,N,V_innerShadowCount) innerShadowCount;
@property (T^{?=Ifffffff{CGPoint=dd}},R,N,V_innerShadow) innerShadow;
@property (TQ,R,N,V_outerGlowCount) outerGlowCount;
@property (T^{?=ffffff},R,N,V_outerGlow) outerGlow;
@property (TQ,N,V_engraveShadowCount) engraveShadowCount;
@property (T^{?=ffffffff{CGPoint=dd}},R,N,V_engraveShadow) engraveShadow;
@property (TQ,R,N,V_extraShadowCount) extraShadowCount;
@property (T^{?=ffffffff{CGPoint=dd}},R,N,V_extraShadow) extraShadow;
@property (TQ,R,N,V_bevelEmbossCount) bevelEmbossCount;
@property (T^{?=ffffffffffffI},R,N,V_emboss) emboss;
@property (Tf,R,N,V_scalefactor) scalefactor;
@property (Ti,R,N,V_renderStrategy) renderStrategy;
@property (TI,R,V_outputBlendMode) outputBlendMode;
```

## Class methods

```
+[CUIShapeEffectStack colorWithRed:green:blue:alpha:];
+[CUIShapeEffectStack sharedCIContext];
+[CUIShapeEffectStack composite:into:];
+[CUIShapeEffectStack composite:atop:];
+[CUIShapeEffectStack composite:over:];
+[CUIShapeEffectStack invert:];
+[CUIShapeEffectStack adjustOpacity:by:];
+[CUIShapeEffectStack bevelEmbossFrom:withSize:soften:angle:altitude:highlightRed:highlightGreen:highlightBlue:highlightOpacity:shadowRed:shadowGreen:shadowBlue:shadowOpacity:bevelStyle:];
+[CUIShapeEffectStack blend:over:blendKind:];
+[CUIShapeEffectStack blur:radius:];
+[CUIShapeEffectStack colorWithGray:alpha:];
+[CUIShapeEffectStack composite:outOf:];
+[CUIShapeEffectStack gradientWithParameters:inRect:];
+[CUIShapeEffectStack hueSaturationFrom:withCenterAngle:width:tintRed:tintGreen:tintBlue:];
+[CUIShapeEffectStack image:withOpacity:];
+[CUIShapeEffectStack imageFromBlendWithMask:foreground:background:];
+[CUIShapeEffectStack innerGlowFrom:withRadius:red:green:blue:opacity:];
+[CUIShapeEffectStack innerShadowFrom:withOffset:radius:red:green:blue:opacity:];
+[CUIShapeEffectStack newColorByAdjustingLightnessOfColor:darker:];
+[CUIShapeEffectStack offset:by:];
+[CUIShapeEffectStack outerGlowFrom:withSize:spread:red:green:blue:opacity:];
+[CUIShapeEffectStack outerShadowFrom:withOffset:size:spread:red:green:blue:opacity:];
+[CUIShapeEffectStack pixelZoomed:scale:about:];
+[CUIShapeEffectStack preferredCIContextOptions];
+[CUIShapeEffectStack rectangle:withRed:green:blue:alpha:];
+[CUIShapeEffectStack shadowFrom:red:green:blue:opacity:];
+[CUIShapeEffectStack shapeEffectSingleBlurFrom:withInteriorFill:offset:blurSize:innerGlowRed:innerGlowGreen:innerGlowBlue:innerGlowOpacity:innerShadowRed:innerShadowGreen:innerShadowBlue:innerShadowOpacity:outerGlowRed:outerGlowGreen:outerGlowBlue:outerGlowOpacity:outerShadowRed:outerShadowGreen:outerShadowBlue:outerShadowOpacity:hasInsideShadowBlur:hasOutsideShadowBlur:];
+[CUIShapeEffectStack unsharpMask:radius:intensity:];
```

## Instance methods

```
-[CUIShapeEffectStack cacheKey];
-[CUIShapeEffectStack dealloc];
-[CUIShapeEffectStack hasEffects];
-[CUIShapeEffectStack anyEffectAllowsTintSubstitution];
-[CUIShapeEffectStack hasColorOverlay];
-[CUIShapeEffectStack outputBlendMode];
-[CUIShapeEffectStack _cleanupEffectSettings];
-[CUIShapeEffectStack _newFlattenedImageFromShapeCGImage:withScale:ciContext:blendOverImage:];
-[CUIShapeEffectStack _normalizeEffectParameters];
-[CUIShapeEffectStack _precompositeColorOverlayInnerGradient];
-[CUIShapeEffectStack _setBevelEmbossAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setColorFillAtIndex:FromPreset:index:];
-[CUIShapeEffectStack _setEngraveShadowAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setExtraShadowAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setHueSaturationAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setInnerGlowAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setInnerShadowAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setInteriorGradientAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setOuterGlowAtIndex:fromPreset:index:];
-[CUIShapeEffectStack _setOutputOpacityFromPreset:atIndex:];
-[CUIShapeEffectStack _setShapeOpacityFromPreset:atIndex:];
-[CUIShapeEffectStack _updateRenderStrategyFromEffect:];
-[CUIShapeEffectStack adjustEffectColorsToTemperature:onlyTintableColors:];
-[CUIShapeEffectStack applyCustomForegroundColor:];
-[CUIShapeEffectStack applyCustomForegroundColor:tintEffectColors:];
-[CUIShapeEffectStack bevelEmbossCount];
-[CUIShapeEffectStack cgBlendModeForOutputBlending];
-[CUIShapeEffectStack colorOverlay];
-[CUIShapeEffectStack colorOverlayCount];
-[CUIShapeEffectStack colorOverlayOpacity];
-[CUIShapeEffectStack compositeEffectStackWithShapeImage:withScale:blendOntoImage:];
-[CUIShapeEffectStack effectInsetsWithScale:];
-[CUIShapeEffectStack effectPaddingWithScale:];
-[CUIShapeEffectStack effectPreset];
-[CUIShapeEffectStack emboss];
-[CUIShapeEffectStack engraveShadow];
-[CUIShapeEffectStack engraveShadowCount];
-[CUIShapeEffectStack expressableByColorFillCheckingOutputBlending:];
-[CUIShapeEffectStack extraShadow];
-[CUIShapeEffectStack extraShadowCount];
-[CUIShapeEffectStack hasBevelEmboss];
-[CUIShapeEffectStack hasEngraveShadow];
-[CUIShapeEffectStack hasExtraShadow];
-[CUIShapeEffectStack hasHueSaturation];
-[CUIShapeEffectStack hasInnerGlow];
-[CUIShapeEffectStack hasInnerGradient];
-[CUIShapeEffectStack hasInnerShadow];
-[CUIShapeEffectStack hasOuterGlow];
-[CUIShapeEffectStack hueSaturation];
-[CUIShapeEffectStack hueSaturationCount];
-[CUIShapeEffectStack image:withAdjustedOpacity:];
-[CUIShapeEffectStack imageWithBevelEmbossOfImage:effect:];
-[CUIShapeEffectStack imageWithColorOverlayOfImage:effect:];
-[CUIShapeEffectStack imageWithEngraveShadowOfImage:effect:];
-[CUIShapeEffectStack imageWithExtraShadowOfImage:effect:];
-[CUIShapeEffectStack imageWithHueSaturationOfImage:effect:];
-[CUIShapeEffectStack imageWithInnerGlowOfImage:effect:];
-[CUIShapeEffectStack imageWithInnerShadowOfImage:effect:];
-[CUIShapeEffectStack imageWithInteriorGradientFillOfImage:effect:];
-[CUIShapeEffectStack imageWithOuterGlowOfImage:effect:];
-[CUIShapeEffectStack imageWithSingleBlurShapeEffectOfImage:withInteriorFill:];
-[CUIShapeEffectStack initWithEffectPreset:];
-[CUIShapeEffectStack innerGlow];
-[CUIShapeEffectStack innerGlowCount];
-[CUIShapeEffectStack innerGradient];
-[CUIShapeEffectStack innerGradientCount];
-[CUIShapeEffectStack innerGradientOpacity];
-[CUIShapeEffectStack innerShadow];
-[CUIShapeEffectStack innerShadowCount];
-[CUIShapeEffectStack newColorByProcessingColor:];
-[CUIShapeEffectStack newFlattenedImageFromCGImage:withScale:ciContext:];
-[CUIShapeEffectStack newFlattenedImageFromShapeCGImage:];
-[CUIShapeEffectStack newFlattenedImageFromShapeCGImage:withScale:];
-[CUIShapeEffectStack newFlattenedImageFromShapeCGImage:withScale:cache:];
-[CUIShapeEffectStack newFlattenedImageFromShapeCGImage:withScale:ciContext:];
-[CUIShapeEffectStack optimizedSingleBlurEffectCompositeWithShapeImage:];
-[CUIShapeEffectStack outerGlow];
-[CUIShapeEffectStack outerGlowCount];
-[CUIShapeEffectStack outputOpacity];
-[CUIShapeEffectStack processedImageFromImage:];
-[CUIShapeEffectStack processedImageFromImage:withScale:];
-[CUIShapeEffectStack processedImageFromShapeImage:];
-[CUIShapeEffectStack processedImageFromShapeImage:withScale:];
-[CUIShapeEffectStack processedImageFromShapeImage:withScale:invertShadows:];
-[CUIShapeEffectStack processedImageFromShapePath:inRect:];
-[CUIShapeEffectStack renderStrategy];
-[CUIShapeEffectStack scaleBrightnessOfEffectColorsByAmount:onlyTintableColors:];
-[CUIShapeEffectStack scaleEffectParametersBy:];
-[CUIShapeEffectStack scalefactor];
-[CUIShapeEffectStack setBypassColorFills:];
-[CUIShapeEffectStack setColorOverlayCount:];
-[CUIShapeEffectStack setEngraveShadowCount:];
-[CUIShapeEffectStack setInnerGlowCount:];
-[CUIShapeEffectStack setInnerGradientCount:];
-[CUIShapeEffectStack setInnerShadowCount:];
-[CUIShapeEffectStack shapeOpacity];
-[CUIShapeEffectStack standardEffectCompositeWithShapeImage:blendOntoImage:];
-[CUIShapeEffectStack updateOutputBlendingWithInteriorFillHeuristic];
```
