# `BWScalerProcessorControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 6 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _frame;
Q _bufferType;
B _processingModeSet;
i _processingMode;
i _resolvedProcessingResolutionFlavor;
{?="width"i"height"i} _inputCropDimensions;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_frame) frame;
@property (TQ,R,N,V_bufferType) bufferType;
@property (Ti,N) processingMode;
@property (Ti,N,V_resolvedProcessingResolutionFlavor) resolvedProcessingResolutionFlavor;
@property (T{?=ii},N,V_inputCropDimensions) inputCropDimensions;
```

## Instance methods

```
-[BWScalerProcessorControllerInput processingMode];
-[BWScalerProcessorControllerInput dealloc];
-[BWScalerProcessorControllerInput resolvedProcessingResolutionFlavor];
-[BWScalerProcessorControllerInput description];
-[BWScalerProcessorControllerInput initWithSettings:portType:];
-[BWScalerProcessorControllerInput setResolvedProcessingResolutionFlavor:];
-[BWScalerProcessorControllerInput frame];
-[BWScalerProcessorControllerInput addFrame:bufferType:];
-[BWScalerProcessorControllerInput bufferType];
-[BWScalerProcessorControllerInput inputCropDimensions];
-[BWScalerProcessorControllerInput setInputCropDimensions:];
-[BWScalerProcessorControllerInput setProcessingMode:];
```
