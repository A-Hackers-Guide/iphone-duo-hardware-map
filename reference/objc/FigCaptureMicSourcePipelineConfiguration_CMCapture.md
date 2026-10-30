# `FigCaptureMicSourcePipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureSourceConfiguration" _micConfiguration;
@"NSArray" _micConnectionConfigurations;
@"FigCaptureSourceConfiguration" _cameraConfigurationForStereoAudioCapture;
@"BWZoomCommandHandler" _zoomCommandHandlerForStereoAudioCapture;
B _flipStereoAudioCaptureChannels;
B _windNoiseRemovalEnabled;
@"NSString" _sessionPreset;
B _configuresAppAudioSession;
B _configuresAppAudioSessionToMixWithOthers;
B _configuresAppAudioSessionForBluetoothHighQualityRecording;
B _audioSourceNodeShouldCallEndInterruption;
Q _clientSDKVersionToken;
B _clientOSVersionSupportsDecoupledIO;
{?="val"[8I]} _clientAuditToken;
B _isAudioOnlyRecordingSession;
@"AVAudioFormat" _remoteIOOutputFormat;
Q clientSDKVersionToken;
```

## Instance methods

```
-[FigCaptureMicSourcePipelineConfiguration dealloc];
```
