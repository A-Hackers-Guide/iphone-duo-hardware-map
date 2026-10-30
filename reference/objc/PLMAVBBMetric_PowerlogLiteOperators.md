# `PLMAVBBMetric`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"PLAgent" _logAgent;
@"NSString" _notifyTitle;
@"NSNumber" _aPeriodicTriggerCnt;
@"NSNumber" _aPeriodicProfileId;
@"NSData" _aPeriodicTriggerPayload;
@"NSMutableDictionary" _prodMetrics;
@"PLMAVBBHardwareMessage" _storeMetricsLogger;
```

## Properties

```
@property (T@"NSString",&,V_notifyTitle) notifyTitle;
@property (T@"NSNumber",&,V_aPeriodicTriggerCnt) aPeriodicTriggerCnt;
@property (T@"NSNumber",&,V_aPeriodicProfileId) aPeriodicProfileId;
@property (T@"NSData",&,V_aPeriodicTriggerPayload) aPeriodicTriggerPayload;
@property (T@"NSMutableDictionary",&,V_prodMetrics) prodMetrics;
@property (T@"PLMAVBBHardwareMessage",&,V_storeMetricsLogger) storeMetricsLogger;
@property (T@"PLAgent",&,V_logAgent) logAgent;
```

## Class methods

```
+[PLMAVBBMetric sharedInstance];
```

## Instance methods

```
-[PLMAVBBMetric setProdMetrics:];
-[PLMAVBBMetric setNotifyTitle:];
-[PLMAVBBMetric aPeriodicProfileId];
-[PLMAVBBMetric aPeriodicTriggerCnt];
-[PLMAVBBMetric aPeriodicTriggerPayload];
-[PLMAVBBMetric flushPeriodicMetrics];
-[PLMAVBBMetric initializeDataStoreBBTS:triggerCnt:triggerId:];
-[PLMAVBBMetric initializeMetricsDictWithTS:triggerCnt:triggerId:];
-[PLMAVBBMetric logAgent];
-[PLMAVBBMetric modelProdMetricsNotify];
-[PLMAVBBMetric notifyTitle];
-[PLMAVBBMetric prodMetrics];
-[PLMAVBBMetric queueAperiodicMetricId:payload:profileId:];
-[PLMAVBBMetric queuePeriodicMetricId:payload:forTrigger:];
-[PLMAVBBMetric registerForNotifClient:andProfile:];
-[PLMAVBBMetric setAPeriodicProfileId:];
-[PLMAVBBMetric setAPeriodicTriggerCnt:];
-[PLMAVBBMetric setAPeriodicTriggerPayload:];
-[PLMAVBBMetric setLogAgent:];
-[PLMAVBBMetric setStoreMetricsLogger:];
-[PLMAVBBMetric storeMetricsLogger];
```
