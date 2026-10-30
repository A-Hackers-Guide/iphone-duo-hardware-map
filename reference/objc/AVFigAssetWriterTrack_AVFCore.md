# `AVFigAssetWriterTrack`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 42 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _weakReference;
^{OpaqueFigAssetWriter=} _figAssetWriter;
i _trackID;
@"NSString" _mediaType;
@"AVMediaFileType" _mediaFileType;
@"NSObject<OS_dispatch_queue>" _aboveHighWaterLevelQueue;
B _aboveHighWaterLevel;
@"NSOperationQueue" _operationQueue;
@"NSObject<OS_dispatch_queue>" _finalVTCompressionSessionStateQueue;
@"NSDictionary" _finalVTCompressionSessionState;
@"AVWeakReference" _weakReferenceToAssetWriterInput;
```

## Properties

```
@property (T^{OpaqueFigAssetWriter=},R,N,V_figAssetWriter) figAssetWriter;
@property (T@"NSString",R,N,V_mediaType) mediaType;
@property (T@"AVMediaFileType",R,N,V_mediaFileType) mediaFileType;
@property (Ti,R,N,V_trackID) trackID;
@property (T^{__CVPixelBufferPool=},R,N) pixelBufferPool;
@property (TB,R,N) encoderSupportsMultiPass;
@property (TB,R,GisAboveHighWaterLevel) aboveHighWaterLevel;
@property (T@"AVWeakReference",&,V_weakReferenceToAssetWriterInput) weakReferenceToAssetWriterInput;
@property (T@"NSDictionary",R,GfinalVTCompressionSessionState) finalVTCompressionSessionState;
```

## Class methods

```
+[AVFigAssetWriterTrack assetWriterTrackWithFigAssetWriter:mediaType:mediaFileType:formatSpecification:sourcePixelBufferAttributes:multiPass:attachedAdaptor:error:];
```

## Instance methods

```
-[AVFigAssetWriterTrack setExtendedLanguageTag:];
-[AVFigAssetWriterTrack pixelBufferPool];
-[AVFigAssetWriterTrack init];
-[AVFigAssetWriterTrack trackID];
-[AVFigAssetWriterTrack dealloc];
-[AVFigAssetWriterTrack setAlternateGroupID:];
-[AVFigAssetWriterTrack mediaType];
-[AVFigAssetWriterTrack setLanguageCode:];
-[AVFigAssetWriterTrack setLayer:];
-[AVFigAssetWriterTrack setFigMetadata:];
-[AVFigAssetWriterTrack setTrackVolume:];
-[AVFigAssetWriterTrack weakReferenceToAssetWriterInput];
-[AVFigAssetWriterTrack setProvisionalAlternateGroupID:];
-[AVFigAssetWriterTrack _attachToFigAssetWriterUsingFormatSpecification:sourcePixelBufferAttributes:multiPass:error:];
-[AVFigAssetWriterTrack _figAssetWriterDidDropBelowLowWaterLevelForTrackID:];
-[AVFigAssetWriterTrack _figAssetWriterFinalCompressionSessionStateAvailable:finalCompressionSessionState:];
-[AVFigAssetWriterTrack _refreshAboveHighWaterLevel];
-[AVFigAssetWriterTrack addPixelBuffer:atPresentationTime:error:];
-[AVFigAssetWriterTrack addSampleBuffer:error:];
-[AVFigAssetWriterTrack addTaggedPixelBufferGroup:atPresentationTime:error:];
-[AVFigAssetWriterTrack beginPassReturningError:];
-[AVFigAssetWriterTrack encoderSupportsMultiPass];
-[AVFigAssetWriterTrack endPassWithCompletionHandler:];
-[AVFigAssetWriterTrack figAssetWriter];
-[AVFigAssetWriterTrack finalVTCompressionSessionState];
-[AVFigAssetWriterTrack initWithFigAssetWriter:mediaType:mediaFileType:formatSpecification:sourcePixelBufferAttributes:multiPass:error:];
-[AVFigAssetWriterTrack isAboveHighWaterLevel];
-[AVFigAssetWriterTrack markEndOfDataReturningError:];
-[AVFigAssetWriterTrack mediaFileType];
-[AVFigAssetWriterTrack prepareToEndSession];
-[AVFigAssetWriterTrack setExcludeFromAutoSelection:];
-[AVFigAssetWriterTrack setFigDimensions:];
-[AVFigAssetWriterTrack setFigTrackMatrix:];
-[AVFigAssetWriterTrack setFormatDescriptions:];
-[AVFigAssetWriterTrack setMarksOutputTrackAsEnabled:];
-[AVFigAssetWriterTrack setMediaDataLocation:];
-[AVFigAssetWriterTrack setMediaTimeScale:];
-[AVFigAssetWriterTrack setPreferredChunkAlignment:];
-[AVFigAssetWriterTrack setPreferredChunkDuration:];
-[AVFigAssetWriterTrack setPreferredChunkSize:];
-[AVFigAssetWriterTrack setSampleReferenceBaseURL:];
-[AVFigAssetWriterTrack setWeakReferenceToAssetWriterInput:];
```
