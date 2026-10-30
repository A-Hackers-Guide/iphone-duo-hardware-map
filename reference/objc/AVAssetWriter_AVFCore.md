# `AVAssetWriter`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVIntegrityChecking`, `AVWeakObservable`, `AVKeyPathDependencyHost`
- 1 instance variables, 19 properties, 75 instance methods, 4 class methods

## Instance variables

```
@"AVAssetWriterInternal" _internal;
```

## Properties

```
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"AVAssetWriterHelper",R,&,G_helper) helper;
@property (T@"NSURL",R,C,N) outputURL;
@property (T@"NSString",R,C,N) outputFileType;
@property (T@"NSArray",R,N) availableMediaTypes;
@property (Tq,R) status;
@property (T@"NSError",R) error;
@property (T@"NSArray",C,N) metadata;
@property (TB,N) shouldOptimizeForNetworkUse;
@property (T@"NSURL",C,N) directoryForTemporaryFiles;
@property (T@"NSArray",R,N) inputs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAssetWriter initialize];
+[AVAssetWriter automaticallyNotifiesObserversForKey:];
+[AVAssetWriter _errorForOSStatus:];
+[AVAssetWriter assetWriterWithURL:fileType:error:];
```

## Instance methods

```
-[AVAssetWriter startWriting];
-[AVAssetWriter setMovieFragmentInterval:];
-[AVAssetWriter movieFragmentInterval];
-[AVAssetWriter setPreferredVolume:];
-[AVAssetWriter init];
-[AVAssetWriter preferredTransform];
-[AVAssetWriter overallDurationHint];
-[AVAssetWriter inputs];
-[AVAssetWriter flush];
-[AVAssetWriter preferredRate];
-[AVAssetWriter dealloc];
-[AVAssetWriter initWithContentType:];
-[AVAssetWriter status];
-[AVAssetWriter setPreferredTransform:];
-[AVAssetWriter error];
-[AVAssetWriter metadata];
-[AVAssetWriter isDefunct];
-[AVAssetWriter preferredVolume];
-[AVAssetWriter setDelegate:];
-[AVAssetWriter outputFileType];
-[AVAssetWriter setMetadata:];
-[AVAssetWriter delegate];
-[AVAssetWriter description];
-[AVAssetWriter _helper];
-[AVAssetWriter outputURL];
-[AVAssetWriter finishWriting];
-[AVAssetWriter addInput:];
-[AVAssetWriter cancelWriting];
-[AVAssetWriter finishWritingWithCompletionHandler:];
-[AVAssetWriter initWithURL:fileType:error:];
-[AVAssetWriter startSessionAtSourceTime:];
-[AVAssetWriter canAddInput:];
-[AVAssetWriter setProducesCombinableFragments:];
-[AVAssetWriter setShouldOptimizeForNetworkUse:];
-[AVAssetWriter _initInternalObject];
-[AVAssetWriter _setHelper:ifCurrentHelper:];
-[AVAssetWriter _setHelper:ifCurrentHelper:withBlock:];
-[AVAssetWriter _supportsSampleReferencesReturningError:];
-[AVAssetWriter _transitionToFailedStatusWithError:];
-[AVAssetWriter addCallbackToCancelDuringDeallocation:];
-[AVAssetWriter addInputGroup:];
-[AVAssetWriter availableMediaTypes];
-[AVAssetWriter canAddInputGroup:];
-[AVAssetWriter canApplyOutputSettings:forMediaType:];
-[AVAssetWriter declareKeyPathDependenciesWithRegistry:];
-[AVAssetWriter directoryForTemporaryFiles];
-[AVAssetWriter endSessionAtSourceTime:];
-[AVAssetWriter finishWritingDelegate];
-[AVAssetWriter flushSegment];
-[AVAssetWriter initWithFileType:error:];
-[AVAssetWriter initialMovieFragmentInterval];
-[AVAssetWriter initialMovieFragmentSequenceNumber];
-[AVAssetWriter initialSegmentStartTime];
-[AVAssetWriter inputGroups];
-[AVAssetWriter isProVideoStorageSupported];
-[AVAssetWriter movieTimeScale];
-[AVAssetWriter outputFileTypeProfile];
-[AVAssetWriter preferredOutputSegmentInterval];
-[AVAssetWriter producesCombinableFragments];
-[AVAssetWriter requiresInProcessOperation];
-[AVAssetWriter setDirectoryForTemporaryFiles:];
-[AVAssetWriter setFinishWritingDelegate:];
-[AVAssetWriter setInitialMovieFragmentInterval:];
-[AVAssetWriter setInitialMovieFragmentSequenceNumber:];
-[AVAssetWriter setInitialSegmentStartTime:];
-[AVAssetWriter setMovieTimeScale:];
-[AVAssetWriter setOutputFileTypeProfile:];
-[AVAssetWriter setOverallDurationHint:];
-[AVAssetWriter setPreferredOutputSegmentInterval:];
-[AVAssetWriter setPreferredRate:];
-[AVAssetWriter setRequiresInProcessOperation:];
-[AVAssetWriter setUsesProVideoStorage:];
-[AVAssetWriter setWritesSinglePassUsingPredeterminedFileSize:mediaDataSize:];
-[AVAssetWriter shouldOptimizeForNetworkUse];
-[AVAssetWriter usesProVideoStorage];
```
