# `AVMomentCaptureMovieRecordingSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 8 properties, 22 instance methods, 2 class methods

## Instance variables

```
q _uniqueID;
Q _userInitiatedCaptureTime;
@"NSString" _videoCodecType;
@"NSURL" _movieFileURL;
@"NSArray" _movieMetadata;
B _autoSpatialOverCaptureEnabled;
@"NSString" _spatialOverCaptureGroupIdentifier;
@"NSURL" _spatialOverCaptureMovieFileURL;
@"NSArray" _spatialOverCaptureMovieMetadata;
```

## Properties

```
@property (Tq,R,N,V_uniqueID) uniqueID;
@property (TQ,N,V_userInitiatedCaptureTime) userInitiatedCaptureTime;
@property (T@"NSString",C,N) videoCodecType;
@property (T@"NSURL",C,N,V_movieFileURL) movieFileURL;
@property (T@"NSArray",C,N) movieMetadata;
@property (TB,N,GisAutoSpatialOverCaptureEnabled,V_autoSpatialOverCaptureEnabled) autoSpatialOverCaptureEnabled;
@property (T@"NSURL",C,N,V_spatialOverCaptureMovieFileURL) spatialOverCaptureMovieFileURL;
@property (T@"NSArray",C,N) spatialOverCaptureMovieMetadata;
```

## Class methods

```
+[AVMomentCaptureMovieRecordingSettings movieRecordingSettings];
+[AVMomentCaptureMovieRecordingSettings movieRecordingSettingsFromMomentCaptureSettings:];
```

## Instance methods

```
-[AVMomentCaptureMovieRecordingSettings debugDescription];
-[AVMomentCaptureMovieRecordingSettings dealloc];
-[AVMomentCaptureMovieRecordingSettings isAutoSpatialOverCaptureEnabled];
-[AVMomentCaptureMovieRecordingSettings uniqueID];
-[AVMomentCaptureMovieRecordingSettings description];
-[AVMomentCaptureMovieRecordingSettings copyWithZone:];
-[AVMomentCaptureMovieRecordingSettings spatialOverCaptureGroupIdentifier];
-[AVMomentCaptureMovieRecordingSettings setAutoSpatialOverCaptureEnabled:];
-[AVMomentCaptureMovieRecordingSettings userInitiatedCaptureTime];
-[AVMomentCaptureMovieRecordingSettings setVideoCodecType:];
-[AVMomentCaptureMovieRecordingSettings videoCodecType];
-[AVMomentCaptureMovieRecordingSettings _initFromMomentCaptureSettings:];
-[AVMomentCaptureMovieRecordingSettings spatialOverCaptureMovieMetadata];
-[AVMomentCaptureMovieRecordingSettings _sanitizedMovieMetadataArrayForMovieMetadataArray:exceptionReason:];
-[AVMomentCaptureMovieRecordingSettings movieFileURL];
-[AVMomentCaptureMovieRecordingSettings movieMetadata];
-[AVMomentCaptureMovieRecordingSettings setMovieFileURL:];
-[AVMomentCaptureMovieRecordingSettings setMovieMetadata:];
-[AVMomentCaptureMovieRecordingSettings setSpatialOverCaptureMovieFileURL:];
-[AVMomentCaptureMovieRecordingSettings setSpatialOverCaptureMovieMetadata:];
-[AVMomentCaptureMovieRecordingSettings setUserInitiatedCaptureTime:];
-[AVMomentCaptureMovieRecordingSettings spatialOverCaptureMovieFileURL];
```
