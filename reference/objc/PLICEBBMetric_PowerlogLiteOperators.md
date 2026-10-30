# `PLICEBBMetric`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"PLAgent" _logAgent;
@"NSDictionary" _plistSimMetrics;
@"NSMutableDictionary" _sendSimMetrics;
@"NSMutableDictionary" _lteSimMetrics;
@"NSMutableDictionary" _umtsSimMetrics;
@"NSMutableDictionary" _egprsSimMetrics;
@"NSMutableDictionary" _tdsSimMetrics;
@"NSNumber" _error;
@"PLTimer" _tickTock;
@"NSString" _notifyTitle;
@"NSNumber" _aPeriodicTriggerCnt;
@"NSNumber" _aPeriodicProfileId;
@"NSData" _aPeriodicTriggerPayload;
@"NSMutableDictionary" _prodMetrics;
@"PLICEBBHardwareMessage" _storeMetricsLogger;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSDictionary",&,V_plistSimMetrics) plistSimMetrics;
@property (T@"NSMutableDictionary",&,V_sendSimMetrics) sendSimMetrics;
@property (T@"NSMutableDictionary",&,V_lteSimMetrics) lteSimMetrics;
@property (T@"NSMutableDictionary",&,V_umtsSimMetrics) umtsSimMetrics;
@property (T@"NSMutableDictionary",&,V_egprsSimMetrics) egprsSimMetrics;
@property (T@"NSMutableDictionary",&,V_tdsSimMetrics) tdsSimMetrics;
@property (T@"NSNumber",&,V_error) error;
@property (T@"PLTimer",&,V_tickTock) tickTock;
@property (T@"NSString",&,V_notifyTitle) notifyTitle;
@property (T@"NSNumber",&,V_aPeriodicTriggerCnt) aPeriodicTriggerCnt;
@property (T@"NSNumber",&,V_aPeriodicProfileId) aPeriodicProfileId;
@property (T@"NSData",&,V_aPeriodicTriggerPayload) aPeriodicTriggerPayload;
@property (T@"NSMutableDictionary",&,V_prodMetrics) prodMetrics;
@property (T@"PLICEBBHardwareMessage",&,V_storeMetricsLogger) storeMetricsLogger;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"PLAgent",&,V_logAgent) logAgent;
```

## Class methods

```
+[PLICEBBMetric sharedInstance];
```

## Instance methods

```
-[PLICEBBMetric setError:];
-[PLICEBBMetric queue];
-[PLICEBBMetric error];
-[PLICEBBMetric setQueue:];
-[PLICEBBMetric plistSimMetrics];
-[PLICEBBMetric setProdMetrics:];
-[PLICEBBMetric egprsSimMetrics];
-[PLICEBBMetric setNotifyTitle:];
-[PLICEBBMetric aPeriodicProfileId];
-[PLICEBBMetric aPeriodicTriggerCnt];
-[PLICEBBMetric aPeriodicTriggerPayload];
-[PLICEBBMetric deregisterForNotifications:];
-[PLICEBBMetric initializeDataStoreBBTS:triggerCnt:triggerId:];
-[PLICEBBMetric initializeMetricsDictWithTS:triggerCnt:triggerId:];
-[PLICEBBMetric initializeMetricsSim];
-[PLICEBBMetric logAgent];
-[PLICEBBMetric lteSimMetrics];
-[PLICEBBMetric modelProdMetricsNotify];
-[PLICEBBMetric modelSimMetricsNotify:];
-[PLICEBBMetric notifyTitle];
-[PLICEBBMetric prodMetrics];
-[PLICEBBMetric queueAperiodicMetricId:payload:profileId:];
-[PLICEBBMetric queuePeriodicMetricId:payload:forTrigger:];
-[PLICEBBMetric registerForNotifClient:andProfile:];
-[PLICEBBMetric sendSimMetrics];
-[PLICEBBMetric setAPeriodicProfileId:];
-[PLICEBBMetric setAPeriodicTriggerCnt:];
-[PLICEBBMetric setAPeriodicTriggerPayload:];
-[PLICEBBMetric setEgprsSimMetrics:];
-[PLICEBBMetric setLogAgent:];
-[PLICEBBMetric setLteSimMetrics:];
-[PLICEBBMetric setPlistSimMetrics:];
-[PLICEBBMetric setSendSimMetrics:];
-[PLICEBBMetric setStoreMetricsLogger:];
-[PLICEBBMetric setTdsSimMetrics:];
-[PLICEBBMetric setTickTock:];
-[PLICEBBMetric setUmtsSimMetrics:];
-[PLICEBBMetric storeMetricsLogger];
-[PLICEBBMetric tdsSimMetrics];
-[PLICEBBMetric tickTock];
-[PLICEBBMetric umtsSimMetrics];
```
