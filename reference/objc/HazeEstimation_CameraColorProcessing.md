# `HazeEstimation`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLComputePipelineState>" _computePipelineHazeThumbnailGeneration;
@"<MTLCommandQueue>" _commandQueue;
B _hazeConfigured;
@"HazeProperties" _hazeProperties;
@"<MTLTexture>" _inputRGBTexture;
_hazeValue;
{SourceROI="StartX"I"StartY"I"EndX"I"EndY"I} _hazeROI;
_hazeValueForLTM;
```

## Properties

```
@property (T@"<MTLTexture>",&,N,V_inputRGBTexture) inputRGBTexture;
@property (T,N,V_hazeValue) hazeValue;
@property (T,N,V_hazeValueForLTM) hazeValueForLTM;
@property (T@"HazeProperties",&,N,V_hazeProperties) hazeProperties;
@property (T{SourceROI=IIII},N,V_hazeROI) hazeROI;
```

## Instance methods

```
-[HazeEstimation configure];
-[HazeEstimation purgeResources];
-[HazeEstimation inputRGBTexture];
-[HazeEstimation estimateHaze:];
-[HazeEstimation hazeROI];
-[HazeEstimation calculateHazeValues:pixels:thresh:properties:];
-[HazeEstimation setHazeValueForLTM:];
-[HazeEstimation setHazeProperties:];
-[HazeEstimation createShaders];
-[HazeEstimation hazeValue];
-[HazeEstimation setHazeValue:];
-[HazeEstimation hazeValueForLTM];
-[HazeEstimation initWithMetalContext:];
-[HazeEstimation prepareThumbnail:];
-[HazeEstimation hazeProperties];
-[HazeEstimation setInputRGBTexture:];
-[HazeEstimation run];
-[HazeEstimation setHazeROI:];
```
