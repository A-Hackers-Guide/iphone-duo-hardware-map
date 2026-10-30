# `AVAssetReaderTrackOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetReaderOutput`
- 1 instance variables, 4 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"AVAssetReaderTrackOutputInternal" _trackOutputInternal;
```

## Properties

```
@property (TB,R,N,G_isAttachedToAdaptor) attachedToAdaptor;
@property (T@"AVAssetTrack",R,N) track;
@property (T@"NSDictionary",R,N) outputSettings;
@property (T@"NSString",C,N) audioTimePitchAlgorithm;
```

## Class methods

```
+[AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:outputSettings:];
```

## Instance methods

```
-[AVAssetReaderTrackOutput outputSettings];
-[AVAssetReaderTrackOutput _isAttachedToAdaptor];
-[AVAssetReaderTrackOutput setAppliesPreferredTrackTransform:];
-[AVAssetReaderTrackOutput _copyNextSampleBufferForAdaptor];
-[AVAssetReaderTrackOutput _formatDescriptions];
-[AVAssetReaderTrackOutput init];
-[AVAssetReaderTrackOutput dealloc];
-[AVAssetReaderTrackOutput _getUniformMediaSubtypeIfExists];
-[AVAssetReaderTrackOutput _trimsSampleDurations];
-[AVAssetReaderTrackOutput initWithTrack:outputSettings:];
-[AVAssetReaderTrackOutput audioTimePitchAlgorithm];
-[AVAssetReaderTrackOutput limitsImageQueueCapacityToOneFrame];
-[AVAssetReaderTrackOutput setLimitsImageQueueCapacityToOneFrame:];
-[AVAssetReaderTrackOutput appliesPreferredTrackTransform];
-[AVAssetReaderTrackOutput track];
-[AVAssetReaderTrackOutput copyNextSampleBuffer];
-[AVAssetReaderTrackOutput _attachedAdaptor];
-[AVAssetReaderTrackOutput description];
-[AVAssetReaderTrackOutput _enableTrackExtractionReturningError:];
-[AVAssetReaderTrackOutput _asset];
-[AVAssetReaderTrackOutput setAudioTimePitchAlgorithm:];
-[AVAssetReaderTrackOutput mediaType];
-[AVAssetReaderTrackOutput _setAttachedAdaptor:];
-[AVAssetReaderTrackOutput _figAssetReaderExtractionOptions];
```
