# `PLSinopeBBMetric`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"PLAgent" _logAgent;
@"NSString" _notificationTitle;
@"NSNumber" _aPeriodicProfileId;
@"NSData" _aPeriodicTriggerPayload;
@"NSNumber" _aPeriodicTriggerCnt;
@"NSData" _periodicTriggerPayload;
@"NSMutableDictionary" _metricDict;
@"PLSinopeBBHardwareMessage" _hardwareMessage;
```

## Properties

```
@property (T@"NSString",&,V_notificationTitle) notificationTitle;
@property (T@"NSNumber",&,V_aPeriodicProfileId) aPeriodicProfileId;
@property (T@"NSData",&,V_aPeriodicTriggerPayload) aPeriodicTriggerPayload;
@property (T@"NSNumber",&,V_aPeriodicTriggerCnt) aPeriodicTriggerCnt;
@property (T@"NSData",&,V_periodicTriggerPayload) periodicTriggerPayload;
@property (T@"NSMutableDictionary",&,V_metricDict) metricDict;
@property (T@"PLSinopeBBHardwareMessage",&,V_hardwareMessage) hardwareMessage;
@property (T@"PLAgent",&,V_logAgent) logAgent;
```

## Class methods

```
+[PLSinopeBBMetric sharedInstance];
```

## Instance methods

```
-[PLSinopeBBMetric setNotificationTitle:];
-[PLSinopeBBMetric notificationTitle];
-[PLSinopeBBMetric metricDict];
-[PLSinopeBBMetric setMetricDict:];
-[PLSinopeBBMetric hardwareMessage];
-[PLSinopeBBMetric aPeriodicProfileId];
-[PLSinopeBBMetric aPeriodicTriggerCnt];
-[PLSinopeBBMetric aPeriodicTriggerPayload];
-[PLSinopeBBMetric flushPeriodicMetrics];
-[PLSinopeBBMetric initializeDataStoreBBTS:triggerCnt:triggerId:];
-[PLSinopeBBMetric initializeMetricsDictWithTS:triggerCnt:triggerId:];
-[PLSinopeBBMetric logAgent];
-[PLSinopeBBMetric modelProdMetricsNotify];
-[PLSinopeBBMetric periodicTriggerPayload];
-[PLSinopeBBMetric queueAperiodicMetricId:payload:forTrigger:];
-[PLSinopeBBMetric queuePeriodicMetricId:payload:forTrigger:];
-[PLSinopeBBMetric registerForNotifClient:andProfile:];
-[PLSinopeBBMetric setAPeriodicProfileId:];
-[PLSinopeBBMetric setAPeriodicTriggerCnt:];
-[PLSinopeBBMetric setAPeriodicTriggerPayload:];
-[PLSinopeBBMetric setHardwareMessage:];
-[PLSinopeBBMetric setLogAgent:];
-[PLSinopeBBMetric setPeriodicTriggerPayload:];
```
