# `AVAssetReaderOutputAnnotationAdaptor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAssetReaderOutputAdaptor`
- 2 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"AVAssetReaderTrackOutput" _trackOutput;
@"AVAssetReaderOutputMetadataAdaptor" _assetReaderOutputMetadataAdaptor;
```

## Properties

```
@property (T@"AVAssetReaderTrackOutput",R,N) assetReaderTrackOutput;
```

## Class methods

```
+[AVAssetReaderOutputAnnotationAdaptor assetReaderOutputAnnotationAdaptorWithAssetReaderTrackOutput:];
```

## Instance methods

```
-[AVAssetReaderOutputAnnotationAdaptor init];
-[AVAssetReaderOutputAnnotationAdaptor dealloc];
-[AVAssetReaderOutputAnnotationAdaptor initWithAssetReaderTrackOutput:];
-[AVAssetReaderOutputAnnotationAdaptor addExtractionForOutput:figAssetReader:options:withOutputExtactionID:];
-[AVAssetReaderOutputAnnotationAdaptor assetReaderTrackOutput];
-[AVAssetReaderOutputAnnotationAdaptor nextAnnotation];
```
