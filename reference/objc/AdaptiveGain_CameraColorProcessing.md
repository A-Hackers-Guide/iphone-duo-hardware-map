# `AdaptiveGain`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLComputePipelineState>" _computePipelineHistogramGeneration;
@"<MTLTexture>" _inputRGBTexture;
_adaptiveGainValue;
@"<MTLBuffer>" _globalHistBuffer;
{?="LumShift"I"CoeffAvgY"[3I]"CoeffMaxY"[3I]"AvgYOffset"I} _lumaParams;
{SourceROI="StartX"I"StartY"I"EndX"I"EndY"I} _globalHistSourceROI;
```

## Properties

```
@property (T@"<MTLTexture>",&,N,V_inputRGBTexture) inputRGBTexture;
@property (T{SourceROI=IIII},N,V_globalHistSourceROI) globalHistSourceROI;
```

## Instance methods

```
-[AdaptiveGain configure];
-[AdaptiveGain inputRGBTexture];
-[AdaptiveGain createShaders];
-[AdaptiveGain initWithMetalContext:];
-[AdaptiveGain setInputRGBTexture:];
-[AdaptiveGain releaseTextures];
-[AdaptiveGain allocInternalData];
-[AdaptiveGain computeGain:withTargetRange:];
-[AdaptiveGain globalHistSourceROI];
-[AdaptiveGain setGlobalHistSourceROI:];
```
