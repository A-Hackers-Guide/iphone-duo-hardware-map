# `TrackedSubject`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _groupID;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trackedRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _unscaledTrackedRect;
@"NSMutableArray" _gazeScores;
@"NSMutableArray" _trajectory;
@"NSMutableArray" _trajectoryTimeStamps;
{?="value"q"timescale"i"flags"I"epoch"q} _firstSignificantTimeStamp;
B _isPet;
B _isSignificant;
B _isPersistentlySignificant;
f _significanceDetectionThreshold;
I _smartFramingSceneMonitorMode;
f _distance;
f _motionInPreviewPixels;
f _motionFilteringWeightDecayRatio;
f _vipConfidence;
B _isVIPSignificant;
B _isSignificantForApertureControl;
{?="value"q"timescale"i"flags"I"epoch"q} _firstVIPSignificantTimeStamp;
{?="value"q"timescale"i"flags"I"epoch"q} _firstVIPDropOffTimeStamp;
f _vipDetectionThreshold;
f _vipDetectionDurationTimeInSeconds;
f _vipDropOffThreshold;
f _vipDropOffDurationTimeInSeconds;
B _isGazing;
```

## Properties

```
@property (TB,R,N,V_isPersistentlySignificant) isPersistentlySignificant;
@property (TB,R,N,V_isSignificant) isSignificant;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_trackedRect) trackedRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_unscaledTrackedRect) unscaledTrackedRect;
@property (Tf,R,N,V_distance) distance;
@property (Tf,R,N,V_motionInPreviewPixels) motionInPreviewPixels;
@property (TB,R,N,V_isVIPSignificant) isVIPSignificant;
@property (TB,R,N,V_isSignificantForApertureControl) isSignificantForApertureControl;
@property (TB,R,N,V_isGazing) isGazing;
```

## Instance methods

```
-[TrackedSubject distance];
-[TrackedSubject dealloc];
-[TrackedSubject isSignificant];
-[TrackedSubject isSignificantForApertureControl];
-[TrackedSubject _appendArray:withObject:restrictingLengthTo:];
-[TrackedSubject _updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:];
-[TrackedSubject initWithGroupID:significanceDetectionThreshold:smartFramingSceneMonitorMode:isPet:vipDetectionThreshold:vipDetectionDurationTimeInSeconds:vipDropOffThreshold:vipDropOffDurationTimeInSeconds:motionFilteringWeightDecayRatio:];
-[TrackedSubject isGazing];
-[TrackedSubject isPersistentlySignificant];
-[TrackedSubject isVIPSignificant];
-[TrackedSubject motionInPreviewPixels];
-[TrackedSubject resetTrajectoryHistory];
-[TrackedSubject trackedRect];
-[TrackedSubject unscaledTrackedRect];
-[TrackedSubject updateStatesUsingTrackedRect:trackedRectSize:gazeProbabilitiesData:largestFaceSize:totalDetectedFaceCount:currentPTS:distance:pixelBufferSize:vipConfidence:unscaledTrackedRect:];
```
