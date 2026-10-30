# `AVAssetWriterWritingHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetWriterHelper`
- Protocols: `AVAssetWriterFigAssetWriterNotificationHandlerDelegate`
- 6 instance variables, 4 properties, 30 instance methods, 3 class methods

## Instance variables

```
^{OpaqueFigAssetWriter=} _figAssetWriter;
B _figAssetWriterIsRemote;
@"NSObject<OS_dispatch_queue>" _figAssetWriterAccessQueue;
B _startSessionCalled;
@"AVAssetWriterFigAssetWriterNotificationHandler" _notificationHandler;
^v _figAssetWriterCallbackContextToken;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:];
+[AVAssetWriterWritingHelper finishWritingDelegateOperationWithAssetWriter:andFigAssetWriter:andDelegate:];
+[AVAssetWriterWritingHelper prepareInputsOperationsWithInputs:];
```

## Instance methods

```
-[AVAssetWriterWritingHelper flush];
-[AVAssetWriterWritingHelper _isDefunct];
-[AVAssetWriterWritingHelper dealloc];
-[AVAssetWriterWritingHelper status];
-[AVAssetWriterWritingHelper finishWriting];
-[AVAssetWriterWritingHelper cancelWriting];
-[AVAssetWriterWritingHelper finishWritingWithCompletionHandler:];
-[AVAssetWriterWritingHelper startSessionAtSourceTime:];
-[AVAssetWriterWritingHelper checkConfigurationToOutputSegmentDataReturningDebugDescription:];
-[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithCustomFigAssetWriterFinishOperation:];
-[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithDiskFullErrorLastOperation:];
-[AVAssetWriterWritingHelper _retainedFigAssetWriter];
-[AVAssetWriterWritingHelper _transitionToFinishWritingHelperWithFinishWritingOperations:];
-[AVAssetWriterWritingHelper areAllInputsPreferredMediaChunkAlignmentEqualTo:];
-[AVAssetWriterWritingHelper areAudioAndVideoOutputSettingsPassthrough];
-[AVAssetWriterWritingHelper checkAVAssetWriterInputConfigurationToOutputSegmentDataForFragmentedMPEG4FileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:];
-[AVAssetWriterWritingHelper didReceiveFigAssetWriterNotificationWithSuccess:error:];
-[AVAssetWriterWritingHelper endSessionAtSourceTime:];
-[AVAssetWriterWritingHelper figTrackReferences];
-[AVAssetWriterWritingHelper flushSegment];
-[AVAssetWriterWritingHelper hasProRes4KHighFPSVideoOutputSetting];
-[AVAssetWriterWritingHelper hasProResVideoOutputSetting];
-[AVAssetWriterWritingHelper initWithConfigurationState:assetWriter:];
-[AVAssetWriterWritingHelper initWithConfigurationState:assetWriter:error:];
-[AVAssetWriterWritingHelper isConfiguredForFragmentedMPEG4];
-[AVAssetWriterWritingHelper prepareEncodedSampleBuffersForPaddedWrites];
-[AVAssetWriterWritingHelper setAllInputsFigPreferredChunkAlignmentTo:];
-[AVAssetWriterWritingHelper storageSpacePreallocationSize];
-[AVAssetWriterWritingHelper transitionToFailedStatusWithError:];
-[AVAssetWriterWritingHelper writerInputForTrackID:];
```
