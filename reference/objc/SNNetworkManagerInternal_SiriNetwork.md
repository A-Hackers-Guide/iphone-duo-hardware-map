# `SNNetworkManagerInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientCarrierBundleDelegate`, `CoreTelephonyClientCellularUsagePolicyDelegate`, `CoreTelephonyClientDataDelegate`, `CoreTelephonyClientSubscriberDelegate`, `CoreTelephonyClientRegistrationDelegate`
- 28 instance variables, 3 properties, 30 instance methods, 3 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lock;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 observers;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 coreTelephonyClient;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 dataServiceDescriptor;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastDataSubscriptionSlot;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 subscriptionSlotOneStatus;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 subscriptionSlotTwoStatus;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastSuccessfulSymptomsFetch;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastFetchInProgress;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastSignalStrengthValue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 signalStrengthMeasurementsUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 subscriptionCount;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 carrierNameUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastCellularRATUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 currentRegistrationStatusUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastCellularLQMUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastIntelligentConnectivityEnabledUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastPrimaryNetworkInterfaceUnlocked;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 primaryInterfaceEvaluator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pathEvaluator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pathStatus;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pathUsesCellular;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 queue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkWiFiManager;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkWirelessCoexManager;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastTimeSymptomsFetch;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionQualityReport;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lockConnectionQuality;
```

## Properties

```
@property (T@"NSNumber",N,&) lastSignalStrength;
@property (T@"CTSignalStrengthMeasurements",N,&) signalStrengthMeasurements;
@property (T@"NSString",N,C) carrierName;
```

## Class methods

```
+[SNNetworkManagerInternal shared];
+[SNNetworkManagerInternal acquireDormancySuspendAssertion:];
+[SNNetworkManagerInternal releaseDormancySuspendAssertion:];
```

## Instance methods

```
-[SNNetworkManagerInternal signalStrengthChanged:info:];
-[SNNetworkManagerInternal cellMonitorUpdate:info:];
-[SNNetworkManagerInternal carrierBundleChange:];
-[SNNetworkManagerInternal intelligentConnectivityChanged:];
-[SNNetworkManagerInternal simStatusDidChange:status:];
-[SNNetworkManagerInternal preferredDataSimChanged:];
-[SNNetworkManagerInternal carrierName];
-[SNNetworkManagerInternal setCarrierName:];
-[SNNetworkManagerInternal releaseWiFiAssertion];
-[SNNetworkManagerInternal registerClient];
-[SNNetworkManagerInternal removeObserver:];
-[SNNetworkManagerInternal init];
-[SNNetworkManagerInternal setSignalStrengthMeasurements:];
-[SNNetworkManagerInternal updateNetworkPerformanceFeed];
-[SNNetworkManagerInternal dealloc];
-[SNNetworkManagerInternal acquireWiFiAssertionWithWifiAssertionTypeRawValue:];
-[SNNetworkManagerInternal resetLinkRecommendationInfo];
-[SNNetworkManagerInternal forceFastDormancy];
-[SNNetworkManagerInternal networkQualityWithNetworkType:];
-[SNNetworkManagerInternal addObserver:];
-[SNNetworkManagerInternal setLastSignalStrength:];
-[SNNetworkManagerInternal enhancedDataLinkQualityChanged:metric:];
-[SNNetworkManagerInternal getSNLinkRecommendationMetrics:];
-[SNNetworkManagerInternal stopMonitoringNetwork];
-[SNNetworkManagerInternal startMonitoringNetwork:];
-[SNNetworkManagerInternal signalStrengthMeasurements];
-[SNNetworkManagerInternal lastSignalStrength];
-[SNNetworkManagerInternal unregisterClient];
-[SNNetworkManagerInternal getSNProximityLinkRecommendationWithRetry:completion:];
-[SNNetworkManagerInternal displayStatusChanged:status:];
```
