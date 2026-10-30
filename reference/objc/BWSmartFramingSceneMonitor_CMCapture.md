# `BWSmartFramingSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
I _smartFramingSceneMonitorMode;
@"NSMutableArray" _optimalFOVHistory;
@"NSMutableArray" _optimalFOVHistoryPTS;
f _suggestedFOVSlackDurationInSeconds;
i _cumulativeSuggestedFOVType;
@"NSMutableDictionary" _subjectDistanceRangeInMM;
f _subjectMotionSpeedPixelsPerSecond;
@"NSDictionary" _fieldsOfView;
B _zoomInTransitionEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _lastFaceDetectionPTS;
f _noFaceDetectedZoomOutTimeInSeconds;
{?="value"q"timescale"i"flags"I"epoch"q} _lastSuggestedFieldOfViewChangePTS;
@"NSArray" _viewsInAscendingFOV;
@"NSDictionary" _minimumRequiredSignificantFaceCount;
@"NSDictionary" _detectedObjectsInfo;
{?="value"q"timescale"i"flags"I"epoch"q} _detectedObjectsInfoPTS;
@"SubjectSelection" _subjectSelection;
d _minVisibleSubjectRatioForShutterSoundRelaxation;
```

## Properties

```
@property (TI,R,N,V_smartFramingSceneMonitorMode) smartFramingSceneMonitorMode;
```

## Class methods

```
+[BWSmartFramingSceneMonitor initialize];
```

## Instance methods

```
-[BWSmartFramingSceneMonitor dealloc];
-[BWSmartFramingSceneMonitor reset];
-[BWSmartFramingSceneMonitor initWithSmartFramingSceneMonitorMode:];
-[BWSmartFramingSceneMonitor resolveMonitoringResultWithSampleBuffer:fromDynamicFieldOfViewRects:];
-[BWSmartFramingSceneMonitor setSmartFramingCamGazeProbabilitiesByFaceGroupID:];
-[BWSmartFramingSceneMonitor setSmartFramingFieldOfViewRects:];
-[BWSmartFramingSceneMonitor smartFramingSceneMonitorMode];
```
