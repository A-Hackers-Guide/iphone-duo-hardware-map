# `FigIrisAutoTrimmer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 2 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _motionAvailable;
{?="w"d"x"d"y"d"z"d} _captureMotionDelta;
d _captureMotionDeltaPeriod;
B _haveCaptureMotionDelta;
{?="w"d"x"d"y"d"z"d} _lastAttitude;
{?="w"d"x"d"y"d"z"d} _lastDelta;
d _lastCheckedTimestamp;
i _lastStatus;
i _svmKernelType;
i _svmVectorCount;
i _svmParamCount;
f _svmRBFRho;
f _svmRBFGamma;
@"NSArray" _svmKeys;
@"NSData" _svmNormalization;
@"NSData" _svmVectors;
@"NSMutableArray" _motionSamples;
Q _estimatedIntermediatesCount;
B _intermediateLoggingEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _maxHoldDuration;
q _maxHoldFrames;
d _bufferHistorySeconds;
d _motionSampleRate;
Q _nominalHistorySize;
B _vitalityScoringEnabled;
f _vitalityDocumentThreshold;
I _vitalityScoringVersion;
{?="major"S"minor"S"patch"S} _vitalityScoringSmartCameraPipelineVersion;
```

## Properties

```
@property (TB,R,N) trimmingActive;
@property (TI,R,N) vitalityScoringVersion;
```

## Class methods

```
+[FigIrisAutoTrimmer initialize];
```

## Instance methods

```
-[FigIrisAutoTrimmer stopMotionProcessing];
-[FigIrisAutoTrimmer setVitalityScoringSmartCameraPipelineVersion:];
-[FigIrisAutoTrimmer setBufferHistorySeconds:];
-[FigIrisAutoTrimmer exportMotionSamples];
-[FigIrisAutoTrimmer init];
-[FigIrisAutoTrimmer maxHoldDuration];
-[FigIrisAutoTrimmer dealloc];
-[FigIrisAutoTrimmer processCountOfVisibleVitalityObjects:forHostTime:];
-[FigIrisAutoTrimmer setIntermediateLoggingEnabled:];
-[FigIrisAutoTrimmer setMaxHoldDuration:];
-[FigIrisAutoTrimmer computeVitalityScoreForStillImageHostPTS:movieRange:];
-[FigIrisAutoTrimmer bufferHistorySeconds];
-[FigIrisAutoTrimmer emissionStatusForHostPTS:];
-[FigIrisAutoTrimmer beginTrimmingForStillImageHostPTS:minimumPTS:];
-[FigIrisAutoTrimmer vitalityScoringEnabled];
-[FigIrisAutoTrimmer videoFrameRate];
-[FigIrisAutoTrimmer intermediateLoggingEnabled];
-[FigIrisAutoTrimmer setVitalityScoringEnabled:];
-[FigIrisAutoTrimmer trimmingActive];
-[FigIrisAutoTrimmer startMotionProcessing];
-[FigIrisAutoTrimmer processInferences:forHostTime:];
-[FigIrisAutoTrimmer vitalityScoringSmartCameraPipelineVersion];
-[FigIrisAutoTrimmer processISPMotionData:forHostTime:];
-[FigIrisAutoTrimmer setVideoFrameRate:];
-[FigIrisAutoTrimmer vitalityScoringVersion];
```
