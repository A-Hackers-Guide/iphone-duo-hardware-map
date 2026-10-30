# `PKInkBehavior`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 37 instance variables, 21 properties, 43 instance methods, 2 class methods

## Instance variables

```
B _usesAzimuthOrAltitude;
B _showBrushIndicator;
d _rulerOffsetScale;
d _rulerOffsetConstant;
@"NSMutableArray" _cachedRadiusFunctions;
@"NSMutableArray" _cachedRadius2Functions;
@"NSMutableArray" _cachedThresholdFunctions;
@"NSMutableArray" _cachedAzimuthFunctions;
@"NSMutableArray" _cachedOpacityFunctions;
@"NSMutableArray" _cachedEdgeWidthFunctions;
@"NSMutableArray" _cachedAspectRatioFunctions;
{unique_ptr<PKFunction, std::default_delete<PKFunction>>=""{?="__ptr_"^{PKFunction}}} _weightFunction;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _radiusOutput;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _radius2Output;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _thresholdOutput;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _azimuthOutput;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _opacityOutput;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _edgeWidthOutput;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _aspectRatioOutput;
{vector<PKOutputFunction, std::allocator<PKOutputFunction>>="__begin_"^{PKOutputFunction}"__end_"^{PKOutputFunction}""{?="__cap_"^{PKOutputFunction}}} _brushOpacityOutput;
B _useUnclampedWeight;
B _supportsCombiningStrokes;
B _uiAzimuthControl;
@"NSString" _identifier;
Q _version;
@"NSString" _variant;
@"PKInkRenderingDescriptor" _renderingDescriptor;
d _blendAlpha;
d _targetMultiple;
d _baseAlpha;
@"PKInkSmoothingDescriptor" _smoothingDescriptor;
@"PKInkFeatheringDescriptor" _featheringDescriptor;
@"PKInkFeatheringDescriptor" _pencilFeatheringDescriptor;
@"PKInkAnimationDescriptor" _animationDescriptor;
@"NSArray" _uiWidths;
d _defaultWidth;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _inkTransform;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (TQ,R,N,V_version) version;
@property (T@"NSString",R,N,V_variant) variant;
@property (T@"PKInkRenderingDescriptor",R,N,V_renderingDescriptor) renderingDescriptor;
@property (T@"PKInkParticleDescriptor",R,N) particleDescriptor;
@property (T@"PKInkParticleDescriptor",R,N) secondaryParticleDescriptor;
@property (T@"NSArray",R,D,N) inkFunctions;
@property (Td,N,V_blendAlpha) blendAlpha;
@property (Td,N,V_targetMultiple) targetMultiple;
@property (Td,N,V_baseAlpha) baseAlpha;
@property (TB,N,V_useUnclampedWeight) useUnclampedWeight;
@property (T{CGAffineTransform=dddddd},N,V_inkTransform) inkTransform;
@property (TB,N,V_supportsCombiningStrokes) supportsCombiningStrokes;
@property (T@"NSArray",C,N,V_uiWidths) uiWidths;
@property (TB,N,V_uiAzimuthControl) uiAzimuthControl;
@property (Td,N,V_defaultWidth) defaultWidth;
@property (T@"PKInkSmoothingDescriptor",&,N,V_smoothingDescriptor) smoothingDescriptor;
@property (T@"PKInkFeatheringDescriptor",&,N,V_featheringDescriptor) featheringDescriptor;
@property (T@"PKInkFeatheringDescriptor",&,N,V_pencilFeatheringDescriptor) pencilFeatheringDescriptor;
@property (T@"PKInkAnimationDescriptor",&,N,V_animationDescriptor) animationDescriptor;
@property (TB,R,D,N) isEraser;
```

## Class methods

```
+[PKInkBehavior inkRadiusOverride];
+[PKInkBehavior loadInkV2WithURL:];
```

## Instance methods

```
-[PKInkBehavior identifier];
-[PKInkBehavior version];
-[PKInkBehavior description];
-[PKInkBehavior defaultWidth];
-[PKInkBehavior mutableCopy];
-[PKInkBehavior variant];
-[PKInkBehavior _calculateUsesAzimuthOrAltitude];
-[PKInkBehavior addNewInkFunction:];
-[PKInkBehavior animationDescriptor];
-[PKInkBehavior baseAlpha];
-[PKInkBehavior blendAlpha];
-[PKInkBehavior featheringDescriptor];
-[PKInkBehavior initWithRenderingDescriptor:blendAlpha:targetMultiple:baseAlpha:inkTransform:useUnclampedWeight:smoothingDescriptor:featheringDescriptor:pencilFeatheringDescriptor:animationDescriptor:identifier:version:variant:uiWidths:defaultWidth:uiAzimuthControl:showBrushIndicator:supportsCombiningStrokes:rulerOffsetScale:rulerOffsetConstant:weightFunction:inkFunctions:];
-[PKInkBehavior initWithRenderingDescriptor:blendAlpha:targetMultiple:baseAlpha:inkTransform:useUnclampedWeight:smoothingDescriptor:featheringDescriptor:pencilFeatheringDescriptor:animationDescriptor:identifier:version:variant:uiWidths:defaultWidth:uiAzimuthControl:showBrushIndicator:supportsCombiningStrokes:rulerOffsetScale:rulerOffsetConstant:weightFunction:radiusOutput:radius2Output:azimuthOutput:thresholdOutput:opacityOutput:edgeWidthOutput:aspectRatioOutput:brushOpacityOutput:];
-[PKInkBehavior initWithRenderingDescriptor:variant:];
-[PKInkBehavior inkFunctionDidChange:];
-[PKInkBehavior inkFunctions];
-[PKInkBehavior inkTransform];
-[PKInkBehavior isEraser];
-[PKInkBehavior particleDescriptor];
-[PKInkBehavior pencilFeatheringDescriptor];
-[PKInkBehavior removeInkFunction:];
-[PKInkBehavior renderingDescriptor];
-[PKInkBehavior secondaryParticleDescriptor];
-[PKInkBehavior setAnimationDescriptor:];
-[PKInkBehavior setBaseAlpha:];
-[PKInkBehavior setBlendAlpha:];
-[PKInkBehavior setDefaultWidth:];
-[PKInkBehavior setFeatheringDescriptor:];
-[PKInkBehavior setInkTransform:];
-[PKInkBehavior setPencilFeatheringDescriptor:];
-[PKInkBehavior setSmoothingDescriptor:];
-[PKInkBehavior setSupportsCombiningStrokes:];
-[PKInkBehavior setTargetMultiple:];
-[PKInkBehavior setUiAzimuthControl:];
-[PKInkBehavior setUiWidths:];
-[PKInkBehavior setUseUnclampedWeight:];
-[PKInkBehavior smoothingDescriptor];
-[PKInkBehavior supportsCombiningStrokes];
-[PKInkBehavior targetMultiple];
-[PKInkBehavior uiAzimuthControl];
-[PKInkBehavior uiWidths];
-[PKInkBehavior useUnclampedWeight];
```
