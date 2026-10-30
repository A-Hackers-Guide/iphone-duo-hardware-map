# `FigCaptureMovieFileRecordingSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureRecordingSettings`
- 33 instance variables, 32 properties, 70 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _videoSettings;
@"NSDictionary" _audioSettings;
@"NSDictionary" _cinematicAudioSettings;
B _videoMirrored;
i _videoRotationDegrees;
B _recordVideoOrientationAndMirroringChanges;
{?="value"q"timescale"i"flags"I"epoch"q} _movieFragmentInterval;
@"NSArray" _movieLevelMetadata;
B _sendPreviewIOSurface;
B _irisRecording;
B _debugMetadataSidecarFileEnabled;
B _videoDBGFileEnabled;
B _metadataIdentifiersEnabled;
{?="enabled"B"selectionBehavior"q"restrictedSelectionConditions"Q} _bravoCameraSelectionConfigurationForRecording;
B _irisMovieRecording;
@"NSURL" _spatialOverCaptureMovieURL;
@"NSArray" _spatialOverCaptureMovieLevelMetadata;
Q _movieStartTimeOverride;
B _personSegmentationRenderingEnabled;
@"NSData" _personSegmentationForegroundColorCube;
@"NSData" _personSegmentationBackgroundColorCube;
B _videoSTFEnabled;
B _usesVirtualCaptureCard;
@"FigCaptureSmartStyle" smartStyle;
B _smartStyleReversibilitySupported;
B _audioWasPlayingDuringCapture;
B _audioMixWithOthersEnabled;
i _timewarpMode;
B _smartStyleRenderingBypassed;
i _videoOrientation;
@"NSUUID" _videoDBGUUID;
@"FigCaptureSmartStyle" _smartStyle;
{?="u"(?="rational"{?="numerator"i"denominator"i}"floating"f)"tag"i} _maxFrameRate;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_videoSettings) videoSettings;
@property (T@"NSDictionary",C,N,V_audioSettings) audioSettings;
@property (T@"NSDictionary",C,N,V_cinematicAudioSettings) cinematicAudioSettings;
@property (TB,N,V_videoMirrored) videoMirrored;
@property (Ti,N,V_videoOrientation) videoOrientation;
@property (Ti,N,V_videoRotationDegrees) videoRotationDegrees;
@property (TB,N,V_recordVideoOrientationAndMirroringChanges) recordVideoOrientationAndMirroringChanges;
@property (T{?=(?={?=ii}f)i},N,V_maxFrameRate) maxFrameRate;
@property (T{?=qiIq},N,V_movieFragmentInterval) movieFragmentInterval;
@property (T@"NSArray",C,N,V_movieLevelMetadata) movieLevelMetadata;
@property (TB,N,V_sendPreviewIOSurface) sendPreviewIOSurface;
@property (TB,N,GisIrisRecording,V_irisRecording) irisRecording;
@property (TB,N,V_debugMetadataSidecarFileEnabled) debugMetadataSidecarFileEnabled;
@property (TB,N,V_videoDBGFileEnabled) videoDBGFileEnabled;
@property (T@"NSUUID",C,N,V_videoDBGUUID) videoDBGUUID;
@property (TB,N,V_metadataIdentifiersEnabled) metadataIdentifiersEnabled;
@property (T{?=BqQ},N,V_bravoCameraSelectionConfigurationForRecording) bravoCameraSelectionConfigurationForRecording;
@property (TB,N,GisIrisMovieRecording,V_irisMovieRecording) irisMovieRecording;
@property (T@"NSURL",C,N,V_spatialOverCaptureMovieURL) spatialOverCaptureMovieURL;
@property (T@"NSArray",C,N,V_spatialOverCaptureMovieLevelMetadata) spatialOverCaptureMovieLevelMetadata;
@property (TQ,N,V_movieStartTimeOverride) movieStartTimeOverride;
@property (TB,N,V_usesVirtualCaptureCard) usesVirtualCaptureCard;
@property (TB,N,V_personSegmentationRenderingEnabled) personSegmentationRenderingEnabled;
@property (T@"NSData",&,N,V_personSegmentationForegroundColorCube) personSegmentationForegroundColorCube;
@property (T@"NSData",&,N,V_personSegmentationBackgroundColorCube) personSegmentationBackgroundColorCube;
@property (TB,N,V_videoSTFEnabled) videoSTFEnabled;
@property (TB,N,V_smartStyleReversibilitySupported) smartStyleReversibilitySupported;
@property (T@"FigCaptureSmartStyle",C,N,V_smartStyle) smartStyle;
@property (TB,N,V_smartStyleRenderingBypassed) smartStyleRenderingBypassed;
@property (TB,N,V_audioWasPlayingDuringCapture) audioWasPlayingDuringCapture;
@property (TB,N,V_audioMixWithOthersEnabled) audioMixWithOthersEnabled;
@property (Ti,N,V_timewarpMode) timewarpMode;
```

## Class methods

```
+[FigCaptureMovieFileRecordingSettings supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureMovieFileRecordingSettings maxFrameRate];
-[FigCaptureMovieFileRecordingSettings videoSettings];
-[FigCaptureMovieFileRecordingSettings setMovieLevelMetadata:];
-[FigCaptureMovieFileRecordingSettings movieLevelMetadata];
-[FigCaptureMovieFileRecordingSettings setMovieFragmentInterval:];
-[FigCaptureMovieFileRecordingSettings videoSTFEnabled];
-[FigCaptureMovieFileRecordingSettings setAudioMixWithOthersEnabled:];
-[FigCaptureMovieFileRecordingSettings movieFragmentInterval];
-[FigCaptureMovieFileRecordingSettings usesVirtualCaptureCard];
-[FigCaptureMovieFileRecordingSettings setIrisMovieRecording:];
-[FigCaptureMovieFileRecordingSettings setUsesVirtualCaptureCard:];
-[FigCaptureMovieFileRecordingSettings setVideoRotationDegrees:];
-[FigCaptureMovieFileRecordingSettings setVideoMirrored:];
-[FigCaptureMovieFileRecordingSettings setRecordVideoOrientationAndMirroringChanges:];
-[FigCaptureMovieFileRecordingSettings init];
-[FigCaptureMovieFileRecordingSettings setDebugMetadataSidecarFileEnabled:];
-[FigCaptureMovieFileRecordingSettings smartStyle];
-[FigCaptureMovieFileRecordingSettings setMetadataIdentifiersEnabled:];
-[FigCaptureMovieFileRecordingSettings setMaxFrameRate:];
-[FigCaptureMovieFileRecordingSettings sendPreviewIOSurface];
-[FigCaptureMovieFileRecordingSettings setSmartStyle:];
-[FigCaptureMovieFileRecordingSettings setVideoDBGUUID:];
-[FigCaptureMovieFileRecordingSettings timewarpMode];
-[FigCaptureMovieFileRecordingSettings smartStyleRenderingBypassed];
-[FigCaptureMovieFileRecordingSettings dealloc];
-[FigCaptureMovieFileRecordingSettings audioMixWithOthersEnabled];
-[FigCaptureMovieFileRecordingSettings videoOrientation];
-[FigCaptureMovieFileRecordingSettings videoDBGUUID];
-[FigCaptureMovieFileRecordingSettings debugMetadataSidecarFileEnabled];
-[FigCaptureMovieFileRecordingSettings personSegmentationBackgroundColorCube];
-[FigCaptureMovieFileRecordingSettings setAudioWasPlayingDuringCapture:];
-[FigCaptureMovieFileRecordingSettings setVideoSTFEnabled:];
-[FigCaptureMovieFileRecordingSettings setBravoCameraSelectionConfigurationForRecording:];
-[FigCaptureMovieFileRecordingSettings spatialOverCaptureMovieLevelMetadata];
-[FigCaptureMovieFileRecordingSettings setSendPreviewIOSurface:];
-[FigCaptureMovieFileRecordingSettings setSmartStyleRenderingBypassed:];
-[FigCaptureMovieFileRecordingSettings smartStyleReversibilitySupported];
-[FigCaptureMovieFileRecordingSettings bravoCameraSelectionConfigurationForRecording];
-[FigCaptureMovieFileRecordingSettings isIrisRecording];
-[FigCaptureMovieFileRecordingSettings encodeWithCoder:];
-[FigCaptureMovieFileRecordingSettings spatialOverCaptureMovieURL];
-[FigCaptureMovieFileRecordingSettings movieStartTimeOverride];
-[FigCaptureMovieFileRecordingSettings setSpatialOverCaptureMovieLevelMetadata:];
-[FigCaptureMovieFileRecordingSettings setAudioSettings:];
-[FigCaptureMovieFileRecordingSettings audioWasPlayingDuringCapture];
-[FigCaptureMovieFileRecordingSettings description];
-[FigCaptureMovieFileRecordingSettings videoMirrored];
-[FigCaptureMovieFileRecordingSettings setVideoOrientation:];
-[FigCaptureMovieFileRecordingSettings isIrisMovieRecording];
-[FigCaptureMovieFileRecordingSettings initWithCoder:];
-[FigCaptureMovieFileRecordingSettings setIrisRecording:];
-[FigCaptureMovieFileRecordingSettings setSmartStyleReversibilitySupported:];
-[FigCaptureMovieFileRecordingSettings personSegmentationForegroundColorCube];
-[FigCaptureMovieFileRecordingSettings personSegmentationRenderingEnabled];
-[FigCaptureMovieFileRecordingSettings cinematicAudioSettings];
-[FigCaptureMovieFileRecordingSettings audioSettings];
-[FigCaptureMovieFileRecordingSettings videoRotationDegrees];
-[FigCaptureMovieFileRecordingSettings setPersonSegmentationRenderingEnabled:];
-[FigCaptureMovieFileRecordingSettings recordVideoOrientationAndMirroringChanges];
-[FigCaptureMovieFileRecordingSettings setVideoSettings:];
-[FigCaptureMovieFileRecordingSettings copyWithZone:];
-[FigCaptureMovieFileRecordingSettings setMovieStartTimeOverride:];
-[FigCaptureMovieFileRecordingSettings setVideoDBGFileEnabled:];
-[FigCaptureMovieFileRecordingSettings setPersonSegmentationBackgroundColorCube:];
-[FigCaptureMovieFileRecordingSettings metadataIdentifiersEnabled];
-[FigCaptureMovieFileRecordingSettings setPersonSegmentationForegroundColorCube:];
-[FigCaptureMovieFileRecordingSettings setSpatialOverCaptureMovieURL:];
-[FigCaptureMovieFileRecordingSettings setTimewarpMode:];
-[FigCaptureMovieFileRecordingSettings setCinematicAudioSettings:];
-[FigCaptureMovieFileRecordingSettings videoDBGFileEnabled];
```
