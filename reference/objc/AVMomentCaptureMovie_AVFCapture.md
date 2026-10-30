# `AVMomentCaptureMovie`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"AVMomentCaptureMovieRecordingResolvedSettings" _resolvedSettings;
@"NSURL" _outputFileURL;
@"NSURL" _debugMetadataSidecarFileURL;
@"NSURL" _videoDBGFileURL;
^{__CVBuffer=} _previewPixelBuffer;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
@"NSArray" _movieMetadata;
@"NSString" _overCaptureGroupIdentifier;
B _hasOverCapture;
```

## Properties

```
@property (T@"AVMomentCaptureMovieRecordingResolvedSettings",R,N,V_resolvedSettings) resolvedSettings;
@property (T@"NSURL",R,N,V_outputFileURL) outputFileURL;
@property (T@"NSURL",R,N,V_debugMetadataSidecarFileURL) debugMetadataSidecarFileURL;
@property (T@"NSURL",R,N,V_videoDBGFileURL) videoDBGFileURL;
@property (T^{__CVBuffer=},R,N,V_previewPixelBuffer) previewPixelBuffer;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (T@"NSArray",R,N,V_movieMetadata) movieMetadata;
```

## Class methods

```
+[AVMomentCaptureMovie movieWithResolvedSettings:outputFileURL:movieMetadata:];
```

## Instance methods

```
-[AVMomentCaptureMovie debugDescription];
-[AVMomentCaptureMovie dealloc];
-[AVMomentCaptureMovie _setDuration:];
-[AVMomentCaptureMovie duration];
-[AVMomentCaptureMovie description];
-[AVMomentCaptureMovie resolvedSettings];
-[AVMomentCaptureMovie outputFileURL];
-[AVMomentCaptureMovie videoDBGFileURL];
-[AVMomentCaptureMovie _initWithResolvedSettings:outputFileURL:movieMetadata:];
-[AVMomentCaptureMovie _setDebugMetadataSidecarFileURL:];
-[AVMomentCaptureMovie _setPreviewPixelBuffer:];
-[AVMomentCaptureMovie _setVideoDBGFileURL:];
-[AVMomentCaptureMovie debugMetadataSidecarFileURL];
-[AVMomentCaptureMovie movieMetadata];
-[AVMomentCaptureMovie previewPixelBuffer];
```
