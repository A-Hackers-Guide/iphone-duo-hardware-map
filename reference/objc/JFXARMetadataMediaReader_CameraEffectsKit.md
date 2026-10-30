# `JFXARMetadataMediaReader`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXMediaMetadataReader`
- 4 instance variables, 14 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<JFXMediaMetadataReader>" _reader;
@"NSError" _lastDecodeError;
@"JFXARMetadataMediaReaderItem" _cachedARMetadata;
@"NSObject<OS_dispatch_queue>" _synchronizationQueue;
```

## Properties

```
@property (T@"<JFXMediaMetadataReader>",R,N,V_reader) reader;
@property (T@"NSError",&,N,V_lastDecodeError) lastDecodeError;
@property (T@"JFXARMetadataMediaReaderItem",&,N,V_cachedARMetadata) cachedARMetadata;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_synchronizationQueue) synchronizationQueue;
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

## Class methods

```
+[JFXARMetadataMediaReader initialize];
```

## Instance methods

```
-[JFXARMetadataMediaReader setIsScrubbing:];
-[JFXARMetadataMediaReader isScrubbing];
-[JFXARMetadataMediaReader status];
-[JFXARMetadataMediaReader error];
-[JFXARMetadataMediaReader reader];
-[JFXARMetadataMediaReader name];
-[JFXARMetadataMediaReader initWithMetadataReader:];
-[JFXARMetadataMediaReader synchronizationQueue];
-[JFXARMetadataMediaReader lastDecodeError];
-[JFXARMetadataMediaReader JFX_ARMetadataFromMetadataReaderItem:];
-[JFXARMetadataMediaReader arMetadataItemForTime:];
-[JFXARMetadataMediaReader beginReading];
-[JFXARMetadataMediaReader beginReadingAtTimeRange:];
-[JFXARMetadataMediaReader cachedARMetadata];
-[JFXARMetadataMediaReader metadataForTime:];
-[JFXARMetadataMediaReader readableTimeRange];
-[JFXARMetadataMediaReader setCachedARMetadata:];
-[JFXARMetadataMediaReader setLastDecodeError:];
-[JFXARMetadataMediaReader signPostID];
```
