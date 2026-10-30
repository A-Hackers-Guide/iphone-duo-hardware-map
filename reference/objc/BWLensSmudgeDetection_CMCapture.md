# `BWLensSmudgeDetection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
{BWLensSmudgeDetectionConfiguration="lensSmudgeDetectionEnabled"B"lensSmudgeDetectionInterval"{?="value"q"timescale"i"flags"I"epoch"q}} _configuration;
@"NSMutableDictionary" _detectionInfo;
@"NSMutableDictionary" _tuningParametersByPortType;
{?="status"i"observedConfidence"f"smudgeConfUpdated"B"prevSmudgeConf"f"smudgeConf"f"smudgeProbUpdated"B"smudgeProb"f} _cmcData;
{?="status"i"observedConfidence"f"smudgeConfUpdated"B"prevSmudgeConf"f"smudgeConf"f"smudgeProbUpdated"B"smudgeProb"f} _anstData;
{?="roll"d"pitch"d"yaw"d} _preAttitude;
f _attitudeDiff;
q _mode;
B _stopped;
{?="value"q"timescale"i"flags"I"epoch"q} _detectionCycleDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _lastDetectionStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _detectionEndTime;
B _didUpdateStatus;
@? _inferenceEngineToTearDownBlock;
@? _inferencesToSkipBlock;
```

## Properties

```
@property (T@?,C,N,V_inferenceEngineToTearDownBlock) inferenceEngineToTearDownBlock;
@property (T@?,C,N,V_inferencesToSkipBlock) inferencesToSkipBlock;
```

## Class methods

```
+[BWLensSmudgeDetection initialize];
```

## Instance methods

```
-[BWLensSmudgeDetection inferenceEngineToTearDownBlock];
-[BWLensSmudgeDetection dealloc];
-[BWLensSmudgeDetection setInferenceEngineToTearDownBlock:];
-[BWLensSmudgeDetection inferencesToSkipBlock];
-[BWLensSmudgeDetection setInferencesToSkipBlock:];
-[BWLensSmudgeDetection initWithConfiguration:activePortTypes:];
-[BWLensSmudgeDetection readISPMotionDataUsingMetadata:attitude:];
-[BWLensSmudgeDetection updateDetectionUsingSampleBuffer:detectionUpdatedBlock:];
```
