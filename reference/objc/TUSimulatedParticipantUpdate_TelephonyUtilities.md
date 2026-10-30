# `TUSimulatedParticipantUpdate`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _spatialPersonaEnabled;
B _videoEnabled;
{TUSimulatedParticipantUpdateHasSet="spatialPersonaEnabled"b1"videoEnabled"b1} _hasSet;
```

## Properties

```
@property (T{TUSimulatedParticipantUpdateHasSet=b1b1},R,N,V_hasSet) hasSet;
@property (TB,N,GisSpatialPersonaEnabled,V_spatialPersonaEnabled) spatialPersonaEnabled;
@property (TB,N,GisVideoEnabled,V_videoEnabled) videoEnabled;
```

## Class methods

```
+[TUSimulatedParticipantUpdate supportsSecureCoding];
```

## Instance methods

```
-[TUSimulatedParticipantUpdate isVideoEnabled];
-[TUSimulatedParticipantUpdate setSpatialPersonaEnabled:];
-[TUSimulatedParticipantUpdate setVideoEnabled:];
-[TUSimulatedParticipantUpdate init];
-[TUSimulatedParticipantUpdate encodeWithCoder:];
-[TUSimulatedParticipantUpdate description];
-[TUSimulatedParticipantUpdate initWithCoder:];
-[TUSimulatedParticipantUpdate copyWithZone:];
-[TUSimulatedParticipantUpdate isSpatialPersonaEnabled];
-[TUSimulatedParticipantUpdate hasSet];
```
