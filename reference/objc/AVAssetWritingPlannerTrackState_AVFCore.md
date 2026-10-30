# `AVAssetWritingPlannerTrackState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 24 instance methods, 2 class methods

## Instance variables

```
i _assemblyTrackID;
@"NSString" _mediaType;
@"NSString" _videoCodecType;
@"NSString" _audioCodecType;
B _requiresCompression;
@"NSArray" _segmentStates;
@"NSData" _lastCompletedSegmentFinalClientState;
@"NSDictionary" _lastCompletedSegmentFinalCompressionSessionState;
B _loudnessMeasurementCompleted;
@"NSData" _measuredLoudnessMagicCookie;
```

## Properties

```
@property (Ti,V_assemblyTrackID) assemblyTrackID;
@property (T@"NSString",C,V_mediaType) mediaType;
@property (TB,V_requiresCompression) requiresCompression;
@property (T@"NSString",C,V_videoCodecType) videoCodecType;
@property (T@"NSString",C,V_audioCodecType) audioCodecType;
@property (T@"NSArray",C,V_segmentStates) segmentStates;
@property (T@"NSData",C,V_lastCompletedSegmentFinalClientState) lastCompletedSegmentFinalClientState;
@property (T@"NSDictionary",C,V_lastCompletedSegmentFinalCompressionSessionState) lastCompletedSegmentFinalCompressionSessionState;
@property (TB,V_loudnessMeasurementCompleted) loudnessMeasurementCompleted;
@property (T@"NSData",C,V_measuredLoudnessMagicCookie) measuredLoudnessMagicCookie;
```

## Class methods

```
+[AVAssetWritingPlannerTrackState emptyState];
+[AVAssetWritingPlannerTrackState fromDictionary:error:];
```

## Instance methods

```
-[AVAssetWritingPlannerTrackState toDictionary];
-[AVAssetWritingPlannerTrackState dealloc];
-[AVAssetWritingPlannerTrackState setMediaType:];
-[AVAssetWritingPlannerTrackState description];
-[AVAssetWritingPlannerTrackState mediaType];
-[AVAssetWritingPlannerTrackState assemblyTrackID];
-[AVAssetWritingPlannerTrackState setMeasuredLoudnessMagicCookie:];
-[AVAssetWritingPlannerTrackState audioCodecType];
-[AVAssetWritingPlannerTrackState lastCompletedSegmentFinalClientState];
-[AVAssetWritingPlannerTrackState lastCompletedSegmentFinalCompressionSessionState];
-[AVAssetWritingPlannerTrackState loudnessMeasurementCompleted];
-[AVAssetWritingPlannerTrackState measuredLoudnessMagicCookie];
-[AVAssetWritingPlannerTrackState requiresCompression];
-[AVAssetWritingPlannerTrackState resumableBy:];
-[AVAssetWritingPlannerTrackState segmentStates];
-[AVAssetWritingPlannerTrackState setAssemblyTrackID:];
-[AVAssetWritingPlannerTrackState setAudioCodecType:];
-[AVAssetWritingPlannerTrackState setLastCompletedSegmentFinalClientState:];
-[AVAssetWritingPlannerTrackState setLastCompletedSegmentFinalCompressionSessionState:];
-[AVAssetWritingPlannerTrackState setLoudnessMeasurementCompleted:];
-[AVAssetWritingPlannerTrackState setRequiresCompression:];
-[AVAssetWritingPlannerTrackState setSegmentStates:];
-[AVAssetWritingPlannerTrackState setVideoCodecType:];
-[AVAssetWritingPlannerTrackState videoCodecType];
```
