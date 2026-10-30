# `FigAudioCaptureConnectionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureConnectionConfiguration`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _audioCaptureMode;
B _windNoiseRemovalEnabled;
B _audioZoomEnabled;
i _builtInMicrophonePosition;
d _builtInMicrophoneRequiredSampleRate;
I _spatialAudioChannelLayoutTag;
```

## Properties

```
@property (Ti,N,V_audioCaptureMode) audioCaptureMode;
@property (TB,N,V_windNoiseRemovalEnabled) windNoiseRemovalEnabled;
@property (TB,N,V_audioZoomEnabled) audioZoomEnabled;
@property (Ti,N,V_builtInMicrophonePosition) builtInMicrophonePosition;
@property (Td,N,V_builtInMicrophoneRequiredSampleRate) builtInMicrophoneRequiredSampleRate;
@property (TI,N,V_spatialAudioChannelLayoutTag) spatialAudioChannelLayoutTag;
```

## Instance methods

```
-[FigAudioCaptureConnectionConfiguration audioZoomEnabled];
-[FigAudioCaptureConnectionConfiguration windNoiseRemovalEnabled];
-[FigAudioCaptureConnectionConfiguration setAudioCaptureMode:];
-[FigAudioCaptureConnectionConfiguration setWindNoiseRemovalEnabled:];
-[FigAudioCaptureConnectionConfiguration reasonForNotEqualingConfiguration:];
-[FigAudioCaptureConnectionConfiguration spatialAudioChannelLayoutTag];
-[FigAudioCaptureConnectionConfiguration setAudioZoomEnabled:];
-[FigAudioCaptureConnectionConfiguration audioCaptureMode];
-[FigAudioCaptureConnectionConfiguration builtInMicrophonePosition];
-[FigAudioCaptureConnectionConfiguration copyXPCEncoding];
-[FigAudioCaptureConnectionConfiguration description];
-[FigAudioCaptureConnectionConfiguration setBuiltInMicrophoneRequiredSampleRate:];
-[FigAudioCaptureConnectionConfiguration initWithXPCEncoding:];
-[FigAudioCaptureConnectionConfiguration builtInMicrophoneRequiredSampleRate];
-[FigAudioCaptureConnectionConfiguration copyWithZone:];
-[FigAudioCaptureConnectionConfiguration isEqual:];
-[FigAudioCaptureConnectionConfiguration setBuiltInMicrophonePosition:];
-[FigAudioCaptureConnectionConfiguration setSpatialAudioChannelLayoutTag:];
```
