# `BWSISNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 24 instance variables, 0 properties, 19 instance methods, 1 class methods

## Instance variables

```
^? _createSampleBufferProcessorFunction;
^{OpaqueFigSampleBufferProcessor=} _sampleBufferProcessor;
@"NSDictionary" _cameraTuningDictionary;
@"NSDictionary" _sensorIDDictionary;
@"NSDictionary" _noiseModelParamsDictionary;
@"NSDictionary" _fusionParamsDictionary;
i _fusionScheme;
B _alwaysRequestsPreBracketedEV0;
B _allowExperimentalOverrides;
i _lensShadingCorrectionMode;
i _maxIntegrationTimeLimitMsec;
f _bracketGainCap;
@"NSArray" _exposureValues;
@"NSArray" _afWindowParamsArray;
i _sisBracketCount;
@"NSArray" _oisExposureDurationTypes;
i _oisBracketCount;
@"FigCaptureStillImageSettings" _currentCaptureSettings;
B _preBracketedFrameReceived;
i _numberFramesReceived;
i _lastFusionTypeUsed;
B _livePhotoSupported;
B _OISSupported;
B _allowAllocationsAtPrepareTime;
```

## Class methods

```
+[BWSISNode initialize];
```

## Instance methods

```
-[BWSISNode prepareForCurrentConfigurationToBecomeLive];
-[BWSISNode renderSampleBuffer:forInput:];
-[BWSISNode dealloc];
-[BWSISNode nodeSubType];
-[BWSISNode didSelectFormat:forInput:];
-[BWSISNode handleNodeError:forInput:];
-[BWSISNode nodeType];
-[BWSISNode OISSupported];
-[BWSISNode initWithCameraTuningDictionary:sensorIDDictionary:fusionScheme:];
-[BWSISNode _initWithCameraTuningDictionary:sensorIDDictionary:sbpCreationFunction:fusionScheme:allowExperimentalOverrides:];
-[BWSISNode allowAllocationsAtPrepareTime];
-[BWSISNode alwaysRequestsPreBracketedEV0];
-[BWSISNode attachesInputBracketToOutputSampleBuffer];
-[BWSISNode livePhotoSupported];
-[BWSISNode setAllowAllocationsAtPrepareTime:];
-[BWSISNode setAlwaysRequestsPreBracketedEV0:];
-[BWSISNode setAttachesInputBracketToOutputSampleBuffer:];
-[BWSISNode setLivePhotoSupported:];
-[BWSISNode setOISSupported:];
```
