# `WiFiAvailabilityNearbySource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAvailabilitySource`
- 4 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSArray" recommendedNetworks;
@? changeHandler;
@? relevancyHandler;
@? removalHandler;
```

## Properties

```
@property (T@"NSArray",C,VrecommendedNetworks) recommendedNetworks;
@property (T@?,C,N,VchangeHandler) changeHandler;
@property (T@?,C,N,VrelevancyHandler) relevancyHandler;
@property (T@?,C,N,VremovalHandler) removalHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAvailabilityNearbySource setChangeHandler:];
-[WiFiAvailabilityNearbySource changeHandler];
-[WiFiAvailabilityNearbySource recommendedNetworks];
-[WiFiAvailabilityNearbySource relevancyHandler];
-[WiFiAvailabilityNearbySource relevantNetworks];
-[WiFiAvailabilityNearbySource removalHandler];
-[WiFiAvailabilityNearbySource setRecommendedNetworks:];
-[WiFiAvailabilityNearbySource setRelevancyHandler:];
-[WiFiAvailabilityNearbySource setRemovalHandler:];
```
