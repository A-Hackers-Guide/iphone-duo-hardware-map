# `JFXAVMediaMetaDataReader`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXAVMediaDataReader`
- Protocols: `JFXMediaMetadataReader`
- 3 instance variables, 13 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"AVAssetReaderOutputMetadataAdaptor" _assetReaderOutputMetadataAdaptor;
@"AVMetadataItem" _currentMetadataItem;
@"AVMetadataItem" _nextMetadataItem;
```

## Properties

```
@property (T@"AVAssetReaderOutputMetadataAdaptor",&,N,V_assetReaderOutputMetadataAdaptor) assetReaderOutputMetadataAdaptor;
@property (T@"AVMetadataItem",&,N,V_currentMetadataItem) currentMetadataItem;
@property (T@"AVMetadataItem",&,N,V_nextMetadataItem) nextMetadataItem;
@property (T{?={?=qiIq}{?=qiIq}},R,N) readableTimeRange;
@property (TB,N) isScrubbing;
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (TQ,R,N) signPostID;
@property (T@"NSString",R,N) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXAVMediaMetaDataReader JFX_preloadData];
-[JFXAVMediaMetaDataReader assetReaderOutputMetadataAdaptor];
-[JFXAVMediaMetaDataReader cancelReadingForReaderReset];
-[JFXAVMediaMetaDataReader createAssetReaderTrackOutput];
-[JFXAVMediaMetaDataReader currentMetadataItem];
-[JFXAVMediaMetaDataReader didUpdateReadingRange];
-[JFXAVMediaMetaDataReader hasRemainingAvailableData];
-[JFXAVMediaMetaDataReader metadataForTime:];
-[JFXAVMediaMetaDataReader nextMetadataItem];
-[JFXAVMediaMetaDataReader readAheadToTime:];
-[JFXAVMediaMetaDataReader readAndDiscardRemainingAvailableData];
-[JFXAVMediaMetaDataReader setAssetReaderOutputMetadataAdaptor:];
-[JFXAVMediaMetaDataReader setCurrentMetadataItem:];
-[JFXAVMediaMetaDataReader setNextMetadataItem:];
-[JFXAVMediaMetaDataReader startTimeOfCurrentData];
```
