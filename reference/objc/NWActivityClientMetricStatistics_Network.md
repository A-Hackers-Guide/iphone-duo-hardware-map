# `NWActivityClientMetricStatistics`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _activityUUID;
@"NSUUID" _externallyVisibleActivityUUID;
@"NSString" _bundleID;
@"NSDictionary" _dictionaryRepresentation;
@"NSData" _metricData;
{nw_activity_client_metric_report_s="activity_uuid"[16C]"client_metric_name"[256c]"client_metric"[5000c]"__pad"[0C]} _report;
```

## Properties

```
@property (T{nw_activity_client_metric_report_s=[16C][256c][5000c][0C]},N,V_report) report;
@property (T@"NSUUID",&,N,V_activityUUID) activityUUID;
@property (T@"NSString",&,N) clientMetricName;
@property (T@"NSString",&,N) clientMetricString;
@property (T@"NSDictionary",&,N,V_dictionaryRepresentation) dictionaryRepresentation;
@property (T@"NSData",&,N,V_metricData) metricData;
@property (T@"NSUUID",&,N,V_externallyVisibleActivityUUID) externallyVisibleActivityUUID;
@property (T@"NSString",&,N,V_bundleID) bundleID;
@property (T@"NSDictionary",R,N) clientMetric;
```

## Instance methods

```
-[NWActivityClientMetricStatistics setReport:];
-[NWActivityClientMetricStatistics setBundleID:];
-[NWActivityClientMetricStatistics externallyVisibleActivityUUID];
-[NWActivityClientMetricStatistics setExternallyVisibleActivityUUID:];
-[NWActivityClientMetricStatistics activityUUID];
-[NWActivityClientMetricStatistics setActivityUUID:];
-[NWActivityClientMetricStatistics metricData];
-[NWActivityClientMetricStatistics bundleID];
-[NWActivityClientMetricStatistics initWithData:];
-[NWActivityClientMetricStatistics report];
-[NWActivityClientMetricStatistics dictionaryRepresentation];
-[NWActivityClientMetricStatistics clientMetric];
-[NWActivityClientMetricStatistics clientMetricName];
-[NWActivityClientMetricStatistics clientMetricString];
-[NWActivityClientMetricStatistics initWithNWActivityClientMetricReport:length:];
-[NWActivityClientMetricStatistics setClientMetricName:];
-[NWActivityClientMetricStatistics setClientMetricString:];
-[NWActivityClientMetricStatistics setDictionaryRepresentation:];
-[NWActivityClientMetricStatistics setMetricData:];
```
