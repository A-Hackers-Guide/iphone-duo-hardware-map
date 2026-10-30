# `BWVariableFrameRateSelector`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 38 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
f _suggestedFrameRate;
i _mode;
f _integrationTimeFrom60To30;
f _integrationTimeFrom30To24;
f _integrationTimeFrom30BackTo60;
@"NSMutableDictionary" _vfrAEMaxGainsByPortType;
@"NSMutableDictionary" _variableFrameRateInfo;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _variableFrameRateInfoLock;
i _frameRateConversionStatus;
B _lastStabilityFlag;
B _deviceMotionEnabled;
B _sceneMotionEnabled;
B _zoomInProgress;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _sceneMotionAEInLowLight;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _sceneMotionAEInHighLight;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _deviceMotionInLowLight;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _deviceMotionInHighLight;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _aeLimits;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _zoomRequest;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _flickerDetected;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _waterSceneDetected;
f _previousEITForAELimitsReached;
i _globalMotionAE;
@"NSMutableDictionary" _highLightSceneMotionThresholdsByPortType;
@"NSMutableDictionary" _lowLightSceneMotionThresholdsByPortType;
{?="w"d"x"d"y"d"z"d} _lastQuaternion;
{?="w"d"x"d"y"d"z"d} _lastQuaternionDiff;
B _testRun;
B _frameRateConversionInVISNodeEnabled;
B _teleAutoVideoFrameRateAllows24FPS;
B _lowLightVideoNoiseReductionEnabled;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _lowLightVideoNoiseReductionLuxScene;
@"NSMutableDictionary" _lowLightVideoNoiseReductionLuxThresholdsByPortType;
@"NSString" _lastPortType;
i _lastQuadraBinningFactor;
@"BWInferenceResult" _mostRecentInferenceResult;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _smartCameraLock;
{?="reason"i"mode"i"fromFR"f"toFR"f"time"{?="value"q"timescale"i"flags"I"epoch"q}"isSceneStable"B"aeLimitsReached"B"waterSceneDetected"B"currentFrameRate"i} _state;
```

## Properties

```
@property (Tf,R,N) suggestedFrameRate;
```

## Class methods

```
+[BWVariableFrameRateSelector initialize];
```

## Instance methods

```
-[BWVariableFrameRateSelector dealloc];
-[BWVariableFrameRateSelector addAttachmentsToSamplebuffer:];
-[BWVariableFrameRateSelector getAEMaxGainForPortType:suggestedFrameRate:];
-[BWVariableFrameRateSelector initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:teleAutoVideoFrameRateAllows24FPS:lowLightVideoNoiseReductionEnabled:];
-[BWVariableFrameRateSelector processSampleBuffer:frameStatistics:currentFrameRate:aeMaxGain:zoomInProgress:mostRecentInferenceResult:];
-[BWVariableFrameRateSelector suggestedFrameRate];
```
