# `WiFiAvailabilitySource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@?,C,N) changeHandler;
@property (T@?,C,N) relevancyHandler;
@property (T@?,C,N) removalHandler;
```

## Instance methods

```
-[WiFiAvailabilitySource setChangeHandler:];
-[WiFiAvailabilitySource changeHandler];
-[WiFiAvailabilitySource relevancyHandler];
-[WiFiAvailabilitySource relevantNetworks];
-[WiFiAvailabilitySource removalHandler];
-[WiFiAvailabilitySource setRelevancyHandler:];
-[WiFiAvailabilitySource setRemovalHandler:];
-[WiFiAvailabilitySource candidateNetworks];
-[WiFiAvailabilitySource fetchCandidateNetworksMatchingBSSIDs:completionHandler:];
```
