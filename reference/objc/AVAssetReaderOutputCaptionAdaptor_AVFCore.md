# `AVAssetReaderOutputCaptionAdaptor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAssetReaderOutputAdaptor`
- 1 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"AVAssetReaderOutputCaptionAdaptorInternal" _internal;
```

## Properties

```
@property (T@"<AVAssetReaderCaptionValidationHandling>",W) validationDelegate;
@property (T@"AVAssetReaderTrackOutput",R,N) assetReaderTrackOutput;
```

## Class methods

```
+[AVAssetReaderOutputCaptionAdaptor assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:];
```

## Instance methods

```
-[AVAssetReaderOutputCaptionAdaptor dealloc];
-[AVAssetReaderOutputCaptionAdaptor initWithAssetReaderTrackOutput:];
-[AVAssetReaderOutputCaptionAdaptor _readSampleBuffersAndReturnAVCaption];
-[AVAssetReaderOutputCaptionAdaptor addExtractionForOutput:figAssetReader:options:withOutputExtactionID:];
-[AVAssetReaderOutputCaptionAdaptor appendOutputCaptionGroup:];
-[AVAssetReaderOutputCaptionAdaptor assetReaderTrackOutput];
-[AVAssetReaderOutputCaptionAdaptor captionsNotPresentInPreviousGroupsInCaptionGroup:];
-[AVAssetReaderOutputCaptionAdaptor nextCaptionGroup];
-[AVAssetReaderOutputCaptionAdaptor pairedAVCaptionForFigCaption:];
-[AVAssetReaderOutputCaptionAdaptor setFigCaptionToAVCaptionMapping:];
-[AVAssetReaderOutputCaptionAdaptor setValidationDelegate:];
-[AVAssetReaderOutputCaptionAdaptor validationDelegate];
```
