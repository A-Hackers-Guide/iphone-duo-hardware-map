# `TUNearbyDeviceHandleCapabilities`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _avLessCapable;
B _lagunaCapable;
B _audioCallCapable;
B _telephonyRelayCapable;
B _greenTea;
```

## Properties

```
@property (TB,R,N,GisAVLessCapable,V_avLessCapable) avLessCapable;
@property (TB,R,N,GisLagunaCapable,V_lagunaCapable) lagunaCapable;
@property (TB,R,N,GisAudioCallCapable,V_audioCallCapable) audioCallCapable;
@property (TB,R,N,GisTelephonyRelayCapable,V_telephonyRelayCapable) telephonyRelayCapable;
@property (TB,R,N,GisGreenTea,V_greenTea) greenTea;
```

## Class methods

```
+[TUNearbyDeviceHandleCapabilities supportsSecureCoding];
```

## Instance methods

```
-[TUNearbyDeviceHandleCapabilities isGreenTea];
-[TUNearbyDeviceHandleCapabilities encodeWithCoder:];
-[TUNearbyDeviceHandleCapabilities description];
-[TUNearbyDeviceHandleCapabilities initWithCoder:];
-[TUNearbyDeviceHandleCapabilities copyWithZone:];
-[TUNearbyDeviceHandleCapabilities isAVLessCapable];
-[TUNearbyDeviceHandleCapabilities isLagunaCapable];
-[TUNearbyDeviceHandleCapabilities initWithAVLessCapable:lagunaCapable:audioCallCapable:telephonyRelayCapable:greenTea:];
-[TUNearbyDeviceHandleCapabilities isAudioCallCapable];
-[TUNearbyDeviceHandleCapabilities isTelephonyRelayCapable];
```
