# `WFMeasure`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 67 instance methods, 1 class methods

## Instance variables

```
B _isInProgress;
B _isPeriodicTest;
B _isSiriTimeout;
B _isApsdTimeout;
B _isRetest;
i _tclass;
@"NSString" _gatewayAddress;
@"NSMutableSet" _dnsServers;
Q _options;
@"NSObject<OS_dispatch_group>" _dispatchGroup;
@? _completionHandler;
@"NSObject<OS_dispatch_queue>" _completionQueue;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSString" _interfaceName;
@"NSString" _publicDNSAddress;
@"NSString" _testDNSHostname;
@"NSString" _testReason;
@"NPTPerformanceTest" _performanceTest;
@"WFMeasureResult" _result;
```

## Properties

```
@property (TB,N,V_isInProgress) isInProgress;
@property (TQ,N,V_options) options;
@property (T@"NSObject<OS_dispatch_group>",&,N,V_dispatchGroup) dispatchGroup;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_completionQueue) completionQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (T@"NSString",&,N,V_interfaceName) interfaceName;
@property (T@"NSString",&,N,V_gatewayAddress) gatewayAddress;
@property (T@"NSMutableSet",&,N,V_dnsServers) dnsServers;
@property (T@"NSString",&,N,V_publicDNSAddress) publicDNSAddress;
@property (T@"NSString",&,N,V_testDNSHostname) testDNSHostname;
@property (T@"NSString",&,N,V_testReason) testReason;
@property (TB,N,V_isPeriodicTest) isPeriodicTest;
@property (TB,N,V_isSiriTimeout) isSiriTimeout;
@property (TB,N,V_isApsdTimeout) isApsdTimeout;
@property (TB,N,V_isRetest) isRetest;
@property (Ti,N,V_tclass) tclass;
@property (T@"NPTPerformanceTest",&,N,V_performanceTest) performanceTest;
@property (T@"WFMeasureResult",&,N,V_result) result;
```

## Class methods

```
+[WFMeasure supportsLinkRecoveryTests];
```

## Instance methods

```
-[WFMeasure setIsPeriodicTest:];
-[WFMeasure setResult:];
-[WFMeasure tclass];
-[WFMeasure getLazyNSStringPreference:exists:];
-[WFMeasure shouldApsdSampleSiriTCP];
-[WFMeasure start:withCompletionQueue:];
-[WFMeasure setCompletionHandler:];
-[WFMeasure dispatchSiriTest:trafficClass:];
-[WFMeasure setOptions:];
-[WFMeasure completionHandler];
-[WFMeasure setDnsServers:];
-[WFMeasure setPublicDNSAddress:];
-[WFMeasure getPeriodicSampleTrafficClass];
-[WFMeasure completionQueue];
-[WFMeasure abort];
-[WFMeasure initializePerformanceTest];
-[WFMeasure getApsdSampleTrafficClass];
-[WFMeasure setInterfaceName:];
-[WFMeasure isInProgress];
-[WFMeasure performanceTest];
-[WFMeasure testReason];
-[WFMeasure interfaceName];
-[WFMeasure retrieveNetworkConfigurations];
-[WFMeasure shouldTimeoutSampleSiriTCP];
-[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:];
-[WFMeasure shouldTimeoutSampleSiriTLS];
-[WFMeasure shouldPeriodicSampleSiriTLS];
-[WFMeasure isSiriTimeout];
-[WFMeasure isRetest];
-[WFMeasure setTestReason:];
-[WFMeasure gatewayAddress];
-[WFMeasure shouldPeriodicSampleSiriTCP];
-[WFMeasure incrementTrafficClassSucceeded:size:count:];
-[WFMeasure result];
-[WFMeasure publicDNSAddress];
-[WFMeasure setTclass:];
-[WFMeasure setCompletionQueue:];
-[WFMeasure getLazyNSNumberPreference:exists:];
-[WFMeasure dispatchPingTest:];
-[WFMeasure description];
-[WFMeasure setDispatchGroup:];
-[WFMeasure getTimeoutSampleTrafficClass];
-[WFMeasure setIsInProgress:];
-[WFMeasure setGatewayAddress:];
-[WFMeasure testDNSHostname];
-[WFMeasure doPing:count:timeout:size:class:minRTT:maxRTT:successCount:];
-[WFMeasure options];
-[WFMeasure doDNSResolution:timeout:];
-[WFMeasure initWithType:andReason:prevTestedOptions:prevTestedTrafficClass:andInterfaceName:];
-[WFMeasure dnsServers];
-[WFMeasure dispatchDNSTest:];
-[WFMeasure setInternalQueue:];
-[WFMeasure isApsdTimeout];
-[WFMeasure shouldApsdSampleSiriTLS];
-[WFMeasure setPerformanceTest:];
-[WFMeasure doThroughputTest];
-[WFMeasure setIsApsdTimeout:];
-[WFMeasure setIsRetest:];
-[WFMeasure dispatchGroup];
-[WFMeasure doULThroughputTest];
-[WFMeasure internalQueue];
-[WFMeasure setIsSiriTimeout:];
-[WFMeasure dispatchThroughputTest];
-[WFMeasure incrementTrafficClassAttempted:size:count:];
-[WFMeasure isPeriodicTest];
-[WFMeasure dispatchULThroughputTest];
-[WFMeasure setTestDNSHostname:];
```
