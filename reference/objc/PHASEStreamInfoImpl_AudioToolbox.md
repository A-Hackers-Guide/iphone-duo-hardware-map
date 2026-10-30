# `PHASEStreamInfoImpl`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PHASEStreamInfo`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
I _latencyInFrames;
@"AVAudioFormat" _format;
@"NSDictionary" _streamDescription;
```

## Properties

```
@property (T@"AVAudioFormat",R,N,V_format) format;
@property (TI,R,N,V_latencyInFrames) latencyInFrames;
@property (T@"NSDictionary",?,R,N,V_streamDescription) streamDescription;
```

## Instance methods

```
-[PHASEStreamInfoImpl streamDescription];
-[PHASEStreamInfoImpl format];
-[PHASEStreamInfoImpl initWithFormat:latencyInFrames:];
-[PHASEStreamInfoImpl latencyInFrames];
-[PHASEStreamInfoImpl initWithFormat:latencyInFrames:streamDescription:];
```
