# `SFAnalyticsCollection`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _excludedVersion;
@"NSMutableDictionary" _matchingRules;
@"NSString" _processName;
@"NSMutableDictionary" _allowedEvents;
@? _tearDownMetricsHook;
@"<SFAnalyticsCollectionAction>" _actions;
@"NSObject<OS_dispatch_queue>" _queue;
@"SECSFAVersion" _selfVersion;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_matchingRules) matchingRules;
@property (T@"NSMutableDictionary",&,V_allowedEvents) allowedEvents;
@property (TB,V_excludedVersion) excludedVersion;
@property (T@?,C,V_tearDownMetricsHook) tearDownMetricsHook;
@property (T@"<SFAnalyticsCollectionAction>",&,V_actions) actions;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"SECSFAVersion",&,V_selfVersion) selfVersion;
@property (T@"NSString",&,V_processName) processName;
```

## Class methods

```
+[SFAnalyticsCollection isVersionSameOrNewer:than:];
+[SFAnalyticsCollection parseVersion:platform:];
```

## Instance methods

```
-[SFAnalyticsCollection setProcessName:];
-[SFAnalyticsCollection init];
-[SFAnalyticsCollection setActions:];
-[SFAnalyticsCollection dealloc];
-[SFAnalyticsCollection queue];
-[SFAnalyticsCollection actions];
-[SFAnalyticsCollection processName];
-[SFAnalyticsCollection setQueue:];
-[SFAnalyticsCollection drainSetupQueue];
-[SFAnalyticsCollection loadCollection:];
-[SFAnalyticsCollection excludedVersion];
-[SFAnalyticsCollection setSelfVersion:];
-[SFAnalyticsCollection allowedEvents];
-[SFAnalyticsCollection allowedVersionsWithSelf:];
-[SFAnalyticsCollection initWithActionInterface:product:build:];
-[SFAnalyticsCollection match:eventClass:attributes:bucket:logger:];
-[SFAnalyticsCollection matchingRules];
-[SFAnalyticsCollection onQueue_stopMetricCollection];
-[SFAnalyticsCollection parseCollection:logger:];
-[SFAnalyticsCollection selfVersion];
-[SFAnalyticsCollection setAllowedEvents:];
-[SFAnalyticsCollection setExcludedVersion:];
-[SFAnalyticsCollection setMatchingRules:];
-[SFAnalyticsCollection setTearDownMetricsHook:];
-[SFAnalyticsCollection setupMetricsHook:];
-[SFAnalyticsCollection stopMetricCollection];
-[SFAnalyticsCollection storeCollection:logger:];
-[SFAnalyticsCollection tearDownMetricsHook];
```
