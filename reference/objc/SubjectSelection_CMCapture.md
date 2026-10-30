# `SubjectSelection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _smartFramingSceneMonitorMode;
@"NSMutableDictionary" _subjectTracksByGroupID;
@"NSMutableDictionary" _gazeProbabilitiesByGroupID;
f _faceSignificanceDetectionThreshold;
f _petSignificanceDetectionThreshold;
B _petTrackingEnabled;
f _faceRectExpansionScaleFactor;
f _petBodyRectExpansionScaleFactor;
f _vipDetectionThreshold;
f _vipDetectionDurationTimeInSeconds;
f _vipDropOffThreshold;
f _vipDropOffDurationTimeInSeconds;
f _motionFilteringWeightDecayRatio;
f _lastNondisruptiveSwitchingFormatZoomFactor;
```

## Instance methods

```
-[SubjectSelection dealloc];
-[SubjectSelection reset];
-[SubjectSelection updateStatesUsingDetectedObjects:currentPTS:trackedSubjectsByGroupIDOut:pixelBufferSize:nondisruptiveSwitchingFormatZoomFactor:];
-[SubjectSelection _createDetectionsByGroupIDFromDetections:expansionFactor:largestSizeOut:totalDetectionsCountOut:];
-[SubjectSelection _setSubjectSelectionCamGazeProbabilitiesByFaceGroupID:];
-[SubjectSelection initWithSmartFramingSceneMonitorMode:];
-[SubjectSelection setSubjectSelectionCamGazeProbabilitiesByFaceGroupID:];
```
