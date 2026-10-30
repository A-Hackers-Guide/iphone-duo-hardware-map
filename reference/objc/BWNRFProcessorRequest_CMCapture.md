# `BWNRFProcessorRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 17 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"BWNRFProcessorControllerConfiguration" _configuration;
@"BWNRFProcessorInput" _input;
@"NRFUBFusionOutput" _output;
@"NRFRawNightModeOutputFrame" _rawNightModeOutputFrame;
@"NRFDeepFusionOutput" _deepFusionOutput;
B _processErrorRecoveryFrame;
B _processErrorRecoveryProxy;
B _processHDRErrorRecovery;
B _processOriginalImage;
B _processLinearImage;
B _processToneMapping;
B _processInferenceInputImage;
i _clientBracketSequenceNumber;
B _processSemanticRendering;
B _provideInferenceInputImageForProcessing;
B _inferencesAvailable;
@"<BWNRFProcessorControllerDelegate>" _delegate;
B _processSmartStyleRenderingInput;
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
@property (T@"BWNRFProcessorInput",R,N,V_input) input;
@property (T@"NRFUBFusionOutput",R,N,V_output) output;
@property (T@"NRFRawNightModeOutputFrame",R,N,V_rawNightModeOutputFrame) rawNightModeOutputFrame;
@property (T@"NRFDeepFusionOutput",R,N,V_deepFusionOutput) deepFusionOutput;
@property (TB,R,N) processSemanticRendering;
@property (TB,R,N) provideInferenceInputImageForProcessing;
@property (TB,R,N) inferencesAvailable;
@property (TB,R,N,V_processSmartStyleRenderingInput) processSmartStyleRenderingInput;
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
-[BWNRFProcessorRequest gainMapEnabled];
-[BWNRFProcessorRequest input];
-[BWNRFProcessorRequest setErr:];
-[BWNRFProcessorRequest setDeliveredDeferredProxyImage:];
-[BWNRFProcessorRequest processSemanticRendering];
-[BWNRFProcessorRequest deliveredAdaptiveBracketingErrorRecoveryFrame];
-[BWNRFProcessorRequest setMaxExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWNRFProcessorRequest dealloc];
-[BWNRFProcessorRequest provideInferenceInputImageForProcessing];
-[BWNRFProcessorRequest setDemosaicedRawErr:];
-[BWNRFProcessorRequest demosaicedRawErr];
-[BWNRFProcessorRequest deepFusionOutput];
-[BWNRFProcessorRequest setTotalExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWNRFProcessorRequest setNumberOfFramesAddedForMultiFrameProcessing:];
-[BWNRFProcessorRequest deliveredDeferredProxyImage];
-[BWNRFProcessorRequest err];
-[BWNRFProcessorRequest description];
-[BWNRFProcessorRequest inferencesAvailable];
-[BWNRFProcessorRequest setGainMapEnabled:];
-[BWNRFProcessorRequest setMinExposureTimesOfFramesAddedForMultiFrameProcessing:];
-[BWNRFProcessorRequest rawNightModeOutputFrame];
-[BWNRFProcessorRequest minExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWNRFProcessorRequest output];
-[BWNRFProcessorRequest setDeliveredAdaptiveBracketingErrorRecoveryFrame:];
-[BWNRFProcessorRequest totalExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWNRFProcessorRequest processSmartStyleRenderingInput];
-[BWNRFProcessorRequest maxExposureTimesOfFramesAddedForMultiFrameProcessing];
-[BWNRFProcessorRequest numberOfFramesAddedForMultiFrameProcessing];
```
