# `BWUBProcessorRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"BWUBProcessorInput" _input;
@"UBFusionOutput" _output;
@"UBDeepFusionOutput" _deepFusionOutput;
B _processErrorRecoveryFrame;
B _processOriginalImage;
B _processSemanticRendering;
B _provideInferenceInputImageForProcessing;
B _inferencesAvailable;
@"<BWUBProcessorControllerDelegate>" _delegate;
i _err;
i _numberOfFramesAddedForMultiFrameProcessing;
f _totalExposureTimesOfFramesAddedForMultiFrameProcessing;
f _minExposureTimesOfFramesAddedForMultiFrameProcessing;
f _maxExposureTimesOfFramesAddedForMultiFrameProcessing;
B _deliveredDeferredProxyImage;
```

## Properties

```
@property (T@"BWUBProcessorInput",R,N) input;
@property (T@"UBFusionOutput",R,N) output;
@property (T@"UBDeepFusionOutput",R,N) deepFusionOutput;
@property (TB,R,N) provideInferenceInputImageForProcessing;
@property (TB,R,N) inferencesAvailable;
@property (Ti,N,V_err) err;
@property (Ti,N,V_numberOfFramesAddedForMultiFrameProcessing) numberOfFramesAddedForMultiFrameProcessing;
@property (Tf,N,V_totalExposureTimesOfFramesAddedForMultiFrameProcessing) totalExposureTimesOfFramesAddedForMultiFrameProcessing;
@property (Tf,N,V_minExposureTimesOfFramesAddedForMultiFrameProcessing) minExposureTimesOfFramesAddedForMultiFrameProcessing;
@property (Tf,N,V_maxExposureTimesOfFramesAddedForMultiFrameProcessing) maxExposureTimesOfFramesAddedForMultiFrameProcessing;
@property (TB,N,V_deliveredDeferredProxyImage) deliveredDeferredProxyImage;
```

## Instance methods

```
-[BWUBProcessorRequest input];
-[BWUBProcessorRequest setErr:];
-[BWUBProcessorRequest setDeliveredDeferredProxyImage:];
-[BWUBProcessorRequest setMaxExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWUBProcessorRequest dealloc];
-[BWUBProcessorRequest provideInferenceInputImageForProcessing];
-[BWUBProcessorRequest deepFusionOutput];
-[BWUBProcessorRequest setTotalExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWUBProcessorRequest setNumberOfFramesAddedForMultiFrameProcessing:];
-[BWUBProcessorRequest deliveredDeferredProxyImage];
-[BWUBProcessorRequest err];
-[BWUBProcessorRequest description];
-[BWUBProcessorRequest inferencesAvailable];
-[BWUBProcessorRequest setMinExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWUBProcessorRequest minExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWUBProcessorRequest output];
-[BWUBProcessorRequest totalExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWUBProcessorRequest maxExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWUBProcessorRequest numberOfFramesAddedForMultiFrameProcessing];
```
