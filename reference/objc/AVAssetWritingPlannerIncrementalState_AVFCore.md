# `AVAssetWritingPlannerIncrementalState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _trackStates;
@"NSString" _softwareBuild;
B _allSegmentsCompleted;
```

## Properties

```
@property (T@"NSArray",C,V_trackStates) trackStates;
@property (T@"NSString",C,V_softwareBuild) softwareBuild;
@property (TB,V_allSegmentsCompleted) allSegmentsCompleted;
```

## Class methods

```
+[AVAssetWritingPlannerIncrementalState emptyState];
+[AVAssetWritingPlannerIncrementalState fromDictionary:error:];
```

## Instance methods

```
-[AVAssetWritingPlannerIncrementalState toDictionary];
-[AVAssetWritingPlannerIncrementalState dealloc];
-[AVAssetWritingPlannerIncrementalState description];
-[AVAssetWritingPlannerIncrementalState setTrackStates:];
-[AVAssetWritingPlannerIncrementalState allSegmentsCompleted];
-[AVAssetWritingPlannerIncrementalState resumableBy:];
-[AVAssetWritingPlannerIncrementalState setAllSegmentsCompleted:];
-[AVAssetWritingPlannerIncrementalState setSoftwareBuild:];
-[AVAssetWritingPlannerIncrementalState softwareBuild];
-[AVAssetWritingPlannerIncrementalState trackIncrementalStateForTrack:];
-[AVAssetWritingPlannerIncrementalState trackStates];
```
