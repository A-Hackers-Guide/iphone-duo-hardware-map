# `FigCaptureAudioFileRecordingSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureRecordingSettings`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _audioSettings;
@"NSDictionary" _cinematicAudioSettings;
@"NSArray" _metadata;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_audioSettings) audioSettings;
@property (T@"NSDictionary",C,N,V_cinematicAudioSettings) cinematicAudioSettings;
@property (T@"NSArray",C,N,V_metadata) metadata;
```

## Class methods

```
+[FigCaptureAudioFileRecordingSettings supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureAudioFileRecordingSettings init];
-[FigCaptureAudioFileRecordingSettings dealloc];
-[FigCaptureAudioFileRecordingSettings metadata];
-[FigCaptureAudioFileRecordingSettings encodeWithCoder:];
-[FigCaptureAudioFileRecordingSettings setMetadata:];
-[FigCaptureAudioFileRecordingSettings setAudioSettings:];
-[FigCaptureAudioFileRecordingSettings description];
-[FigCaptureAudioFileRecordingSettings initWithCoder:];
-[FigCaptureAudioFileRecordingSettings cinematicAudioSettings];
-[FigCaptureAudioFileRecordingSettings audioSettings];
-[FigCaptureAudioFileRecordingSettings copyWithZone:];
-[FigCaptureAudioFileRecordingSettings setCinematicAudioSettings:];
```
