# `BWMetadataDetectorGatingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFanOutNode`
- Protocols: `BWMRCSceneObserver`
- 18 instance variables, 10 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _mrcOutput;
@"BWNodeOutput" _appClipCodeOutput;
@"BWNodeOutput" _textLocalizationOutput;
@"BWMetadataDetectorGatingOutputController" _mrcOutputController;
@"BWMetadataDetectorGatingOutputController" _appClipCodeOutputController;
@"BWMetadataDetectorGatingOutputController" _textLocalizationOutputController;
@"NSMutableArray" _outputControllers;
B _lowPowerModeEnabled;
@"NSObject<OS_dispatch_group>" _detectorsAvailableGroup;
B _needsSynchronization;
^{OpaqueVTPixelTransferSession=} _transferSession;
@"BWPixelBufferPool" _outputBufferPool;
{?="width"i"height"i} _outputBufferPoolDimensions;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sceneLock;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _qrCodeScene;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _appClipCodeScene;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _textScene;
@"BWSceneStabilityMonitor" _sceneStabilityMonitor;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_mrcOutput) mrcOutput;
@property (T@"BWNodeOutput",R,N,V_appClipCodeOutput) appClipCodeOutput;
@property (T@"BWNodeOutput",R,N,V_textLocalizationOutput) textLocalizationOutput;
@property (T@"<BWMetadataDetectedResultsObserver>",R,N) mrcResultsObserver;
@property (T@"<BWMetadataDetectedResultsObserver>",R,N) appClipCodeResultsObserver;
@property (T@"<BWMetadataDetectedResultsObserver>",R,N) textLocalizationResultsObserver;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWMetadataDetectorGatingNode initialize];
```

## Instance methods

```
-[BWMetadataDetectorGatingNode prepareForCurrentConfigurationToBecomeLive];
-[BWMetadataDetectorGatingNode renderSampleBuffer:forInput:];
-[BWMetadataDetectorGatingNode mrcOutput];
-[BWMetadataDetectorGatingNode dealloc];
-[BWMetadataDetectorGatingNode initWithMRCEnabled:appClipCodeEnabled:textLocalizationEnabled:lowPowerModeEnabled:compressed8BitInputEnabled:];
-[BWMetadataDetectorGatingNode textLocalizationResultsObserver];
-[BWMetadataDetectorGatingNode appClipCodeResultsObserver];
-[BWMetadataDetectorGatingNode appClipCodeOutput];
-[BWMetadataDetectorGatingNode sceneDidChangeQRConfidence:appClipCodeConfidence:documentConfidence:textConfidence:];
-[BWMetadataDetectorGatingNode initWithSceneClassifierVersion:mrcEnabled:appClipCodeEnabled:textLocalizationEnabled:lowPowerModeEnabled:compressed8BitInputEnabled:];
-[BWMetadataDetectorGatingNode didReachEndOfDataForConfigurationID:input:];
-[BWMetadataDetectorGatingNode mrcResultsObserver];
-[BWMetadataDetectorGatingNode nodeSubType];
-[BWMetadataDetectorGatingNode textLocalizationOutput];
-[BWMetadataDetectorGatingNode didSelectFormat:forInput:];
-[BWMetadataDetectorGatingNode nodeType];
```
