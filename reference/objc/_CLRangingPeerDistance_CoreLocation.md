# `_CLRangingPeerDistance`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 7 properties, 17 instance methods, 1 class methods

## Instance variables

```
@ _internal;
B _initiator;
```

## Properties

```
@property (T@"_CLRangingPeer",R,C,N) peer;
@property (T@"NSDate",R,C,N) timestamp;
@property (T@"NSDate",R,C,N) date;
@property (T@"NSNumber",R,C,N) distanceMeters;
@property (T@"NSNumber",R,C,N) accuracyMeters;
@property (TB,R,N,GisInitiator,V_initiator) initiator;
@property (TB,R,N) shouldUnlock;
```

## Class methods

```
+[_CLRangingPeerDistance supportsSecureCoding];
```

## Instance methods

```
-[_CLRangingPeerDistance isInitiator];
-[_CLRangingPeerDistance initiator];
-[_CLRangingPeerDistance init];
-[_CLRangingPeerDistance dealloc];
-[_CLRangingPeerDistance timestamp];
-[_CLRangingPeerDistance date];
-[_CLRangingPeerDistance encodeWithCoder:];
-[_CLRangingPeerDistance peer];
-[_CLRangingPeerDistance description];
-[_CLRangingPeerDistance initWithCoder:];
-[_CLRangingPeerDistance copyWithZone:];
-[_CLRangingPeerDistance distanceMeters];
-[_CLRangingPeerDistance initWithPeer:timestamp:distanceMeters:accuracyMeters:initiator:];
-[_CLRangingPeerDistance accuracyMeters];
-[_CLRangingPeerDistance initWithPeer:date:distanceMeters:accuracyMeters:initiator:];
-[_CLRangingPeerDistance initWithPeer:date:distanceMeters:accuracyMeters:initiator:shouldUnlock:];
-[_CLRangingPeerDistance shouldUnlock];
```
