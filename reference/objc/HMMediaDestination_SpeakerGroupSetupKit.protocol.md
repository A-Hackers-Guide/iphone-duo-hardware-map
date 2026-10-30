# `HMMediaDestination` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpeakerGroupSetupKit.framework/SpeakerGroupSetupKit`](../userland/System__Library__PrivateFrameworks__SpeakerGroupSetupKit.framework__SpeakerGroupSetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C) audioDestinationIdentifier;
@property (T@"NSString",R,C) unconfiguredDestinationIdentifier;
@property (T@"NSString",R,C) audioDestinationName;
@property (Tq,R) audioDestinationType;
@property (TB,R) supportsAudioDestination;
@property (TB,R) supportsSurroundSystemFrontRole;
@property (TB,R) supportsSurroundSystemRearRole;
```

## Instance methods

```
-[HMMediaDestination audioDestinationIdentifier];
-[HMMediaDestination audioDestinationName];
-[HMMediaDestination supportsSurroundSystemFrontRole];
-[HMMediaDestination audioDestinationType];
-[HMMediaDestination supportsAudioDestination];
-[HMMediaDestination supportsSurroundSystemRearRole];
-[HMMediaDestination unconfiguredDestinationIdentifier];
```
