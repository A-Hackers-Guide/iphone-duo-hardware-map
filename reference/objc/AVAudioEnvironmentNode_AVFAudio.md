# `AVAudioEnvironmentNode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioNode`
- Protocols: `AVAudioMixing`
- 0 instance variables, 15 properties, 17 instance methods, 0 class methods

## Properties

```
@property (Tq,N) outputType;
@property (Tf,N) outputVolume;
@property (TQ,R,N) nextAvailableInputBus;
@property (T{AVAudio3DPoint=fff},N) listenerPosition;
@property (T{AVAudio3DVectorOrientation={AVAudio3DPoint=fff}{AVAudio3DPoint=fff}},N) listenerVectorOrientation;
@property (T{AVAudio3DAngularOrientation=fff},N) listenerAngularOrientation;
@property (T@"AVAudioEnvironmentDistanceAttenuationParameters",R,N) distanceAttenuationParameters;
@property (T@"AVAudioEnvironmentReverbParameters",R,N) reverbParameters;
@property (T@"NSArray",R,N) applicableRenderingAlgorithms;
@property (TB,N,GisListenerHeadTrackingEnabled) listenerHeadTrackingEnabled;
@property (Tf,D,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioEnvironmentNode init];
-[AVAudioEnvironmentNode outputType];
-[AVAudioEnvironmentNode setOutputType:];
-[AVAudioEnvironmentNode outputVolume];
-[AVAudioEnvironmentNode setOutputVolume:];
-[AVAudioEnvironmentNode setListenerPosition:];
-[AVAudioEnvironmentNode setListenerVectorOrientation:];
-[AVAudioEnvironmentNode setListenerHeadTrackingEnabled:];
-[AVAudioEnvironmentNode applicableRenderingAlgorithms];
-[AVAudioEnvironmentNode distanceAttenuationParameters];
-[AVAudioEnvironmentNode isListenerHeadTrackingEnabled];
-[AVAudioEnvironmentNode listenerAngularOrientation];
-[AVAudioEnvironmentNode listenerPosition];
-[AVAudioEnvironmentNode listenerVectorOrientation];
-[AVAudioEnvironmentNode nextAvailableInputBus];
-[AVAudioEnvironmentNode reverbParameters];
-[AVAudioEnvironmentNode setListenerAngularOrientation:];
```
