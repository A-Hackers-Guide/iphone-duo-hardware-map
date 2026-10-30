# `SNNetworkManager`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SNNetworkManagerObserverInternal`
- 3 instance variables, 8 properties, 23 instance methods, 3 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _queue;
@"SNNetworkManagerInternal" _underlyingNetworkManager;
```

## Properties

```
@property (T@"SNNetworkManagerInternal",&,N,V_underlyingNetworkManager) underlyingNetworkManager;
@property (T@"NSNumber",R,N) lastSignalStrength;
@property (T@"NSString",R,N) carrierName;
@property (T@"CTSignalStrengthMeasurements",R,N) signalStrengthMeasurements;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SNNetworkManager sharedInstance];
+[SNNetworkManager acquireDormancySuspendAssertion:];
+[SNNetworkManager releaseDormancySuspendAssertion:];
```

## Instance methods

```
-[SNNetworkManager carrierName];
-[SNNetworkManager releaseWiFiAssertion];
-[SNNetworkManager registerClient];
-[SNNetworkManager removeObserver:];
-[SNNetworkManager updateNetworkPerformanceFeed];
-[SNNetworkManager resetLinkRecommendationInfo];
-[SNNetworkManager forceFastDormancy];
-[SNNetworkManager _init];
-[SNNetworkManager addObserver:];
-[SNNetworkManager stopMonitoringNetwork];
-[SNNetworkManager signalStrengthMeasurements];
-[SNNetworkManager lastSignalStrength];
-[SNNetworkManager unregisterClient];
-[SNNetworkManager acquireWiFiAssertion:];
-[SNNetworkManager getLinkRecommendation:recommendation:];
-[SNNetworkManager networkManagerLostNonWWANConnectivity:];
-[SNNetworkManager networkManagerNonWWANDidBecomeAvailable:];
-[SNNetworkManager startMonitoringNetworkForHost:];
-[SNNetworkManager networkQuality:];
-[SNNetworkManager getLinkRecommendationMetrics:];
-[SNNetworkManager networkManagerNetworkUnreachable:];
-[SNNetworkManager setUnderlyingNetworkManager:];
-[SNNetworkManager underlyingNetworkManager];
```
