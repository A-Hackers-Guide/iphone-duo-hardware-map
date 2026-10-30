# `AVControlCenterCaptureDeviceWatcher`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureDeviceDiscoverySession" _discoverySession;
@? _handler;
B _centerStageSupported;
B _backgroundBlurSupported;
B _studioLightingSupported;
B _reactionEffectsSupported;
B _backgroundReplacementSupported;
B _micModesSupported;
```

## Properties

```
@property (TB,R) centerStageSupported;
@property (TB,R) backgroundBlurSupported;
@property (TB,R) studioLightingSupported;
@property (TB,R) reactionEffectsSupported;
@property (TB,R) backgroundReplacementSupported;
@property (TB,R,V_micModesSupported) micModesSupported;
```

## Instance methods

```
-[AVControlCenterCaptureDeviceWatcher reactionEffectsSupported];
-[AVControlCenterCaptureDeviceWatcher observeValueForKeyPath:ofObject:change:context:];
-[AVControlCenterCaptureDeviceWatcher dealloc];
-[AVControlCenterCaptureDeviceWatcher backgroundReplacementSupported];
-[AVControlCenterCaptureDeviceWatcher studioLightingSupported];
-[AVControlCenterCaptureDeviceWatcher backgroundBlurSupported];
-[AVControlCenterCaptureDeviceWatcher centerStageSupported];
-[AVControlCenterCaptureDeviceWatcher initWithSupportedVideoEffectsDidChangeHandler:];
-[AVControlCenterCaptureDeviceWatcher micModesSupported];
```
