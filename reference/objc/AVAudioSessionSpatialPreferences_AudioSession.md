# `AVAudioSessionSpatialPreferences`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
B prefersHeadTrackedSpatialization;
B prefersLossyAudioSources;
B alwaysSpatialize;
q maximumSpatializableChannels;
@"NSArray" spatialAudioSources;
```

## Properties

```
@property (TB,N,VprefersHeadTrackedSpatialization) prefersHeadTrackedSpatialization;
@property (TB,N,VprefersLossyAudioSources) prefersLossyAudioSources;
@property (TB,N,ValwaysSpatialize) alwaysSpatialize;
@property (Tq,N,VmaximumSpatializableChannels) maximumSpatializableChannels;
@property (T@"NSArray",&,N,VspatialAudioSources) spatialAudioSources;
```

## Class methods

```
+[AVAudioSessionSpatialPreferences supportsSecureCoding];
```

## Instance methods

```
-[AVAudioSessionSpatialPreferences setPrefersLossyAudioSources:];
-[AVAudioSessionSpatialPreferences setPrefersHeadTrackedSpatialization:];
-[AVAudioSessionSpatialPreferences prefersHeadTrackedSpatialization];
-[AVAudioSessionSpatialPreferences setSpatialAudioSources:];
-[AVAudioSessionSpatialPreferences alwaysSpatialize];
-[AVAudioSessionSpatialPreferences spatialAudioSources];
-[AVAudioSessionSpatialPreferences prefersLossyAudioSources];
-[AVAudioSessionSpatialPreferences encodeWithCoder:];
-[AVAudioSessionSpatialPreferences setAlwaysSpatialize:];
-[AVAudioSessionSpatialPreferences maximumSpatializableChannels];
-[AVAudioSessionSpatialPreferences initWithCoder:];
-[AVAudioSessionSpatialPreferences setMaximumSpatializableChannels:];
```
