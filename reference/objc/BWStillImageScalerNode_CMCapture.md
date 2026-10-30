# `BWStillImageScalerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 14 instance variables, 1 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
^{opaqueCMFormatDescription=} _outputFormatDescription;
i _poolBaseCapacity;
@"BWPixelBufferPool" _pool;
^{OpaqueVTPixelTransferSession=} _scalingSession;
B _blackFillingRequired;
B _enforcesZoomingForPortraitCaptures;
@"NSDictionary" _mainImageDownscalingFactorByAttachedMediaKey;
@"NSDictionary" _outputSizeByAttachedMediaKey;
@"NSMutableDictionary" _pixelBufferPoolByAttachedMediaKey;
^{OpaqueVTPixelTransferSession=} _attachedMediaScalingSession;
B _backPressureDrivenPipelining;
{?="width"i"height"i} _resizedOutputDimensions;
B _preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer;
```

## Properties

```
@property (T{?=ii},N) resizedOutputDimensions;
```

## Class methods

```
+[BWStillImageScalerNode initialize];
```

## Instance methods

```
-[BWStillImageScalerNode backPressureDrivenPipelining];
-[BWStillImageScalerNode setPreferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer:];
-[BWStillImageScalerNode mainImageDownscalingFactorByAttachedMediaKey];
-[BWStillImageScalerNode setResizedOutputDimensions:];
-[BWStillImageScalerNode initWithBasePoolCapacity:nodeConfiguration:];
-[BWStillImageScalerNode renderSampleBuffer:forInput:];
-[BWStillImageScalerNode setBackPressureDrivenPipelining:];
-[BWStillImageScalerNode outputSizeByAttachedMediaKey];
-[BWStillImageScalerNode preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer];
-[BWStillImageScalerNode setEnforcesZoomingForPortraitCaptures:];
-[BWStillImageScalerNode dealloc];
-[BWStillImageScalerNode enforcesZoomingForPortraitCaptures];
-[BWStillImageScalerNode blackFillingRequired];
-[BWStillImageScalerNode setMainImageDownscalingFactorByAttachedMediaKey:];
-[BWStillImageScalerNode resizedOutputDimensions];
-[BWStillImageScalerNode didReachEndOfDataForConfigurationID:input:];
-[BWStillImageScalerNode setBlackFillingRequired:];
-[BWStillImageScalerNode setOutputSizeByAttachedMediaKey:];
-[BWStillImageScalerNode nodeSubType];
-[BWStillImageScalerNode didSelectFormat:forInput:];
-[BWStillImageScalerNode nodeType];
```
