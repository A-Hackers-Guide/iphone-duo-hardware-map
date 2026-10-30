# `AVPlannedSegmentWritingRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _segmentFileOutputURL;
i _assemblyTrackID;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
B _hasFinished;
@? _finishBlock;
@"NSData" _initialClientState;
f _progress;
```

## Properties

```
@property (T@"NSURL",R,V_segmentFileOutputURL) segmentFileOutputURL;
@property (T{?={?=qiIq}{?=qiIq}},R,V_timeRange) timeRange;
@property (Ti,R,V_assemblyTrackID) assemblyTrackID;
@property (T@"NSData",R,V_initialClientState) clientStateToRestore;
@property (Tf,R) progress;
```

## Class methods

```
+[AVPlannedSegmentWritingRequest requestWithSegmentFileOutputURL:assemblyTrackID:timeRange:clientState:progress:finishBlock:];
```

## Instance methods

```
-[AVPlannedSegmentWritingRequest timeRange];
-[AVPlannedSegmentWritingRequest finish];
-[AVPlannedSegmentWritingRequest finishWithError:];
-[AVPlannedSegmentWritingRequest dealloc];
-[AVPlannedSegmentWritingRequest progress];
-[AVPlannedSegmentWritingRequest description];
-[AVPlannedSegmentWritingRequest cancel];
-[AVPlannedSegmentWritingRequest assemblyTrackID];
-[AVPlannedSegmentWritingRequest clientStateToRestore];
-[AVPlannedSegmentWritingRequest finishCommonWithClientState:error:];
-[AVPlannedSegmentWritingRequest finishWithClientState:];
-[AVPlannedSegmentWritingRequest initWithSegmentFileOutputURL:assemblyTrackID:timeRange:clientState:progress:finishBlock:];
-[AVPlannedSegmentWritingRequest segmentFileOutputURL];
```
