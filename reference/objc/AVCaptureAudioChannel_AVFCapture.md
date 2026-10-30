# `AVCaptureAudioChannel`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureAudioChannelInternal" _internal;
B _enabled;
f _volume;
```

## Properties

```
@property (Tf,R,N) averagePowerLevel;
@property (Tf,R,N) peakHoldLevel;
@property (Tf,N,V_volume) volume;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Class methods

```
+[AVCaptureAudioChannel initialize];
```

## Instance methods

```
-[AVCaptureAudioChannel volume];
-[AVCaptureAudioChannel dealloc];
-[AVCaptureAudioChannel setVolume:];
-[AVCaptureAudioChannel initWithConnection:];
-[AVCaptureAudioChannel isEnabled];
-[AVCaptureAudioChannel invalidate];
-[AVCaptureAudioChannel setEnabled:];
-[AVCaptureAudioChannel averagePowerLevel];
-[AVCaptureAudioChannel peakHoldLevel];
```
