# `JFXInstructionGraphBuilder`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 20 instance methods, 3 class methods

## Instance variables

```
i _renderingIntent;
@"PVColorSpace" _outputColorSpace;
{CGSize="width"d"height"d} _outputSize;
{CGSize="width"d"height"d} _frameSize;
```

## Properties

```
@property (T{CGSize=dd},R,N,V_outputSize) outputSize;
@property (T{CGSize=dd},R,N,V_frameSize) frameSize;
@property (T@"PVColorSpace",&,N,V_outputColorSpace) outputColorSpace;
@property (Ti,N,V_renderingIntent) renderingIntent;
```

## Class methods

```
+[JFXInstructionGraphBuilder JFX_transformNode:scale:];
+[JFXInstructionGraphBuilder JFX_maskNode:maskRect:basisSize:];
+[JFXInstructionGraphBuilder JFX_scaleForMediaSize:mediaContentMode:clipAspectRatio:outputSize:outputContentMode:];
```

## Instance methods

```
-[JFXInstructionGraphBuilder frameSize];
-[JFXInstructionGraphBuilder outputSize];
-[JFXInstructionGraphBuilder outputColorSpace];
-[JFXInstructionGraphBuilder renderingIntent];
-[JFXInstructionGraphBuilder JFX_applyCustomRenderingPropertiesToInputNode:customRendererProperties:transformAnimation:transformAnimationContentMode:mediaScale:];
-[JFXInstructionGraphBuilder JFX_mediaTransformAnimationForPlayableElement:liveTransform:];
-[JFXInstructionGraphBuilder JFX_calculateCompositeNodeTransformForCropWithCompositeNodeOutputSize:mediaScale:];
-[JFXInstructionGraphBuilder _buildTestXFormAnimation:baseTransform:clipNaturalSize:];
-[JFXInstructionGraphBuilder _sourceNodeForStillMediaItem:sourceTransform:transformAnimation:transformAnimationContentMode:presentationRange:];
-[JFXInstructionGraphBuilder _sourceNodeForVideoMediaItem:sourceTransform:compositionTrackID:transformAnimation:transformAnimationContentMode:];
-[JFXInstructionGraphBuilder applyEffectStack:presentationRange:toInput:];
-[JFXInstructionGraphBuilder applyEffectStack:toInput:];
-[JFXInstructionGraphBuilder blendNodeForClipSourceNodes:];
-[JFXInstructionGraphBuilder initWithOutputSize:frameSize:outputColorSpace:];
-[JFXInstructionGraphBuilder instructionGraphForPlayableElement:presentationTimeRange:sourceTransform:compositionTrackID:liveTransform:excludingEffectType:customRendererProperties:];
-[JFXInstructionGraphBuilder setOutputColorSpace:];
-[JFXInstructionGraphBuilder setRenderingIntent:];
-[JFXInstructionGraphBuilder sourceNodeForGeneratorEffect:effectRange:];
-[JFXInstructionGraphBuilder sourceNodeForImageBuffer:sourceTransform:];
-[JFXInstructionGraphBuilder sourceNodeForMediaItem:sourceTransform:compositionTrackID:transformAnimation:transformAnimationContentMode:presentationTimeRange:mediaScale:playableAspectRatio:playableAspectRatioPreservationMode:];
```
