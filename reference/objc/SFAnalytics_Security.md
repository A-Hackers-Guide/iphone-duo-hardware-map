# `SFAnalytics`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFAnalyticsProtocol`
- 7 instance variables, 6 properties, 52 instance methods, 23 class methods

## Instance variables

```
@"SFAnalyticsSQLiteStore" _database;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _samplers;
@"NSMutableDictionary" _multisamplers;
b1 _disableLogging;
@"NSMutableSet" _metricsHooks;
@"SFAnalyticsCollection" _collection;
```

## Properties

```
@property (T@"NSMutableSet",&,V_metricsHooks) metricsHooks;
@property (T@"SFAnalyticsCollection",&,V_collection) collection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SFAnalytics databasePath];
+[SFAnalytics logger];
+[SFAnalytics fuzzyDaysSinceDate:];
+[SFAnalytics addOSVersionToEvent:];
+[SFAnalytics defaultAnalyticsDatabasePath:];
+[SFAnalytics defaultProtectedAnalyticsDatabasePath:];
+[SFAnalytics defaultProtectedAnalyticsDatabasePath:uuid:];
+[SFAnalytics encodeSFACollection:error:];
+[SFAnalytics errorWithCode:description:];
+[SFAnalytics errorWithCode:description:underlying:];
+[SFAnalytics formatSFACollection:error:];
+[SFAnalytics fuzzyInteger:];
+[SFAnalytics fuzzyNumber:];
+[SFAnalytics hwModelID];
+[SFAnalytics parseAction:error:];
+[SFAnalytics parseEventFilter:format:error:];
+[SFAnalytics parseRules:format:error:];
+[SFAnalytics parseVersions:error:];
+[SFAnalytics removeLegacyDefaultAnalyticsDatabasePath:usingDispatchToken:];
+[SFAnalytics requiredVersion:rules:reason:error:];
+[SFAnalytics treeOfUnderlyingErrors:depth:];
+[SFAnalytics underlyingErrors:];
+[SFAnalytics validateSFACollection:error:];
```

## Instance methods

```
-[SFAnalytics database];
-[SFAnalytics removeMultiSamplerForName:];
-[SFAnalytics logResultForEvent:hardFailure:result:withAttributes:];
-[SFAnalytics loadCollectionConfiguration];
-[SFAnalytics init];
-[SFAnalytics collection];
-[SFAnalytics logSuccessForEventNamed:];
-[SFAnalytics logHardFailureForEventNamed:withAttributes:];
-[SFAnalytics noteLaunchSequence:];
-[SFAnalytics numberPropertyForKey:];
-[SFAnalytics incrementIntegerPropertyForKey:];
-[SFAnalytics dataPropertyForKey:];
-[SFAnalytics logRockwellFailureForEventNamed:withAttributes:];
-[SFAnalytics setCollection:];
-[SFAnalytics logResultForEvent:hardFailure:result:];
-[SFAnalytics dailyMetrics];
-[SFAnalytics metricsAccountID];
-[SFAnalytics logMetric:withName:];
-[SFAnalytics setDateProperty:forKey:];
-[SFAnalytics setNumberProperty:forKey:];
-[SFAnalytics logSoftFailureForEventNamed:withAttributes:];
-[SFAnalytics datePropertyForKey:];
-[SFAnalytics setDataProperty:forKey:];
-[SFAnalytics updateCollectionConfigurationWithData:];
-[SFAnalytics setMetricsAccountID:];
-[SFAnalytics noteEventNamed:];
-[SFAnalytics AddMultiSamplerForName:withTimeInterval:block:];
-[SFAnalytics addMetricsHook:];
-[SFAnalytics noteEventNamed:timestampBucket:];
-[SFAnalytics logEventNamed:class:attributes:];
-[SFAnalytics addMetricSamplerForName:withTimeInterval:block:];
-[SFAnalytics coreAnalyticsKeyFilter:];
-[SFAnalytics dailyCoreAnalyticsMetrics:];
-[SFAnalytics drainLogQueue];
-[SFAnalytics eventDictForEventName:withAttributes:eventClass:timestampBucket:];
-[SFAnalytics existingMetricSamplerForName:];
-[SFAnalytics existingMultiSamplerForName:];
-[SFAnalytics logEventNamed:class:attributes:timestampBucket:];
-[SFAnalytics logHardFailureForEventNamed:withAttributes:timestampBucket:];
-[SFAnalytics logMetric:withName:oncePerReport:];
-[SFAnalytics logResultForEvent:hardFailure:result:timestampBucket:];
-[SFAnalytics logResultForEvent:hardFailure:result:withAttributes:timestampBucket:];
-[SFAnalytics logSoftFailureForEventNamed:withAttributes:timestampBucket:];
-[SFAnalytics logSuccessForEventNamed:timestampBucket:];
-[SFAnalytics logSystemMetricsForActivityNamed:withAction:];
-[SFAnalytics metricsHooks];
-[SFAnalytics removeMetricSamplerForName:];
-[SFAnalytics removeMetricsHook:];
-[SFAnalytics removeState];
-[SFAnalytics removeStateAndUnlinkFile:];
-[SFAnalytics setMetricsHooks:];
-[SFAnalytics startLogSystemMetricsForActivityNamed:];
```
