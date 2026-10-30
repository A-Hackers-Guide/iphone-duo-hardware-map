# `ACCAudioManager`

- Image: [`/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio`](../userland/System__Library__PrivateFrameworks__AccessoryAudio.framework__AccessoryAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCAudioClientProtocol`
- 1 instance variables, 5 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"ACCAudioClient" _audioClient;
```

## Properties

```
@property (T@"ACCAudioClient",&,N,V_audioClient) audioClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ACCAudioManager sharedACCAudioManager];
```

## Instance methods

```
-[ACCAudioManager init];
-[ACCAudioManager setAudioClient:];
-[ACCAudioManager audioClient];
-[ACCAudioManager allowBackgroundAudioForClient:];
-[ACCAudioManager deviceAudioStates];
-[ACCAudioManager setDigitalAudioSampleRate:];
-[ACCAudioManager supportedDigitalAudioSampleRate:];
-[ACCAudioManager supportedDigitalAudioSampleRates];
```
