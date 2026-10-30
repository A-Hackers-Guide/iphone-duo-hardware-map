# `JFXDepthDataMediaReader`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXMediaVideoTrackReader`
- 5 instance variables, 15 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<JFXMediaVideoTrackReader>" _reader;
@"NSError" _lastDecodeError;
@"JFXMediaReaderDepthData" _cachedDepthData;
@"NSObject<OS_dispatch_queue>" _synchronizationQueue;
@"JFXDepthDecompressor" _depthDecompressor;
```

## Properties

```
@property (T@"<JFXMediaVideoTrackReader>",R,N,V_reader) reader;
@property (T@"NSError",&,N,V_lastDecodeError) lastDecodeError;
@property (T@"JFXMediaReaderDepthData",&,N,V_cachedDepthData) cachedDepthData;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_synchronizationQueue) synchronizationQueue;
@property (T@"JFXDepthDecompressor",&,N,V_depthDecompressor) depthDecompressor;
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
-[JFXDepthDataMediaReader setIsScrubbing:];
-[JFXDepthDataMediaReader isScrubbing];
-[JFXDepthDataMediaReader status];
-[JFXDepthDataMediaReader error];
-[JFXDepthDataMediaReader reader];
-[JFXDepthDataMediaReader name];
-[JFXDepthDataMediaReader synchronizationQueue];
-[JFXDepthDataMediaReader JFX_decompressAVDepthDataFromVideoTrackReaderSample:];
-[JFXDepthDataMediaReader JFX_readDepthDataForTime:];
-[JFXDepthDataMediaReader lastDecodeError];
-[JFXDepthDataMediaReader JFX_cachedDepthDataForTime:];
-[JFXDepthDataMediaReader cachedDepthData];
-[JFXDepthDataMediaReader beginReading];
-[JFXDepthDataMediaReader beginReadingAtTimeRange:];
-[JFXDepthDataMediaReader depthDataForTime:];
-[JFXDepthDataMediaReader depthDecompressor];
-[JFXDepthDataMediaReader initWithVideoTrackReader:];
-[JFXDepthDataMediaReader readableTimeRange];
-[JFXDepthDataMediaReader setCachedDepthData:];
-[JFXDepthDataMediaReader setDepthDecompressor:];
-[JFXDepthDataMediaReader setLastDecodeError:];
-[JFXDepthDataMediaReader signPostID];
-[JFXDepthDataMediaReader videoSampleForTime:];
```
