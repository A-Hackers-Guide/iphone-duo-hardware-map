# `AVSampleBufferDisplayLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `AVIntegrityChecking`, `AVQueuedSampleBufferRendering`, `AVContentKeyRecipientInternal`, `AVContentKeyRecipient`, `AVMediaDataRequesterConsumer`, `AVQueuedSampleBufferRenderingInternal`
- 11 instance variables, 38 properties, 63 instance methods, 5 class methods

## Instance variables

```
@"CALayer" _contentLayer;
@"NSString" _videoGravity;
{CGSize="width"d"height"d} _presentationSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"AVSampleBufferVideoRenderer" _sampleBufferVideoRenderer;
@"NSError" _initFailureError;
@"AVSampleBufferVideoOutput" _videoOutput;
@"<AVLoggingIdentifier>" _loggingIdentifier;
B _overridesPreferredDynamicRangeForVideo;
@"CALayer" _STSLayer;
```

## Properties

```
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (T@"NSUUID",?,R,N) uniqueIdentifier;
@property (TB,?,R,N) disallowsLoggingURLs;
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{OpaqueCMTimebase=},R,&) timebase;
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (TB,R,N) requiresFlushToResumeDecoding;
@property (TB,R,GisReadyForMoreMediaData) readyForMoreMediaData;
@property (TB,R,N) hasSufficientMediaDataForReliablePlaybackStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) outputObscuredDueToInsufficientExternalProtection;
@property (TB,N) preventsCapture;
@property (TB,N) preventsDisplaySleepDuringVideoPlayback;
@property (TB,N) preventsAutomaticBackgroundingDuringVideoPlayback;
@property (TB,G_disallowsVideoLayerDisplayCompositing,S_setDisallowsVideoLayerDisplayCompositing:) disallowsVideoLayerDisplayCompositing;
@property (T@"AVSampleBufferVideoOutput",N) output;
@property (T@"AVSampleBufferVideoRenderer",R,N) sampleBufferRenderer;
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"AVSampleBufferVideoRenderer",R,N,G_sampleBufferVideoRenderer,V_sampleBufferVideoRenderer) sampleBufferVideoRenderer;
@property (T^{OpaqueCMTimebase=},&) controlTimebase;
@property (T@"NSString",C) videoGravity;
@property (TB,R,N,GisReadyForDisplay) readyForDisplay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVSampleBufferDisplayLayer keyPathsForValuesAffectingError];
+[AVSampleBufferDisplayLayer _destRectForAspectRatio:];
+[AVSampleBufferDisplayLayer _getContentLayerClass];
+[AVSampleBufferDisplayLayer keyPathsForValuesAffectingOutputObscuredDueToInsufficientExternalProtection];
+[AVSampleBufferDisplayLayer keyPathsForValuesAffectingStatus];
```

## Instance methods

```
-[AVSampleBufferDisplayLayer timebase];
-[AVSampleBufferDisplayLayer setToneMapToStandardDynamicRange:];
-[AVSampleBufferDisplayLayer _disallowsVideoLayerDisplayCompositing];
-[AVSampleBufferDisplayLayer setControlTimebase:];
-[AVSampleBufferDisplayLayer flushWithRemovalOfDisplayedImage:completionHandler:];
-[AVSampleBufferDisplayLayer outputObscuredDueToInsufficientExternalProtection];
-[AVSampleBufferDisplayLayer setPreferredDynamicRange:];
-[AVSampleBufferDisplayLayer isReadyForDisplay];
-[AVSampleBufferDisplayLayer resetUpcomingSampleBufferPresentationTimeExpectations];
-[AVSampleBufferDisplayLayer isReadyForMoreMediaData];
-[AVSampleBufferDisplayLayer videoPerformanceMetrics];
-[AVSampleBufferDisplayLayer stopRequestingMediaData];
-[AVSampleBufferDisplayLayer init];
-[AVSampleBufferDisplayLayer flush];
-[AVSampleBufferDisplayLayer setPreventsCapture:];
-[AVSampleBufferDisplayLayer hasSufficientMediaDataForReliablePlaybackStart];
-[AVSampleBufferDisplayLayer controlTimebase];
-[AVSampleBufferDisplayLayer setOutput:];
-[AVSampleBufferDisplayLayer dealloc];
-[AVSampleBufferDisplayLayer requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVSampleBufferDisplayLayer setPreventsAutomaticBackgroundingDuringVideoPlayback:];
-[AVSampleBufferDisplayLayer expectMonotonicallyIncreasingUpcomingSampleBufferPresentationTimes];
-[AVSampleBufferDisplayLayer enqueueSampleBuffer:];
-[AVSampleBufferDisplayLayer requiresFlushToResumeDecoding];
-[AVSampleBufferDisplayLayer status];
-[AVSampleBufferDisplayLayer _setDisallowsVideoLayerDisplayCompositing:];
-[AVSampleBufferDisplayLayer setBounds:];
-[AVSampleBufferDisplayLayer error];
-[AVSampleBufferDisplayLayer preventsDisplaySleepDuringVideoPlayback];
-[AVSampleBufferDisplayLayer isDefunct];
-[AVSampleBufferDisplayLayer expectMinimumUpcomingSampleBufferPresentationTime:];
-[AVSampleBufferDisplayLayer layerDidBecomeVisible:];
-[AVSampleBufferDisplayLayer setSTSLabel:];
-[AVSampleBufferDisplayLayer _nameForLogging];
-[AVSampleBufferDisplayLayer videoGravity];
-[AVSampleBufferDisplayLayer layoutSublayers];
-[AVSampleBufferDisplayLayer videoRect];
-[AVSampleBufferDisplayLayer prerollDecodeWithCompletionHandler:];
-[AVSampleBufferDisplayLayer expire];
-[AVSampleBufferDisplayLayer preventsCapture];
-[AVSampleBufferDisplayLayer setVideoGravity:];
-[AVSampleBufferDisplayLayer copyFigSampleBufferAudioRenderer:];
-[AVSampleBufferDisplayLayer setRenderSynchronizer:error:];
-[AVSampleBufferDisplayLayer output];
-[AVSampleBufferDisplayLayer contentKeySession];
-[AVSampleBufferDisplayLayer preventsAutomaticBackgroundingDuringVideoPlayback];
-[AVSampleBufferDisplayLayer setPreventsDisplaySleepDuringVideoPlayback:];
-[AVSampleBufferDisplayLayer _STSLabel];
-[AVSampleBufferDisplayLayer copyDisplayedPixelBuffer];
-[AVSampleBufferDisplayLayer flushAndRemoveImage];
-[AVSampleBufferDisplayLayer _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:];
-[AVSampleBufferDisplayLayer _attachedToExternalContentKeySession];
-[AVSampleBufferDisplayLayer _contentLayer];
-[AVSampleBufferDisplayLayer _preferredDynamicRangeForPiP];
-[AVSampleBufferDisplayLayer _sampleBufferVideoRenderer];
-[AVSampleBufferDisplayLayer _updateLayerTreeGeometryWithVideoGravity:presentationSize:videoGravityShouldTriggerAnimation:];
-[AVSampleBufferDisplayLayer _updatePresentationSize:];
-[AVSampleBufferDisplayLayer makeVideoRenderer];
-[AVSampleBufferDisplayLayer mayRequireContentKeysForMediaDataProcessing];
-[AVSampleBufferDisplayLayer overridesPreferredDynamicRangeForVideo];
-[AVSampleBufferDisplayLayer postVideoRectDidChangeNotification];
-[AVSampleBufferDisplayLayer sampleBufferRenderer];
-[AVSampleBufferDisplayLayer setOverridesPreferredDynamicRangeForVideo:];
```
