# `WCAFetchWiFiBehaviorParameters`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _internalSSIDs;
@"NSDictionary" _disabledMacRandomizationVersions;
@"NSDictionary" _softErrors;
@"NSDictionary" _datapathTelemetry;
@"NSDictionary" _jtrnDefaults;
@"NSArray" _ambiguousSSIDs;
@"NSDictionary" _apProfile;
@"NSDictionary" _beaconParsing;
@"NSDictionary" _lqmDistribution;
```

## Properties

```
@property (T@"NSArray",&,N,V_internalSSIDs) internalSSIDs;
@property (T@"NSDictionary",&,N,V_disabledMacRandomizationVersions) disabledMacRandomizationVersions;
@property (T@"NSDictionary",&,N,V_softErrors) softErrors;
@property (T@"NSDictionary",&,N,V_datapathTelemetry) datapathTelemetry;
@property (T@"NSDictionary",&,N,V_jtrnDefaults) jtrnDefaults;
@property (T@"NSArray",&,N,V_ambiguousSSIDs) ambiguousSSIDs;
@property (T@"NSDictionary",&,N,V_apProfile) apProfile;
@property (T@"NSDictionary",&,N,V_beaconParsing) beaconParsing;
@property (T@"NSDictionary",&,N,V_lqmDistribution) lqmDistribution;
```

## Class methods

```
+[WCAFetchWiFiBehaviorParameters fetchWiFiBehaviorWithCompletion:];
```

## Instance methods

```
-[WCAFetchWiFiBehaviorParameters setApProfile:];
-[WCAFetchWiFiBehaviorParameters apProfile];
-[WCAFetchWiFiBehaviorParameters lqmDistribution];
-[WCAFetchWiFiBehaviorParameters ambiguousSSIDs];
-[WCAFetchWiFiBehaviorParameters beaconParsing];
-[WCAFetchWiFiBehaviorParameters datapathTelemetry];
-[WCAFetchWiFiBehaviorParameters disabledMacRandomizationVersions];
-[WCAFetchWiFiBehaviorParameters internalSSIDs];
-[WCAFetchWiFiBehaviorParameters jtrnDefaults];
-[WCAFetchWiFiBehaviorParameters setAmbiguousSSIDs:];
-[WCAFetchWiFiBehaviorParameters setBeaconParsing:];
-[WCAFetchWiFiBehaviorParameters setDatapathTelemetry:];
-[WCAFetchWiFiBehaviorParameters setDisabledMacRandomizationVersions:];
-[WCAFetchWiFiBehaviorParameters setInternalSSIDs:];
-[WCAFetchWiFiBehaviorParameters setJtrnDefaults:];
-[WCAFetchWiFiBehaviorParameters setLqmDistribution:];
-[WCAFetchWiFiBehaviorParameters setSoftErrors:];
-[WCAFetchWiFiBehaviorParameters softErrors];
```
