# `AVMutableMovie`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMovie`
- 1 instance variables, 9 properties, 62 instance methods, 4 class methods

## Instance variables

```
@"AVMutableMovieInternal" _mutableMovieInternal;
```

## Properties

```
@property (TB,N,GisModified) modified;
@property (T@"AVMediaDataStorage",C,N) defaultMediaDataStorage;
@property (T{?=qiIq},N) interleavingPeriod;
@property (T@"NSArray",C,N) metadata;
@property (Tf,N) preferredRate;
@property (Tf,N) preferredVolume;
@property (T{CGAffineTransform=dddddd},N) preferredTransform;
@property (Ti,N) timescale;
@property (T@"NSArray",R,N) tracks;
```

## Class methods

```
+[AVMutableMovie expectsPropertyRevisedNotifications];
+[AVMutableMovie movieWithData:options:error:];
+[AVMutableMovie movieWithSettingsFromMovie:options:error:];
+[AVMutableMovie movieWithURL:options:error:];
```

## Instance methods

```
-[AVMutableMovie trackReferences];
-[AVMutableMovie setModified:];
-[AVMutableMovie tracksWithMediaCharacteristic:];
-[AVMutableMovie tracksWithMediaType:];
-[AVMutableMovie setPreferredVolume:];
-[AVMutableMovie metadataForFormat:];
-[AVMutableMovie _removeFigAssetNotifications];
-[AVMutableMovie statusOfValueForKey:error:];
-[AVMutableMovie init];
-[AVMutableMovie preferredTransform];
-[AVMutableMovie initWithURL:options:];
-[AVMutableMovie preferredRate];
-[AVMutableMovie data];
-[AVMutableMovie dealloc];
-[AVMutableMovie _classForTrackInspectors];
-[AVMutableMovie removeTimeRange:];
-[AVMutableMovie mutableTrackCompatibleWithTrack:];
-[AVMutableMovie removeTrack:];
-[AVMutableMovie initWithData:options:error:];
-[AVMutableMovie setPreferredTransform:];
-[AVMutableMovie metadata];
-[AVMutableMovie duration];
-[AVMutableMovie isDefunct];
-[AVMutableMovie trackWithTrackID:];
-[AVMutableMovie preferredVolume];
-[AVMutableMovie availableMetadataFormats];
-[AVMutableMovie insertEmptyTimeRange:];
-[AVMutableMovie scaleTimeRange:toDuration:];
-[AVMutableMovie setMetadata:];
-[AVMutableMovie description];
-[AVMutableMovie initWithData:options:];
-[AVMutableMovie isModified];
-[AVMutableMovie fileType];
-[AVMutableMovie copyWithZone:];
-[AVMutableMovie tracks];
-[AVMutableMovie _copyFormatReader];
-[AVMutableMovie URL];
-[AVMutableMovie _addFigAssetNotifications];
-[AVMutableMovie loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVMutableMovie initWithURL:options:error:];
-[AVMutableMovie _addMutableTrackWithMediaType:copySettingsFromTrack:options:];
-[AVMutableMovie _figMutableMovie];
-[AVMutableMovie _initWithFigAsset:];
-[AVMutableMovie _initWithFigError:userInfo:];
-[AVMutableMovie _initWithFormatReader:URL:data:options:];
-[AVMutableMovie _initializationOptions];
-[AVMutableMovie _mutableTracks];
-[AVMutableMovie _signalMetadataUpdated];
-[AVMutableMovie _signalTracksUpdated];
-[AVMutableMovie addMutableTrackWithMediaType:copySettingsFromTrack:options:];
-[AVMutableMovie addMutableTracksCopyingSettingsFromTracks:options:];
-[AVMutableMovie defaultMediaDataStorage];
-[AVMutableMovie initWithFileType:copySettingsFromMovie:options:];
-[AVMutableMovie initWithSettingsFromMovie:options:];
-[AVMutableMovie initWithSettingsFromMovie:options:error:];
-[AVMutableMovie insertTimeRange:ofAsset:atTime:copySampleData:error:];
-[AVMutableMovie interleavingPeriod];
-[AVMutableMovie setDefaultMediaDataStorage:];
-[AVMutableMovie setInterleavingPeriod:];
-[AVMutableMovie setPreferredRate:];
-[AVMutableMovie setTimescale:];
-[AVMutableMovie timescale];
```
