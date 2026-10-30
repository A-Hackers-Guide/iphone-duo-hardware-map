# `BWVideoNoiseReductionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 41 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _cameraInfoByPortType;
i _maxLossyCompressionLevel;
@"NSArray" _requiredAttachedMediaKeys;
@"NSDictionary" _videoNoiseReductionGainThresholdsByPortType;
{?="width"i"height"i} _visOutputDimensions;
f _maximumAllowedOverscan;
{?="width"i"height"i} _visInputValidDimensions;
{?="width"i"height"i} _videoNoiseReductionDimensions;
@"NSString" _lastPortType;
i _lastQuadraBinningFactor;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _sceneMonitor;
f _maximumAllowedFrameRate;
i _maximumAllowedFrameRateReachedCount;
i _maximumAllowedSystemPressureLevel;
B _maximumAllowedSystemPressureLevelReached;
i _clearHistoryThresholdFrameCount;
^{opaqueCMFormatDescription=} _outputFormatDescription;
B _videoNoiseReductionEnabled;
[2^{work_interval}] _workInterval;
@"<MTLCommandQueue>" _metalCommandQueue;
@"<MTLSharedEvent>" _metalSharedEvent;
@"MTLSharedEventListener" _metalSharedEventListener;
@"NSObject<OS_dispatch_semaphore>" _metalProcessingWaitSemaphore;
^{__CVMetalTextureCache=} _metalTextureCache;
@"LLVPreProcessorIBP" _llvPreProcessorIBP;
@"LLVProcessorIBP" _llvProcessorIBP;
@"LLVPostProcessorIBP" _llvPostProcessorIBP;
@"NSObject<OS_dispatch_queue>" _llvProcessingQueue;
B _llvProcessorsLoaded;
@"BWFigCaptureISPProcessingSession" _ispProcessingSession;
@"NSObject<OS_dispatch_semaphore>" _ispWait;
i _ispStatus;
@"BWPixelBufferPool" _llvProcessPixelBufferPool;
^{__CVBuffer=} _llvProcessInputPixelBuffer;
^{__CVBuffer=} _llvProcessOutputPixelBuffer;
^{__CVBuffer=} _lastHumanFullBodiesMask;
i _lastCaptureID;
f _lastApertureDiameter;
@"NSData" _lastLSCGainGridData;
@"BWRamp" _crossfadeRamp;
B _crossfadeInEnabled;
```

## Class methods

```
+[BWVideoNoiseReductionNode initialize];
```

## Instance methods

```
-[BWVideoNoiseReductionNode prepareForCurrentConfigurationToBecomeLive];
-[BWVideoNoiseReductionNode renderSampleBuffer:forInput:];
-[BWVideoNoiseReductionNode dealloc];
-[BWVideoNoiseReductionNode hasNonLiveConfigurationChanges];
-[BWVideoNoiseReductionNode didReachEndOfDataForConfigurationID:input:];
-[BWVideoNoiseReductionNode nodeSubType];
-[BWVideoNoiseReductionNode didSelectFormat:forInput:];
-[BWVideoNoiseReductionNode nodeType];
-[BWVideoNoiseReductionNode initWithCameraInfoByPortType:maxLossyCompressionLevel:ispProcessingSession:videoNoiseReductionGainThresholdsByPortType:visOutputDimensions:];
```
