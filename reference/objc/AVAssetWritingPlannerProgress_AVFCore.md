# `AVAssetWritingPlannerProgress`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _trackProgress;
@"NSMutableDictionary" _trackTotalDuration;
@"NSMutableSet" _apacTrackIDs;
@"NSMutableSet" _loudnessCompletedTrackIDs;
^{OpaqueFigSimpleMutex=} _progressMutex;
```

## Properties

```
@property (Tf,R) overallProgress;
```

## Instance methods

```
-[AVAssetWritingPlannerProgress init];
-[AVAssetWritingPlannerProgress dealloc];
-[AVAssetWritingPlannerProgress overallProgress];
-[AVAssetWritingPlannerProgress progressForTrack:];
-[AVAssetWritingPlannerProgress setCompletedDuration:totalDuration:forTrack:];
-[AVAssetWritingPlannerProgress updateCompletedDuration:forTrack:];
```
