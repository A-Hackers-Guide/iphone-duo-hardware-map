# `_NIWiFiRangingTestConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NIDiscoveryToken" _peerDiscoveryToken;
@"NSDictionary" _parameters;
@"NSArray" _monitoredRegions;
```

## Properties

```
@property (T@"NIDiscoveryToken",R,C,N,V_peerDiscoveryToken) peerDiscoveryToken;
@property (T@"NSDictionary",R,N,V_parameters) parameters;
@property (T@"NSArray",C,V_monitoredRegions) monitoredRegions;
```

## Class methods

```
+[_NIWiFiRangingTestConfiguration supportsSecureCoding];
```

## Instance methods

```
-[_NIWiFiRangingTestConfiguration parameters];
-[_NIWiFiRangingTestConfiguration monitoredRegions];
-[_NIWiFiRangingTestConfiguration descriptionInternal];
-[_NIWiFiRangingTestConfiguration encodeWithCoder:];
-[_NIWiFiRangingTestConfiguration hash];
-[_NIWiFiRangingTestConfiguration setMonitoredRegions:];
-[_NIWiFiRangingTestConfiguration description];
-[_NIWiFiRangingTestConfiguration initWithCoder:];
-[_NIWiFiRangingTestConfiguration copyWithZone:];
-[_NIWiFiRangingTestConfiguration isEqual:];
-[_NIWiFiRangingTestConfiguration initWithDiscoveryToken:wifiRangingParameters:regions:];
-[_NIWiFiRangingTestConfiguration peerDiscoveryToken];
```
