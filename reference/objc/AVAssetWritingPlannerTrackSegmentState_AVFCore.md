# `AVAssetWritingPlannerTrackSegmentState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"NSURL" _segmentURL;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
{?="value"q"timescale"i"flags"I"epoch"q} _overlapDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _flushDuration;
@"NSString" _mediaType;
B _requiresCompression;
q _frameCount;
B _hasCompleted;
```

## Properties

```
@property (T@"NSURL",C,V_segmentURL) segmentURL;
@property (T{?={?=qiIq}{?=qiIq}},V_timeRange) timeRange;
@property (T{?=qiIq},V_overlapDuration) overlapDuration;
@property (T{?=qiIq},V_flushDuration) flushDuration;
@property (T@"NSString",C,V_mediaType) mediaType;
@property (TB,V_requiresCompression) requiresCompression;
@property (Tq,V_frameCount) frameCount;
@property (TB,V_hasCompleted) hasCompleted;
```

## Class methods

```
+[AVAssetWritingPlannerTrackSegmentState emptyState];
+[AVAssetWritingPlannerTrackSegmentState fromDictionary:mediaType:error:];
```

## Instance methods

```
-[AVAssetWritingPlannerTrackSegmentState toDictionary];
-[AVAssetWritingPlannerTrackSegmentState setTimeRange:];
-[AVAssetWritingPlannerTrackSegmentState frameCount];
-[AVAssetWritingPlannerTrackSegmentState timeRange];
-[AVAssetWritingPlannerTrackSegmentState dealloc];
-[AVAssetWritingPlannerTrackSegmentState setMediaType:];
-[AVAssetWritingPlannerTrackSegmentState description];
-[AVAssetWritingPlannerTrackSegmentState setFrameCount:];
-[AVAssetWritingPlannerTrackSegmentState mediaType];
-[AVAssetWritingPlannerTrackSegmentState hasCompleted];
-[AVAssetWritingPlannerTrackSegmentState setHasCompleted:];
-[AVAssetWritingPlannerTrackSegmentState overlapDuration];
-[AVAssetWritingPlannerTrackSegmentState flushDuration];
-[AVAssetWritingPlannerTrackSegmentState requiresCompression];
-[AVAssetWritingPlannerTrackSegmentState resumableBy:];
-[AVAssetWritingPlannerTrackSegmentState segmentURL];
-[AVAssetWritingPlannerTrackSegmentState setFlushDuration:];
-[AVAssetWritingPlannerTrackSegmentState setOverlapDuration:];
-[AVAssetWritingPlannerTrackSegmentState setRequiresCompression:];
-[AVAssetWritingPlannerTrackSegmentState setSegmentURL:];
```
