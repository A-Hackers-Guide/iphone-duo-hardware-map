# `BWStreamingPersonSegmentationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _inputRotationAngle;
B _propagateColorInput;
B _cropColorInputToPrimaryCaptureRect;
B _useLowFrameRateOptimizedNetwork;
@"NSString" _alternativeStreamingPersonSegmentationMaskKey;
@"NSString" _alternativeStreamingSkinSegmentationMaskKey;
```

## Properties

```
@property (Ti,N,V_inputRotationAngle) inputRotationAngle;
@property (TB,N,V_propagateColorInput) propagateColorInput;
@property (TB,N,V_cropColorInputToPrimaryCaptureRect) cropColorInputToPrimaryCaptureRect;
@property (TB,N,V_useLowFrameRateOptimizedNetwork) useLowFrameRateOptimizedNetwork;
@property (T@"NSString",&,N,V_alternativeStreamingPersonSegmentationMaskKey) alternativeStreamingPersonSegmentationMaskKey;
@property (T@"NSString",&,N,V_alternativeStreamingSkinSegmentationMaskKey) alternativeStreamingSkinSegmentationMaskKey;
```

## Instance methods

```
-[BWStreamingPersonSegmentationConfiguration useLowFrameRateOptimizedNetwork];
-[BWStreamingPersonSegmentationConfiguration alternativeStreamingPersonSegmentationMaskKey];
-[BWStreamingPersonSegmentationConfiguration alternativeStreamingSkinSegmentationMaskKey];
-[BWStreamingPersonSegmentationConfiguration dealloc];
-[BWStreamingPersonSegmentationConfiguration setUseLowFrameRateOptimizedNetwork:];
-[BWStreamingPersonSegmentationConfiguration setPropagateColorInput:];
-[BWStreamingPersonSegmentationConfiguration description];
-[BWStreamingPersonSegmentationConfiguration propagateColorInput];
-[BWStreamingPersonSegmentationConfiguration cropColorInputToPrimaryCaptureRect];
-[BWStreamingPersonSegmentationConfiguration setInputRotationAngle:];
-[BWStreamingPersonSegmentationConfiguration setAlternativeStreamingPersonSegmentationMaskKey:];
-[BWStreamingPersonSegmentationConfiguration setCropColorInputToPrimaryCaptureRect:];
-[BWStreamingPersonSegmentationConfiguration setAlternativeStreamingSkinSegmentationMaskKey:];
-[BWStreamingPersonSegmentationConfiguration inputRotationAngle];
```
