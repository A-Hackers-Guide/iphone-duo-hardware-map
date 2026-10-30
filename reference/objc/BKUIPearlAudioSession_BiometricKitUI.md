# `BKUIPearlAudioSession`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"AVAudioEngine" _audioEngine;
@"AVAudioPlayerNode" _audioNode;
@"AVAudioPCMBuffer" _lockSoundBuffer;
@"AVAudioPCMBuffer" _scanSoundBuffer;
@"AVAudioPCMBuffer" _completeSoundBuffer;
@"AVAudioPCMBuffer" _endSoundBuffer;
@"AVAudioPCMBuffer" _failSoundBuffer;
@"NSObject<OS_dispatch_queue>" _avPlayerNodeOperationQueue;
B _mediaServicesConnected;
```

## Properties

```
@property (T@"AVAudioEngine",R,N,V_audioEngine) audioEngine;
@property (T@"AVAudioPCMBuffer",R,N,V_lockSoundBuffer) lockSoundBuffer;
@property (T@"AVAudioPCMBuffer",R,N,V_scanSoundBuffer) scanSoundBuffer;
@property (T@"AVAudioPCMBuffer",R,N,V_completeSoundBuffer) completeSoundBuffer;
@property (T@"AVAudioPCMBuffer",R,N,V_endSoundBuffer) endSoundBuffer;
@property (T@"AVAudioPCMBuffer",R,N,V_failSoundBuffer) failSoundBuffer;
```

## Class methods

```
+[BKUIPearlAudioSession _loadSound:];
```

## Instance methods

```
-[BKUIPearlAudioSession play];
-[BKUIPearlAudioSession init];
-[BKUIPearlAudioSession stop];
-[BKUIPearlAudioSession dealloc];
-[BKUIPearlAudioSession audioEngine];
-[BKUIPearlAudioSession scheduleBuffer:atTime:options:completionHandler:];
-[BKUIPearlAudioSession scheduleBuffer:completionHandler:];
-[BKUIPearlAudioSession lockSoundBuffer];
-[BKUIPearlAudioSession scanSoundBuffer];
-[BKUIPearlAudioSession failSoundBuffer];
-[BKUIPearlAudioSession _mediaServicesConnectionWasLost:];
-[BKUIPearlAudioSession _mediaServicesReconnect:];
-[BKUIPearlAudioSession _setupMediaStack];
-[BKUIPearlAudioSession completeSoundBuffer];
-[BKUIPearlAudioSession endSoundBuffer];
```
