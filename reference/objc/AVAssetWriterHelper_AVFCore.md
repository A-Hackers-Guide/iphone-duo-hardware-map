# `AVAssetWriterHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 32 properties, 73 instance methods, 0 class methods

## Instance variables

```
@"AVAssetWriterConfigurationState" _configurationState;
@"AVWeakReference" _weakReferenceToAssetWriter;
```

## Properties

```
@property (TB,R,N,G_isDefunct) defunct;
@property (T@"AVAssetWriterConfigurationState",R,N,V_configurationState) configurationState;
@property (T@"AVWeakReference",&,V_weakReferenceToAssetWriter) weakReferenceToAssetWriter;
@property (T@"NSURL",R,N) outputURL;
@property (T@"AVMediaFileType",R,N) mediaFileType;
@property (T@"NSArray",R,N) availableMediaTypes;
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (T@"<AVAssetWriterDelegate>",W) delegate;
@property (T{?=qiIq},N) movieFragmentInterval;
@property (T{?=qiIq},N) initialMovieFragmentInterval;
@property (T{?=qiIq},N) overallDurationHint;
@property (TB,N) shouldOptimizeForNetworkUse;
@property (T@"NSURL",C,N) directoryForTemporaryFiles;
@property (Ti,N) movieTimeScale;
@property (T@"NSArray",C,N) metadata;
@property (T{CGAffineTransform=dddddd},N) preferredTransform;
@property (Tf,N) preferredVolume;
@property (Tf,N) preferredRate;
@property (Tq,N) singlePassFileSize;
@property (Tq,N) singlePassMediaDataSize;
@property (T@"NSArray",R,N) inputs;
@property (T@"NSArray",R,N) inputGroups;
@property (T{?=qiIq},N) preferredOutputSegmentInterval;
@property (T{?=qiIq},N) initialSegmentStartTime;
@property (T@"NSString",C,N) outputFileTypeProfile;
@property (Tq,N) initialMovieFragmentSequenceNumber;
@property (TB,N) producesCombinableFragments;
@property (TB,R,N,GisOutputFileOnExternalStorageDevice) outputFileIsOnExternalStorageDevice;
@property (TB,R,N,GisProVideoStorageSupported) proVideoStorageSupported;
@property (TB,N) usesProVideoStorage;
@property (TB,N) requiresInProcessOperation;
```

## Instance methods

```
-[AVAssetWriterHelper startWriting];
-[AVAssetWriterHelper setMovieFragmentInterval:];
-[AVAssetWriterHelper movieFragmentInterval];
-[AVAssetWriterHelper setPreferredVolume:];
-[AVAssetWriterHelper init];
-[AVAssetWriterHelper preferredTransform];
-[AVAssetWriterHelper overallDurationHint];
-[AVAssetWriterHelper inputs];
-[AVAssetWriterHelper flush];
-[AVAssetWriterHelper _isDefunct];
-[AVAssetWriterHelper preferredRate];
-[AVAssetWriterHelper dealloc];
-[AVAssetWriterHelper status];
-[AVAssetWriterHelper setPreferredTransform:];
-[AVAssetWriterHelper error];
-[AVAssetWriterHelper metadata];
-[AVAssetWriterHelper preferredVolume];
-[AVAssetWriterHelper setDelegate:];
-[AVAssetWriterHelper setMetadata:];
-[AVAssetWriterHelper delegate];
-[AVAssetWriterHelper outputURL];
-[AVAssetWriterHelper configurationState];
-[AVAssetWriterHelper finishWriting];
-[AVAssetWriterHelper addInput:];
-[AVAssetWriterHelper cancelWriting];
-[AVAssetWriterHelper finishWritingWithCompletionHandler:];
-[AVAssetWriterHelper startSessionAtSourceTime:];
-[AVAssetWriterHelper canAddInput:];
-[AVAssetWriterHelper setProducesCombinableFragments:];
-[AVAssetWriterHelper setShouldOptimizeForNetworkUse:];
-[AVAssetWriterHelper _canApplyOutputSettings:forMediaType:sourceFormat:exceptionReason:];
-[AVAssetWriterHelper _canApplyTrackReferences:exceptionReason:];
-[AVAssetWriterHelper _transitionToClientInitiatedTerminalStatus:];
-[AVAssetWriterHelper addInputGroup:];
-[AVAssetWriterHelper availableMediaTypes];
-[AVAssetWriterHelper canAddInputGroup:];
-[AVAssetWriterHelper canApplyOutputSettings:forMediaType:];
-[AVAssetWriterHelper directoryForTemporaryFiles];
-[AVAssetWriterHelper endSessionAtSourceTime:];
-[AVAssetWriterHelper flushSegment];
-[AVAssetWriterHelper initWithConfigurationState:];
-[AVAssetWriterHelper initialMovieFragmentInterval];
-[AVAssetWriterHelper initialMovieFragmentSequenceNumber];
-[AVAssetWriterHelper initialSegmentStartTime];
-[AVAssetWriterHelper inputGroups];
-[AVAssetWriterHelper isOutputFileOnExternalStorageDevice];
-[AVAssetWriterHelper isProVideoStorageSupported];
-[AVAssetWriterHelper mediaFileType];
-[AVAssetWriterHelper movieTimeScale];
-[AVAssetWriterHelper outputFileTypeProfile];
-[AVAssetWriterHelper preferredOutputSegmentInterval];
-[AVAssetWriterHelper producesCombinableFragments];
-[AVAssetWriterHelper requiresInProcessOperation];
-[AVAssetWriterHelper setDirectoryForTemporaryFiles:];
-[AVAssetWriterHelper setInitialMovieFragmentInterval:];
-[AVAssetWriterHelper setInitialMovieFragmentSequenceNumber:];
-[AVAssetWriterHelper setInitialSegmentStartTime:];
-[AVAssetWriterHelper setMovieTimeScale:];
-[AVAssetWriterHelper setOutputFileTypeProfile:];
-[AVAssetWriterHelper setOverallDurationHint:];
-[AVAssetWriterHelper setPreferredOutputSegmentInterval:];
-[AVAssetWriterHelper setPreferredRate:];
-[AVAssetWriterHelper setRequiresInProcessOperation:];
-[AVAssetWriterHelper setSinglePassFileSize:];
-[AVAssetWriterHelper setSinglePassMediaDataSize:];
-[AVAssetWriterHelper setUsesProVideoStorage:];
-[AVAssetWriterHelper setWeakReferenceToAssetWriter:];
-[AVAssetWriterHelper shouldOptimizeForNetworkUse];
-[AVAssetWriterHelper singlePassFileSize];
-[AVAssetWriterHelper singlePassMediaDataSize];
-[AVAssetWriterHelper transitionToFailedStatusWithError:];
-[AVAssetWriterHelper usesProVideoStorage];
-[AVAssetWriterHelper weakReferenceToAssetWriter];
```
