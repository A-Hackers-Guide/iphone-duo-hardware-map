# `AVAssetWriterConfigurationState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 24 properties, 49 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _URL;
@"<AVAssetWriterDelegate>" _delegate;
@"AVMediaFileType" _mediaFileType;
{?="value"q"timescale"i"flags"I"epoch"q} _movieFragmentInterval;
{?="value"q"timescale"i"flags"I"epoch"q} _initialMovieFragmentInterval;
{?="value"q"timescale"i"flags"I"epoch"q} _overallDurationHint;
B _shouldOptimizeForNetworkUse;
@"NSURL" _directoryForTemporaryFiles;
@"NSArray" _metadataItems;
i _movieTimeScale;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _preferredTransform;
f _preferredVolume;
f _preferredRate;
q _singlePassFileSize;
q _singlePassMediaDataSize;
@"NSArray" _inputs;
@"NSArray" _inputGroups;
{?="value"q"timescale"i"flags"I"epoch"q} _preferredOutputSegmentInterval;
{?="value"q"timescale"i"flags"I"epoch"q} _initialSegmentStartTime;
@"NSString" _outputFileTypeProfile;
q _initialMovieFragmentSequenceNumber;
B _producesCombinableFragments;
B _usesProVideoStorage;
B _requiresInProcessOperation;
```

## Properties

```
@property (T@"NSURL",C,N,V_URL) URL;
@property (T@"<AVAssetWriterDelegate>",W,V_delegate) delegate;
@property (T@"AVMediaFileType",C,N,V_mediaFileType) mediaFileType;
@property (T{?=qiIq},N,V_movieFragmentInterval) movieFragmentInterval;
@property (T{?=qiIq},N,V_initialMovieFragmentInterval) initialMovieFragmentInterval;
@property (T{?=qiIq},N,V_overallDurationHint) overallDurationHint;
@property (TB,N,V_shouldOptimizeForNetworkUse) shouldOptimizeForNetworkUse;
@property (T@"NSURL",C,N,V_directoryForTemporaryFiles) directoryForTemporaryFiles;
@property (T@"NSArray",C,N,V_metadataItems) metadataItems;
@property (Ti,N,V_movieTimeScale) movieTimeScale;
@property (T{CGAffineTransform=dddddd},N,V_preferredTransform) preferredTransform;
@property (Tf,N,V_preferredVolume) preferredVolume;
@property (Tf,N,V_preferredRate) preferredRate;
@property (Tq,N,V_singlePassFileSize) singlePassFileSize;
@property (Tq,N,V_singlePassMediaDataSize) singlePassMediaDataSize;
@property (T@"NSArray",C,N,V_inputs) inputs;
@property (T@"NSArray",C,N,V_inputGroups) inputGroups;
@property (T{?=qiIq},N,V_preferredOutputSegmentInterval) preferredOutputSegmentInterval;
@property (T{?=qiIq},N,V_initialSegmentStartTime) initialSegmentStartTime;
@property (T@"NSString",C,N,V_outputFileTypeProfile) outputFileTypeProfile;
@property (Tq,N,V_initialMovieFragmentSequenceNumber) initialMovieFragmentSequenceNumber;
@property (TB,N,V_producesCombinableFragments) producesCombinableFragments;
@property (TB,N,V_usesProVideoStorage) usesProVideoStorage;
@property (TB,N,V_requiresInProcessOperation) requiresInProcessOperation;
```

## Instance methods

```
-[AVAssetWriterConfigurationState setMovieFragmentInterval:];
-[AVAssetWriterConfigurationState movieFragmentInterval];
-[AVAssetWriterConfigurationState setPreferredVolume:];
-[AVAssetWriterConfigurationState metadataItems];
-[AVAssetWriterConfigurationState preferredTransform];
-[AVAssetWriterConfigurationState overallDurationHint];
-[AVAssetWriterConfigurationState inputs];
-[AVAssetWriterConfigurationState preferredRate];
-[AVAssetWriterConfigurationState dealloc];
-[AVAssetWriterConfigurationState setPreferredTransform:];
-[AVAssetWriterConfigurationState preferredVolume];
-[AVAssetWriterConfigurationState setDelegate:];
-[AVAssetWriterConfigurationState setURL:];
-[AVAssetWriterConfigurationState setInputs:];
-[AVAssetWriterConfigurationState delegate];
-[AVAssetWriterConfigurationState URL];
-[AVAssetWriterConfigurationState setInputGroups:];
-[AVAssetWriterConfigurationState setProducesCombinableFragments:];
-[AVAssetWriterConfigurationState setShouldOptimizeForNetworkUse:];
-[AVAssetWriterConfigurationState directoryForTemporaryFiles];
-[AVAssetWriterConfigurationState initialMovieFragmentInterval];
-[AVAssetWriterConfigurationState initialMovieFragmentSequenceNumber];
-[AVAssetWriterConfigurationState initialSegmentStartTime];
-[AVAssetWriterConfigurationState inputGroups];
-[AVAssetWriterConfigurationState mediaFileType];
-[AVAssetWriterConfigurationState movieTimeScale];
-[AVAssetWriterConfigurationState outputFileTypeProfile];
-[AVAssetWriterConfigurationState preferredOutputSegmentInterval];
-[AVAssetWriterConfigurationState producesCombinableFragments];
-[AVAssetWriterConfigurationState requiresInProcessOperation];
-[AVAssetWriterConfigurationState setDirectoryForTemporaryFiles:];
-[AVAssetWriterConfigurationState setInitialMovieFragmentInterval:];
-[AVAssetWriterConfigurationState setInitialMovieFragmentSequenceNumber:];
-[AVAssetWriterConfigurationState setInitialSegmentStartTime:];
-[AVAssetWriterConfigurationState setMediaFileType:];
-[AVAssetWriterConfigurationState setMetadataItems:];
-[AVAssetWriterConfigurationState setMovieTimeScale:];
-[AVAssetWriterConfigurationState setOutputFileTypeProfile:];
-[AVAssetWriterConfigurationState setOverallDurationHint:];
-[AVAssetWriterConfigurationState setPreferredOutputSegmentInterval:];
-[AVAssetWriterConfigurationState setPreferredRate:];
-[AVAssetWriterConfigurationState setRequiresInProcessOperation:];
-[AVAssetWriterConfigurationState setSinglePassFileSize:];
-[AVAssetWriterConfigurationState setSinglePassMediaDataSize:];
-[AVAssetWriterConfigurationState setUsesProVideoStorage:];
-[AVAssetWriterConfigurationState shouldOptimizeForNetworkUse];
-[AVAssetWriterConfigurationState singlePassFileSize];
-[AVAssetWriterConfigurationState singlePassMediaDataSize];
-[AVAssetWriterConfigurationState usesProVideoStorage];
```
