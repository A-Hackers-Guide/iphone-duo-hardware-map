# `TBNetwork` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `TBScorable`
- 0 instance variables, 20 properties, 21 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) remoteIdentifier;
@property (T@"NSString",R,N) SSID;
@property (TQ,R,N) authMask;
@property (T@"NSString",R,N) authDescription;
@property (T@"NSString",R,N) attributesDescription;
@property (T@"NSSet",R,N) accessPoints;
@property (T@"NSArray",R,N) ownerIdentifiers;
@property (TB,R,N,GisCaptive) captive;
@property (TB,R,N,GisMoving) moving;
@property (TB,R,N,GisSuspicious) suspicious;
@property (TB,R,N,GisPublic) public;
@property (TB,R,N,GisLowQuality) lowQuality;
@property (TB,R,N,GisLowUserPreference) lowUserPreference;
@property (TQ,R,N) type;
@property (TQ,R,N) venueGroup;
@property (TI,R,N) venueType;
@property (TQ,?,R,N) tileKey;
@property (TQ,?,R,N) accessPointCount;
@property (Td,?,R,N) centroidLat;
@property (Td,?,R,N) centroidLng;
```

## Instance methods

```
-[TBNetwork isPublic];
-[TBNetwork accessPoints];
-[TBNetwork venueGroup];
-[TBNetwork SSID];
-[TBNetwork isLowQuality];
-[TBNetwork venueType];
-[TBNetwork isMoving];
-[TBNetwork type];
-[TBNetwork isLowUserPreference];
-[TBNetwork isCaptive];
-[TBNetwork dictionaryRepresentation];
-[TBNetwork ownerIdentifiers];
-[TBNetwork remoteIdentifier];
-[TBNetwork authDescription];
-[TBNetwork attributesDescription];
-[TBNetwork authMask];
-[TBNetwork isSuspicious];
-[TBNetwork tileKey];
-[TBNetwork accessPointCount];
-[TBNetwork centroidLat];
-[TBNetwork centroidLng];
```
