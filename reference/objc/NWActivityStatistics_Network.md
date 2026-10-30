# `NWActivityStatistics`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 15 properties, 27 instance methods, 1 class methods

## Instance variables

```
C _metricType;
@"NSUUID" _externallyVisibleActivityUUID;
@"NSUUID" _externallyVisibleParentUUID;
@"NSUUID" _activityUUID;
@"NSUUID" _parentUUID;
@"NSDictionary" _layer2Report;
@"NSDictionary" _deviceReport;
@"NSMutableDictionary" _dictionaryReport;
{nw_activity_report_s="investigation_identifier"Q"domain"I"label"I"activity_uuid"[16C]"parent_activity_uuid"[16C]"bundle_id"[256c]"start_time_unix_nano"Q"retry"b1"__pad_bits"b7"__pad"[7C]} _report;
```

## Properties

```
@property (T{nw_activity_report_s=QII[16C][16C][256c]Qb1b7[7C]},N,V_report) report;
@property (TC,N,V_metricType) metricType;
@property (T@"NSMutableDictionary",&,N,V_dictionaryReport) dictionaryReport;
@property (T@"NSUUID",&,N,V_activityUUID) activityUUID;
@property (T@"NSUUID",&,N,V_parentUUID) parentUUID;
@property (TI,R,N) domain;
@property (TI,R,N) label;
@property (TB,R,N) retry;
@property (TQ,R,N) investigation_identifier;
@property (TQ,R,N) startTimeUnixNano;
@property (T@"NSUUID",&,N,V_externallyVisibleActivityUUID) externallyVisibleActivityUUID;
@property (T@"NSUUID",&,N,V_externallyVisibleParentUUID) externallyVisibleParentUUID;
@property (T@"NSDictionary",&,N,V_layer2Report) layer2Report;
@property (T@"NSDictionary",&,N,V_deviceReport) deviceReport;
@property (T@"NSString",&,N) bundleID;
```

## Class methods

```
+[NWActivityStatistics createActivityReportDictionary:uuidString:parentUUIDString:];
```

## Instance methods

```
-[NWActivityStatistics setReport:];
-[NWActivityStatistics setDeviceReport:];
-[NWActivityStatistics layer2Report];
-[NWActivityStatistics setMetricType:];
-[NWActivityStatistics metricType];
-[NWActivityStatistics setParentUUID:];
-[NWActivityStatistics domain];
-[NWActivityStatistics label];
-[NWActivityStatistics setBundleID:];
-[NWActivityStatistics setExternallyVisibleParentUUID:];
-[NWActivityStatistics externallyVisibleActivityUUID];
-[NWActivityStatistics initWithJSONData:];
-[NWActivityStatistics setExternallyVisibleActivityUUID:];
-[NWActivityStatistics startTimeUnixNano];
-[NWActivityStatistics setLayer2Report:];
-[NWActivityStatistics activityUUID];
-[NWActivityStatistics retry];
-[NWActivityStatistics initWithNWActivityReport:length:];
-[NWActivityStatistics setActivityUUID:];
-[NWActivityStatistics investigation_identifier];
-[NWActivityStatistics parentUUID];
-[NWActivityStatistics dictionaryReport];
-[NWActivityStatistics bundleID];
-[NWActivityStatistics setDictionaryReport:];
-[NWActivityStatistics externallyVisibleParentUUID];
-[NWActivityStatistics report];
-[NWActivityStatistics deviceReport];
```
