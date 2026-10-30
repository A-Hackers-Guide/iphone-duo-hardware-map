# `TBNetworkMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- Protocols: `TBNetwork`, `NSSecureCoding`, `NSCoding`
- 0 instance variables, 49 properties, 15 instance methods, 6 class methods

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
@property (TI,R,D,N) venueType;
@property (TQ,?,R,D,N) tileKey;
@property (TQ,?,R,N) accessPointCount;
@property (Td,?,R,N) centroidLat;
@property (Td,?,R,N) centroidLng;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TBScore>",R,N) popularityScore;
@property (T@"<TBScore>",R,N) qualityScore;
@property (Tq,R,D,N) accessPointCount;
@property (Tq,D,N) authMask;
@property (TB,D,N) captive;
@property (Td,D,N) centroidLat;
@property (Td,D,N) centroidLng;
@property (T@"NSDate",C,D,N) created;
@property (T@"NSString",C,D,N) identifier;
@property (TB,D,N) lowQuality;
@property (TB,D,N) lowUserPreference;
@property (TB,D,N) moving;
@property (T@"NSString",C,D,N) name;
@property (T@"NSArray",&,D,N) ownerIdentifiers;
@property (Ti,D,N) popularityScoreValue;
@property (TB,D,N) public;
@property (Ti,D,N) qualityScoreValue;
@property (TB,D,N) suspicious;
@property (Tq,R,D,N) tileKey;
@property (Tq,D,N) timestamp;
@property (Tq,D,N) type;
@property (Tq,D,N) venueGroup;
@property (Ti,D,N) venueType;
@property (T@"NSSet",&,D,N) accessPoints;
@property (T@"TBTileMO",&,D,N) tile;
```

## Class methods

```
+[TBNetworkMO supportsSecureCoding];
+[TBNetworkMO fetchRequest];
+[TBNetworkMO entityName];
+[TBNetworkMO generateNewNetworkObjectFromMOC:];
+[TBNetworkMO removeAllNetworksInMOC:];
+[TBNetworkMO removeNetworksUsingPredicate:moc:];
```

## Instance methods

```
-[TBNetworkMO isPublic];
-[TBNetworkMO SSID];
-[TBNetworkMO isLowQuality];
-[TBNetworkMO isMoving];
-[TBNetworkMO isLowUserPreference];
-[TBNetworkMO encodeWithCoder:];
-[TBNetworkMO isCaptive];
-[TBNetworkMO initWithCoder:];
-[TBNetworkMO qualityScore];
-[TBNetworkMO popularityScore];
-[TBNetworkMO dictionaryRepresentation];
-[TBNetworkMO remoteIdentifier];
-[TBNetworkMO authDescription];
-[TBNetworkMO attributesDescription];
-[TBNetworkMO isSuspicious];
```
