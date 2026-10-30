# `AVMutableMovieTrack`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMovieTrack`
- 1 instance variables, 9 properties, 72 instance methods, 2 class methods

## Instance variables

```
@"AVMutableMovieTrackInternal" _mutableMovieTrackInternal;
```

## Properties

```
@property (T@"NSArray",R,N) formatDescriptions;
@property (T@"NSArray",C,N) metadata;
@property (T@"AVMediaDataStorage",C,N) mediaDataStorage;
@property (T@"NSURL",C,N) sampleReferenceBaseURL;
@property (TB,N,GisEnabled) enabled;
@property (Tq,N) alternateGroupID;
@property (TB,N,GisModified) modified;
@property (TB,R,N) hasProtectedContent;
@property (Ti,N) timescale;
```

## Class methods

```
+[AVMutableMovieTrack expectsPropertyRevisedNotifications];
+[AVMutableMovieTrack trackWithTrackID:forMovie:];
```

## Instance methods

```
-[AVMutableMovieTrack setNaturalSize:];
-[AVMutableMovieTrack dimensions];
-[AVMutableMovieTrack setModified:];
-[AVMutableMovieTrack setExtendedLanguageTag:];
-[AVMutableMovieTrack formatDescriptions];
-[AVMutableMovieTrack _figAssetTrack];
-[AVMutableMovieTrack setPreferredVolume:];
-[AVMutableMovieTrack metadataForFormat:];
-[AVMutableMovieTrack layer];
-[AVMutableMovieTrack replaceFormatDescription:withFormatDescription:];
-[AVMutableMovieTrack statusOfValueForKey:error:];
-[AVMutableMovieTrack hasProtectedContent];
-[AVMutableMovieTrack preferredTransform];
-[AVMutableMovieTrack trackID];
-[AVMutableMovieTrack naturalSize];
-[AVMutableMovieTrack mediaPresentationTimeRange];
-[AVMutableMovieTrack dealloc];
-[AVMutableMovieTrack removeTimeRange:];
-[AVMutableMovieTrack setPreferredTransform:];
-[AVMutableMovieTrack metadata];
-[AVMutableMovieTrack isEnabled];
-[AVMutableMovieTrack preferredVolume];
-[AVMutableMovieTrack languageCode];
-[AVMutableMovieTrack availableMetadataFormats];
-[AVMutableMovieTrack insertEmptyTimeRange:];
-[AVMutableMovieTrack locale];
-[AVMutableMovieTrack alternateGroupID];
-[AVMutableMovieTrack setEnabled:];
-[AVMutableMovieTrack scaleTimeRange:toDuration:];
-[AVMutableMovieTrack removeTrackAssociationToTrack:type:];
-[AVMutableMovieTrack setMetadata:];
-[AVMutableMovieTrack description];
-[AVMutableMovieTrack setAlternateGroupID:];
-[AVMutableMovieTrack isModified];
-[AVMutableMovieTrack addTrackAssociationToTrack:type:];
-[AVMutableMovieTrack extendedLanguageTag];
-[AVMutableMovieTrack loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVMutableMovieTrack setLanguageCode:];
-[AVMutableMovieTrack mediaDecodeTimeRange];
-[AVMutableMovieTrack setLayer:];
-[AVMutableMovieTrack setPreferredMediaChunkDuration:];
-[AVMutableMovieTrack _addFigAssetTrackNotifications];
-[AVMutableMovieTrack _figMutableMovie];
-[AVMutableMovieTrack _removeFigAssetTrackNotifications];
-[AVMutableMovieTrack _setSize:forProperty:];
-[AVMutableMovieTrack _setString:forProperty:];
-[AVMutableMovieTrack _signalMetadataUpdated];
-[AVMutableMovieTrack _sizeForProperty:];
-[AVMutableMovieTrack _stringForProperty:];
-[AVMutableMovieTrack appendMediaData:dataOffset:];
-[AVMutableMovieTrack appendSampleBuffer:decodeTime:presentationTime:error:];
-[AVMutableMovieTrack cleanApertureDimensions];
-[AVMutableMovieTrack encodedPixelsDimensions];
-[AVMutableMovieTrack initWithTrackID:forMovie:];
-[AVMutableMovieTrack insertMediaTimeRange:intoTimeRange:];
-[AVMutableMovieTrack insertTimeRange:ofTrack:atTime:copySampleData:error:];
-[AVMutableMovieTrack isCompatibleWithFormatDescription:];
-[AVMutableMovieTrack mediaDataStorage];
-[AVMutableMovieTrack preferredMediaChunkAlignment];
-[AVMutableMovieTrack preferredMediaChunkDuration];
-[AVMutableMovieTrack preferredMediaChunkSize];
-[AVMutableMovieTrack productionApertureDimensions];
-[AVMutableMovieTrack sampleReferenceBaseURL];
-[AVMutableMovieTrack setCleanApertureDimensions:];
-[AVMutableMovieTrack setEncodedPixelsDimensions:];
-[AVMutableMovieTrack setMediaDataStorage:];
-[AVMutableMovieTrack setPreferredMediaChunkAlignment:];
-[AVMutableMovieTrack setPreferredMediaChunkSize:];
-[AVMutableMovieTrack setProductionApertureDimensions:];
-[AVMutableMovieTrack setSampleReferenceBaseURL:];
-[AVMutableMovieTrack setTimescale:];
-[AVMutableMovieTrack timescale];
```
