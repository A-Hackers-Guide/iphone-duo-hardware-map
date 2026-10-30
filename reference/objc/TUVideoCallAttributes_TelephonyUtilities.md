# `TUVideoCallAttributes`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _remoteCameraOrientation;
q _localVideoContextSlotIdentifier;
q _remoteVideoContextSlotIdentifier;
```

## Properties

```
@property (Tq,N,V_remoteCameraOrientation) remoteCameraOrientation;
@property (Tq,N,V_localVideoContextSlotIdentifier) localVideoContextSlotIdentifier;
@property (Tq,N,V_remoteVideoContextSlotIdentifier) remoteVideoContextSlotIdentifier;
```

## Class methods

```
+[TUVideoCallAttributes supportsSecureCoding];
```

## Instance methods

```
-[TUVideoCallAttributes setLocalVideoContextSlotIdentifier:];
-[TUVideoCallAttributes remoteCameraOrientation];
-[TUVideoCallAttributes remoteVideoContextSlotIdentifier];
-[TUVideoCallAttributes setRemoteVideoContextSlotIdentifier:];
-[TUVideoCallAttributes setRemoteCameraOrientation:];
-[TUVideoCallAttributes isEqualToVideoCallAttributes:];
-[TUVideoCallAttributes encodeWithCoder:];
-[TUVideoCallAttributes hash];
-[TUVideoCallAttributes description];
-[TUVideoCallAttributes initWithCoder:];
-[TUVideoCallAttributes isEqual:];
-[TUVideoCallAttributes localVideoContextSlotIdentifier];
```
