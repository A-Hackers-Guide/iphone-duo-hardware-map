# `_TtC14NearbySessions26NearbyAdvertisementRequest`

- Image: [`/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions`](../userland/System__Library__PrivateFrameworks__NearbySessions.framework__NearbySessions.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCoding`
- 4 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
Foundation.UUID identifier;
Foundation.Data invitation;
__C.CBNearbyInfoV2InvitationRouteType route;
NearbySessions.NearbyInvitationActivityType activityType;
```

## Properties

```
@property (T@"NSUUID",N,R) identifier;
@property (T@"NSData",N,R) invitation;
@property (TC,N,R,Vroute) route;
@property (TI,N,R,VactivityType) activityType;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[_TtC14NearbySessions26NearbyAdvertisementRequest supportsSecureCoding];
```

## Instance methods

```
-[_TtC14NearbySessions26NearbyAdvertisementRequest route];
-[_TtC14NearbySessions26NearbyAdvertisementRequest identifier];
-[_TtC14NearbySessions26NearbyAdvertisementRequest init];
-[_TtC14NearbySessions26NearbyAdvertisementRequest activityType];
-[_TtC14NearbySessions26NearbyAdvertisementRequest encodeWithCoder:];
-[_TtC14NearbySessions26NearbyAdvertisementRequest invitation];
-[_TtC14NearbySessions26NearbyAdvertisementRequest description];
-[_TtC14NearbySessions26NearbyAdvertisementRequest initWithCoder:];
-[_TtC14NearbySessions26NearbyAdvertisementRequest initWithIdentifier:invitation:route:activityType:];
```
