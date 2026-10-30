# `JFXEffectsPreviewGenerationRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 36 instance methods, 2 class methods

## Instance variables

```
B _highQuality;
B _scaleAnimationTransformInfoToOutputSize;
i _priority;
I _parentCode;
I _childCode;
@"PVImageBuffer" _image;
@"JFXEffect" _generatorEffect;
@"NSArray" _effectStack;
@"NSDictionary" _customRenderingProperties;
@"NSArray" _pickerPreviewEffectList;
{CGSize="width"d"height"d} _outputSize;
{CGSize="width"d"height"d} _frameSize;
{?="value"q"timescale"i"flags"I"epoch"q} _renderTime;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _userSourceTransform;
{PVTransformAnimationInfo="time"{?="value"q"timescale"i"flags"I"epoch"q}"translation"{CGPoint="x"d"y"d}"scale"d"rotation"d} _animationTransformInfo;
```

## Properties

```
@property (TB,N,V_scaleAnimationTransformInfoToOutputSize) scaleAnimationTransformInfoToOutputSize;
@property (T@"PVImageBuffer",R,N,V_image) image;
@property (T@"JFXEffect",R,N,V_generatorEffect) generatorEffect;
@property (T@"NSArray",R,N,V_effectStack) effectStack;
@property (T{CGSize=dd},R,N,V_outputSize) outputSize;
@property (T{CGSize=dd},R,N,V_frameSize) frameSize;
@property (T{?=qiIq},R,N,V_renderTime) renderTime;
@property (T{CGAffineTransform=dddddd},N,V_userSourceTransform) userSourceTransform;
@property (T@"NSDictionary",C,N,V_customRenderingProperties) customRenderingProperties;
@property (T@"NSArray",&,N,V_pickerPreviewEffectList) pickerPreviewEffectList;
@property (T{PVTransformAnimationInfo={?=qiIq}{CGPoint=dd}dd},N,V_animationTransformInfo) animationTransformInfo;
@property (TB,N,V_highQuality) highQuality;
@property (Ti,N,V_priority) priority;
@property (TI,N,V_parentCode) parentCode;
@property (TI,N,V_childCode) childCode;
```

## Class methods

```
+[JFXEffectsPreviewGenerationRequest JT_centerRect:aspectRatio:];
+[JFXEffectsPreviewGenerationRequest centerAnimationInfoForOutputSize:imageRect:];
```

## Instance methods

```
-[JFXEffectsPreviewGenerationRequest priority];
-[JFXEffectsPreviewGenerationRequest setPriority:];
-[JFXEffectsPreviewGenerationRequest image];
-[JFXEffectsPreviewGenerationRequest frameSize];
-[JFXEffectsPreviewGenerationRequest outputSize];
-[JFXEffectsPreviewGenerationRequest highQuality];
-[JFXEffectsPreviewGenerationRequest renderTime];
-[JFXEffectsPreviewGenerationRequest setHighQuality:];
-[JFXEffectsPreviewGenerationRequest sourceTransform];
-[JFXEffectsPreviewGenerationRequest JFX_scaleToFitSize:withTransform:];
-[JFXEffectsPreviewGenerationRequest generatorEffect];
-[JFXEffectsPreviewGenerationRequest _scaleAndTransformToFitSize:];
-[JFXEffectsPreviewGenerationRequest animationTransformInfo];
-[JFXEffectsPreviewGenerationRequest centerAnimationInfo];
-[JFXEffectsPreviewGenerationRequest childCode];
-[JFXEffectsPreviewGenerationRequest customRenderingProperties];
-[JFXEffectsPreviewGenerationRequest effectStack];
-[JFXEffectsPreviewGenerationRequest generatorJobWithGraphBuilder:];
-[JFXEffectsPreviewGenerationRequest initWithInput:effectStack:outputSize:frameSize:renderTime:];
-[JFXEffectsPreviewGenerationRequest initWithInput:effectStack:outputSize:renderTime:];
-[JFXEffectsPreviewGenerationRequest initWithInputGenerator:effectStack:outputSize:frameSize:renderTime:];
-[JFXEffectsPreviewGenerationRequest initWithInputGenerator:effectStack:outputSize:renderTime:];
-[JFXEffectsPreviewGenerationRequest parentCode];
-[JFXEffectsPreviewGenerationRequest pickerPreviewEffectList];
-[JFXEffectsPreviewGenerationRequest placeholderGeneratorBackground];
-[JFXEffectsPreviewGenerationRequest scaleAnimationTransformInfoToOutputSize];
-[JFXEffectsPreviewGenerationRequest setAnimationTransformInfo:];
-[JFXEffectsPreviewGenerationRequest setChildCode:];
-[JFXEffectsPreviewGenerationRequest setCustomRenderingProperties:];
-[JFXEffectsPreviewGenerationRequest setParentCode:];
-[JFXEffectsPreviewGenerationRequest setPickerPreviewEffectList:];
-[JFXEffectsPreviewGenerationRequest setScaleAnimationTransformInfoToOutputSize:];
-[JFXEffectsPreviewGenerationRequest setTransformAnimationInfo:scaleToOutput:];
-[JFXEffectsPreviewGenerationRequest setUserSourceTransform:];
-[JFXEffectsPreviewGenerationRequest sourceIGNodeUsingGraphBuilder:includeAnimoji:];
-[JFXEffectsPreviewGenerationRequest userSourceTransform];
```
