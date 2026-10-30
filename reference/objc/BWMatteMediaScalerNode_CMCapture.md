# `BWMatteMediaScalerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 8 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _outputFormatDescription;
i _poolBaseCapacity;
@"NSDictionary" _mainImageDownscalingFactorByAttachedMediaKey;
@"NSDictionary" _outputSizeByAttachedMediaKey;
@"NSMutableDictionary" _pixelBufferPoolByAttachedMediaKey;
^{OpaqueVTPixelTransferSession=} _attachedMediaScalingSession;
B _backPressureDrivenPipelining;
B _preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer;
```

## Class methods

```
+[BWMatteMediaScalerNode initialize];
```

## Instance methods

```
-[BWMatteMediaScalerNode backPressureDrivenPipelining];
-[BWMatteMediaScalerNode setPreferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer:];
-[BWMatteMediaScalerNode mainImageDownscalingFactorByAttachedMediaKey];
-[BWMatteMediaScalerNode renderSampleBuffer:forInput:];
-[BWMatteMediaScalerNode setBackPressureDrivenPipelining:];
-[BWMatteMediaScalerNode outputSizeByAttachedMediaKey];
-[BWMatteMediaScalerNode preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer];
-[BWMatteMediaScalerNode dealloc];
-[BWMatteMediaScalerNode setMainImageDownscalingFactorByAttachedMediaKey:];
-[BWMatteMediaScalerNode didReachEndOfDataForConfigurationID:input:];
-[BWMatteMediaScalerNode initWithBasePoolCapacity:];
-[BWMatteMediaScalerNode setOutputSizeByAttachedMediaKey:];
-[BWMatteMediaScalerNode nodeSubType];
-[BWMatteMediaScalerNode didSelectFormat:forInput:];
-[BWMatteMediaScalerNode nodeType];
```
