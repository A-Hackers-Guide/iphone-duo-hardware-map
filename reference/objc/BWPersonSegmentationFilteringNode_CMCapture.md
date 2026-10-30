# `BWPersonSegmentationFilteringNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _gpuPriority;
B _frameRateUpsamplingEnabled;
B _alignsMaskWithPrimaryCaptureRect;
B _inferencePreviouslyAttached;
I _inputOrientationRelativeToSensor;
@"FigSemanticStyleFilteringV1" _segmentationMaskFilter;
^{opaqueCMSampleBuffer=} _cachedFilteredMaskSampleBuffer;
^{opaqueCMFormatDescription=} _filteredMaskFormatDescription;
@"<MTLCommandQueue>" _commandQueue;
```

## Class methods

```
+[BWPersonSegmentationFilteringNode initialize];
```

## Instance methods

```
-[BWPersonSegmentationFilteringNode prepareForCurrentConfigurationToBecomeLive];
-[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:];
-[BWPersonSegmentationFilteringNode dealloc];
-[BWPersonSegmentationFilteringNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWPersonSegmentationFilteringNode nodeSubType];
-[BWPersonSegmentationFilteringNode nodeType];
-[BWPersonSegmentationFilteringNode alignsMaskWithPrimaryCaptureRect];
-[BWPersonSegmentationFilteringNode didReachEndOfDataForInput:];
-[BWPersonSegmentationFilteringNode initWithGPUPriority:frameRateUpsamplingEnabled:metalCommandQueue:];
-[BWPersonSegmentationFilteringNode inputOrientationRelativeToSensor];
-[BWPersonSegmentationFilteringNode setAlignsMaskWithPrimaryCaptureRect:];
-[BWPersonSegmentationFilteringNode setInputOrientationRelativeToSensor:];
```
