# `AVAudioSessionRouteDescription`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSString",R) siriRemoteInputIdentifier;
@property (TQ,R) siriInputSource;
@property (TB,R) supportsSoftwareVolume;
@property (TB,R) supportsDoAP;
@property (T@"NSArray",R,N) inputs;
@property (T@"NSArray",R,N) outputs;
```

## Instance methods

```
-[AVAudioSessionRouteDescription outputs];
-[AVAudioSessionRouteDescription isEqualToRoute:];
-[AVAudioSessionRouteDescription supportsDoAP];
-[AVAudioSessionRouteDescription initWithRawDescription:owningSession:];
-[AVAudioSessionRouteDescription init];
-[AVAudioSessionRouteDescription inputs];
-[AVAudioSessionRouteDescription siriInputSource];
-[AVAudioSessionRouteDescription dealloc];
-[AVAudioSessionRouteDescription updateOutputPortsWithSpatialAudioStatus:];
-[AVAudioSessionRouteDescription siriRemoteInputIdentifier];
-[AVAudioSessionRouteDescription supportsSoftwareVolume];
-[AVAudioSessionRouteDescription hash];
-[AVAudioSessionRouteDescription description];
-[AVAudioSessionRouteDescription privateGetImplementation];
-[AVAudioSessionRouteDescription isEqual:];
```
