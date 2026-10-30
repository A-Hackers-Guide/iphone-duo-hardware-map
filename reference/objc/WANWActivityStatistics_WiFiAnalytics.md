# `WANWActivityStatistics`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _fromInitWithPBCodableData;
I _awdMetricID;
@"PBCodable" _awdReport;
@"NSArray" _activityUUIDs;
@"NSArray" _externallyVisibleActivityUUIDs;
@"_TtC13WiFiAnalytics21WANWActivityTransform" _obj;
```

## Properties

```
@property (T@"PBCodable",&,N,V_awdReport) awdReport;
@property (TI,N,V_awdMetricID) awdMetricID;
@property (T@"_TtC13WiFiAnalytics21WANWActivityTransform",&,N,V_obj) obj;
@property (T@"NSArray",&,V_activityUUIDs) activityUUIDs;
@property (T@"NSArray",&,V_externallyVisibleActivityUUIDs) externallyVisibleActivityUUIDs;
```

## Instance methods

```
-[WANWActivityStatistics activityUUIDs];
-[WANWActivityStatistics externallyVisibleActivityUUIDs];
-[WANWActivityStatistics initWithWAActivityReport:length:];
-[WANWActivityStatistics setActivityUUIDs:];
-[WANWActivityStatistics obj];
-[WANWActivityStatistics getTransformedFlattenedFrom:style:index:];
-[WANWActivityStatistics initWithPBCodableData:];
-[WANWActivityStatistics getTransformedFlattened:];
-[WANWActivityStatistics awdMetricID];
-[WANWActivityStatistics getTransformedFlattenedFrom:style:];
-[WANWActivityStatistics setAwdReport:];
-[WANWActivityStatistics setAwdMetricID:];
-[WANWActivityStatistics awdReport];
-[WANWActivityStatistics setObj:];
-[WANWActivityStatistics expandKeyNameLengths:];
-[WANWActivityStatistics setExternallyVisibleActivityUUIDs:];
```
