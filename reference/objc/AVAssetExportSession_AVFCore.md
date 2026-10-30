# `AVAssetExportSession`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 9 properties, 61 instance methods, 7 class methods

## Instance variables

```
@"AVAssetExportSessionInternal" _exportSession;
```

## Properties

```
@property (T@"NSString",R,N) presetName;
@property (T@"AVAsset",R,&,N) asset;
@property (T@"NSString",C,N) outputFileType;
@property (T@"NSURL",C,N) outputURL;
@property (TB,N) shouldOptimizeForNetworkUse;
@property (TB,N) allowsParallelizedExport;
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (Tf,R,N) progress;
```

## Class methods

```
+[AVAssetExportSession maximumDurationForPreset:properties:];
+[AVAssetExportSession allExportPresets];
+[AVAssetExportSession determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:];
+[AVAssetExportSession estimatedOutputFileLengthForPreset:duration:properties:];
+[AVAssetExportSession exportPresetsCompatibleWithAsset:];
+[AVAssetExportSession exportSessionWithAsset:presetName:];
+[AVAssetExportSession keyPathsForValuesAffectingEstimatedOutputFileLength];
```

## Instance methods

```
-[AVAssetExportSession setTimeRange:];
-[AVAssetExportSession asset];
-[AVAssetExportSession setOutputFileType:];
-[AVAssetExportSession timeRange];
-[AVAssetExportSession setVideoComposition:];
-[AVAssetExportSession init];
-[AVAssetExportSession maxDuration];
-[AVAssetExportSession dealloc];
-[AVAssetExportSession status];
-[AVAssetExportSession audioTimePitchAlgorithm];
-[AVAssetExportSession error];
-[AVAssetExportSession metadata];
-[AVAssetExportSession isDefunct];
-[AVAssetExportSession progress];
-[AVAssetExportSession setOutputURL:];
-[AVAssetExportSession outputFileType];
-[AVAssetExportSession setMetadata:];
-[AVAssetExportSession description];
-[AVAssetExportSession setAudioTimePitchAlgorithm:];
-[AVAssetExportSession supportedFileTypes];
-[AVAssetExportSession outputURL];
-[AVAssetExportSession videoComposition];
-[AVAssetExportSession AVExportSessionExportAsynchronouslyCompletionHandler];
-[AVAssetExportSession fileLengthLimit];
-[AVAssetExportSession setShouldOptimizeForNetworkUse:];
-[AVAssetExportSession _simulateMediaServicesWereResetForTesting];
-[AVAssetExportSession allowsAppleOnlySWAV1Decode];
-[AVAssetExportSession allowsParallelizedExport];
-[AVAssetExportSession audioMix];
-[AVAssetExportSession audioTrackGroupHandling];
-[AVAssetExportSession canPerformMultiplePassesOverSourceMediaData];
-[AVAssetExportSession cancelExport];
-[AVAssetExportSession configureForResumableExportWithCompletionHandler:];
-[AVAssetExportSession customVideoCompositor];
-[AVAssetExportSession determineCompatibleFileTypesWithCompletionHandler:];
-[AVAssetExportSession directoryForTemporaryFiles];
-[AVAssetExportSession estimateMaximumDurationWithCompletionHandler:];
-[AVAssetExportSession estimateOutputFileLengthWithCompletionHandler:];
-[AVAssetExportSession estimatedOutputFileLength];
-[AVAssetExportSession exportAsynchronouslyWithCompletionHandler:];
-[AVAssetExportSession initWithAsset:presetName:];
-[AVAssetExportSession makeLookupableSpatialVideoConfigurations:];
-[AVAssetExportSession maximizePowerEfficiency];
-[AVAssetExportSession metadataItemFilter];
-[AVAssetExportSession minVideoFrameDuration];
-[AVAssetExportSession preserveSyncFrames];
-[AVAssetExportSession presetName];
-[AVAssetExportSession setAllowsAppleOnlySWAV1Decode:];
-[AVAssetExportSession setAllowsParallelizedExport:];
-[AVAssetExportSession setAudioMix:];
-[AVAssetExportSession setAudioTrackGroupHandling:];
-[AVAssetExportSession setCanPerformMultiplePassesOverSourceMediaData:];
-[AVAssetExportSession setDirectoryForTemporaryFiles:];
-[AVAssetExportSession setFileLengthLimit:];
-[AVAssetExportSession setMaximizePowerEfficiency:];
-[AVAssetExportSession setMetadataItemFilter:];
-[AVAssetExportSession setMinVideoFrameDuration:];
-[AVAssetExportSession setPreserveSyncFrames:];
-[AVAssetExportSession setVideoFrameRateConversionAlgorithm:];
-[AVAssetExportSession shouldOptimizeForNetworkUse];
-[AVAssetExportSession videoFrameRateConversionAlgorithm];
```
