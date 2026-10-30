# `AVAssetReaderOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 38 instance methods, 2 class methods

## Instance variables

```
@"AVAssetReaderOutputInternal" _internal;
```

## Properties

```
@property (TB,N,GhasProvider,SsetHasProvider:) hasProvider;
@property (T@"AVWeakReference",R,N,G_weakReferenceToAssetReader) weakReferenceToAssetReader;
@property (Ti,N,G_extractionID,S_setExtractionID:) extractionID;
@property (T@"NSDictionary",R,N,G_figAssetReaderExtractionOptions) figAssetReaderExtractionOptions;
@property (TB,R,N,G_trimsSampleDurations) trimsSampleDurations;
@property (T@"NSString",R,N) mediaType;
@property (TB,N) alwaysCopiesSampleData;
```

## Class methods

```
+[AVAssetReaderOutput initialize];
+[AVAssetReaderOutput _figAssetReaderVideoScalingPropertiesFromVideoSettings:withFormatDescription:];
```

## Instance methods

```
-[AVAssetReaderOutput init];
-[AVAssetReaderOutput dealloc];
-[AVAssetReaderOutput _trimsSampleDurations];
-[AVAssetReaderOutput _status];
-[AVAssetReaderOutput copyNextSampleBuffer];
-[AVAssetReaderOutput _enableTrackExtractionReturningError:];
-[AVAssetReaderOutput _asset];
-[AVAssetReaderOutput mediaType];
-[AVAssetReaderOutput _isFinished];
-[AVAssetReaderOutput _figAssetReader];
-[AVAssetReaderOutput _figAssetReaderExtractionOptions];
-[AVAssetReaderOutput hasProvider];
-[AVAssetReaderOutput setAlwaysCopiesSampleData:];
-[AVAssetReaderOutput setHasProvider:];
-[AVAssetReaderOutput _markAsFinished];
-[AVAssetReaderOutput _attachToWeakReferenceToAssetReader:];
-[AVAssetReaderOutput _cancelReading];
-[AVAssetReaderOutput _errorForOSStatus:];
-[AVAssetReaderOutput _extractionID];
-[AVAssetReaderOutput _figAssetReaderDecodeError];
-[AVAssetReaderOutput _figAssetReaderFailed];
-[AVAssetReaderOutput _figAssetReaderSampleBufferDidBecomeAvailableForExtractionID:];
-[AVAssetReaderOutput _figAssetReaderServerConnectionDied];
-[AVAssetReaderOutput _prepareForReadingReturningError:];
-[AVAssetReaderOutput _setExtractionID:];
-[AVAssetReaderOutput _setFigAssetReader:];
-[AVAssetReaderOutput _updateTimeRangesOnFigAssetReaderReturningError:];
-[AVAssetReaderOutput _weakReferenceToAssetReader];
-[AVAssetReaderOutput alwaysCopiesSampleData];
-[AVAssetReaderOutput currentTimeRanges];
-[AVAssetReaderOutput disablesMultithreadedAndAsyncVideoDecompression];
-[AVAssetReaderOutput markConfigurationAsFinal];
-[AVAssetReaderOutput maximizePowerEfficiency];
-[AVAssetReaderOutput resetForReadingTimeRanges:];
-[AVAssetReaderOutput setDisablesMultithreadedAndAsyncVideoDecompression:];
-[AVAssetReaderOutput setMaximizePowerEfficiency:];
-[AVAssetReaderOutput setSupportsRandomAccess:];
-[AVAssetReaderOutput supportsRandomAccess];
```
