# `CWFNetworkOfInterestManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWNetworkOfInterestManagerDelegate`, `HMHomeManagerDelegate`
- 12 instance variables, 6 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _noiQueue;
@"NSObject<OS_dispatch_semaphore>" _noiWaiter;
@"NWNetworkOfInterestManager" _noiManager;
@"HMHomeManager" _homeManager;
@"NSArray" _trackedHomeNetworks;
@"NSArray" _trackedWorkNetworks;
@"NSMutableSet" _homekitHomeNetworks;
@"NSMutableSet" _colocatedLANNetworks;
@"NSDate" _lastHomeKitWiFiFetchTimestamp;
@"NSObject<OS_dispatch_source>" _homeKitFetchTimer;
@? _homeNetworkDeterminationChangedHandler;
@? _workNetworkDeterminationChangedHandler;
```

## Properties

```
@property (T@?,C,V_homeNetworkDeterminationChangedHandler) homeNetworkDeterminationChangedHandler;
@property (T@?,C,V_workNetworkDeterminationChangedHandler) workNetworkDeterminationChangedHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CWFNetworkOfInterestManager sharedInstance];
+[CWFNetworkOfInterestManager testHomeNetworks];
```

## Instance methods

```
-[CWFNetworkOfInterestManager didStopTrackingNOI:];
-[CWFNetworkOfInterestManager didStopTrackingAllNOIs:];
-[CWFNetworkOfInterestManager didStartTrackingNOI:];
-[CWFNetworkOfInterestManager init];
-[CWFNetworkOfInterestManager workTypeForNetworkName:];
-[CWFNetworkOfInterestManager homeManagerDidUpdateHomes:];
-[CWFNetworkOfInterestManager _workNetworkDeterminationDidChange];
-[CWFNetworkOfInterestManager setHomeNetworkDeterminationChangedHandler:];
-[CWFNetworkOfInterestManager invalidate];
-[CWFNetworkOfInterestManager setColocatedLANNetworks:];
-[CWFNetworkOfInterestManager _homeNetworkDeterminationDidChange];
-[CWFNetworkOfInterestManager setWorkNetworkDeterminationChangedHandler:];
-[CWFNetworkOfInterestManager activate];
-[CWFNetworkOfInterestManager homeNetworkDeterminationChangedHandler];
-[CWFNetworkOfInterestManager workNetworkDeterminationChangedHandler];
-[CWFNetworkOfInterestManager workTypeForNetworkSignature:];
-[CWFNetworkOfInterestManager homeTypeForNetworkSignature:];
-[CWFNetworkOfInterestManager fetchHomeWiFiInfoFromHomeKit];
-[CWFNetworkOfInterestManager homeTypeForNetworkName:];
```
