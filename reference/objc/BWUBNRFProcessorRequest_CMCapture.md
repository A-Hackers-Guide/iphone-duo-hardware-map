# `BWUBNRFProcessorRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 15 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"BWUBNRFProcessorInput" _input;
@"NRFUBFusionOutput" _output;
@"NRFDeepFusionOutput" _deepFusionOutput;
B _processErrorRecoveryFrame;
B _processOriginalImage;
i _clientBracketSequenceNumber;
B _processSemanticRendering;
B _provideInferenceInputImageForProcessing;
B _inferencesAvailable;
@"<BWUBNRFProcessorControllerDelegate>" _delegate;
i _err;
i _demosaicedRawErr;
i _numberOfFramesAddedForMultiFrameProcessing;
f _totalExposureTimesOfFramesAddedForMultiFrameProcessing;
f _minExposureTimesOfFramesAddedForMultiFrameProcessing;
f _maxExposureTimesOfFramesAddedForMultiFrameProcessing;
B _deliveredDeferredProxyImage;
B _deliveredAdaptiveBracketingErrorRecoveryFrame;
B _gainMapEnabled;
```

## Properties

```
@property (T@"BWUBNRFProcessorInput",R,N,V_input) input;
@property (T@"NRFUBFusionOutput",R,N,V_output) output;
@property (T@"NRFDeepFusionOutput",R,N,V_deepFusionOutput) deepFusionOutput;
@property (TB,R,N) processSemanticRendering;
@property (TB,R,N) provideInferenceInputImageForProcessing;
@property (TB,R,N) inferencesAvailable;
@property (Ti,N,V_err) err;
@property (Ti,N,V_demosaicedRawErr) demosaicedRawErr;
@property (Ti,N,V_numberOfFramesAddedForMultiFrameProcessing) numberOfFramesAddedForMultiFrameProcessing;
@property (Tf,N,V_totalExposureTimesOfFramesAddedForMultiFrameProcessing) totalExposureTimesOfFramesAddedForMultiFrameProcessing;
@property (Tf,N,V_minExposureTimesOfFramesAddedForMultiFrameProcessing) minExposureTimesOfFramesAddedForMultiFrameProcessing;
@property (Tf,N,V_maxExposureTimesOfFramesAddedForMultiFrameProcessing) maxExposureTimesOfFramesAddedForMultiFrameProcessing;
@property (TB,N,V_deliveredDeferredProxyImage) deliveredDeferredProxyImage;
@property (TB,N,V_deliveredAdaptiveBracketingErrorRecoveryFrame) deliveredAdaptiveBracketingErrorRecoveryFrame;
@property (TB,N,V_gainMapEnabled) gainMapEnabled;
```

## Instance methods

```
-[BWUBNRFProcessorRequest gainMapEnabled];
-[BWUBNRFProcessorRequest input];
-[BWUBNRFProcessorRequest setErr:];
-[BWUBNRFProcessorRequest setDeliveredDeferredProxyImage:];
-[BWUBNRFProcessorRequest processSemanticRendering];
-[BWUBNRFProcessorRequest deliveredAdaptiveBracketingErrorRecoveryFrame];
-[BWUBNRFProcessorRequest setMaxExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWUBNRFProcessorRequest dealloc];
-[BWUBNRFProcessorRequest provideInferenceInputImageForProcessing];
-[BWUBNRFProcessorRequest setDemosaicedRawErr:];
-[BWUBNRFProcessorRequest demosaicedRawErr];
-[BWUBNRFProcessorRequest deepFusionOutput];
-[BWUBNRFProcessorRequest setTotalExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWUBNRFProcessorRequest setNumberOfFramesAddedForMultiFrameProcessing:];
-[BWUBNRFProcessorRequest deliveredDeferredProxyImage];
-[BWUBNRFProcessorRequest err];
-[BWUBNRFProcessorRequest description];
-[BWUBNRFProcessorRequest inferencesAvailable];
-[BWUBNRFProcessorRequest setGainMapEnabled:];
-[BWUBNRFProcessorRequest setMinExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWUBNRFProcessorRequest minExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWUBNRFProcessorRequest output];
-[BWUBNRFProcessorRequest setDeliveredAdaptiveBracketingErrorRecoveryFrame:];
-[BWUBNRFProcessorRequest totalExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWUBNRFProcessorRequest maxExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWUBNRFProcessorRequest numberOfFramesAddedForMultiFrameProcessing];
```
