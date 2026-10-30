# `BWSceneClassifierSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- 13 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
{?="major"S"minor"S"patch"S} _version;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resultLock;
@"BWInferenceResult" _mostRecentSmartCameraResult;
@"NSObject<OS_dispatch_queue>" _observerQueue;
@"BWFigVideoCaptureDevice" _device;
@"FigWeakReference" _weakMRCSceneObserver;
@"FigWeakReference" _weakSemanticStyleSceneObserver;
i _semanticStyleSceneType;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _foodScene;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _indoorScene;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _outdoorScene;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _sunsetScene;
@"BWLensSmudgeDetection" _lensSmudgeDetection;
```

## Properties

```
@property (T@"<BWMRCSceneObserver>",N) mrcSceneObserver;
@property (T@"<BWSemanticStyleSceneObserver>",N) semanticStyleSceneObserver;
@property (T@?,C,N) inferenceEngineToTearDownBlock;
@property (T@?,C,N) inferencesToSkipBlock;
```

## Class methods

```
+[BWSceneClassifierSinkNode initialize];
```

## Instance methods

```
-[BWSceneClassifierSinkNode semanticStyleSceneObserver];
-[BWSceneClassifierSinkNode renderSampleBuffer:forInput:];
-[BWSceneClassifierSinkNode inferenceEngineToTearDownBlock];
-[BWSceneClassifierSinkNode dealloc];
-[BWSceneClassifierSinkNode setInferenceEngineToTearDownBlock:];
-[BWSceneClassifierSinkNode inferencesToSkipBlock];
-[BWSceneClassifierSinkNode setInferencesToSkipBlock:];
-[BWSceneClassifierSinkNode initWithCaptureDevice:version:lensSmudgeDetectionConfiguration:sinkID:];
-[BWSceneClassifierSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWSceneClassifierSinkNode setSemanticStyleSceneObserver:];
-[BWSceneClassifierSinkNode mrcSceneObserver];
-[BWSceneClassifierSinkNode nodeSubType];
-[BWSceneClassifierSinkNode setMrcSceneObserver:];
```
