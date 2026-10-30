# `NWActivityEpilogueStatistics`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 22 properties, 34 instance methods, 1 class methods

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
{nw_activity_epilogue_report_s="duration_msecs"Q"activity"{nw_activity_report_s="investigation_identifier"Q"domain"I"label"I"activity_uuid"[16C]"parent_activity_uuid"[16C]"bundle_id"[256c]"start_time_unix_nano"Q"retry"b1"__pad_bits"b7"__pad"[7C]}"fragments_quenched"I"underlying_error_domain"i"underlying_error_code"i"completion_reason"i"underlying_error_domain_string"[256c]"end_time_unix_nano"Q"__pad"[0C]} _report;
```

## Properties

```
@property (T{nw_activity_epilogue_report_s=Q{nw_activity_report_s=QII[16C][16C][256c]Qb1b7[7C]}Iiii[256c]Q[0C]},N,V_report) report;
@property (T@"NSMutableDictionary",&,N,V_dictionaryReport) dictionaryReport;
@property (TC,N,V_metricType) metricType;
@property (T@"NSUUID",&,N,V_activityUUID) activityUUID;
@property (T@"NSUUID",&,N,V_parentUUID) parentUUID;
@property (TI,R,N) domain;
@property (TI,R,N) label;
@property (TB,R,N) retry;
@property (TQ,R,N) investigation_identifier;
@property (TQ,R,N) durationMsecs;
@property (TI,R,N) fragmentsQuenched;
@property (Ti,R,N) completionReason;
@property (Tr*,R,N) underlyingErrorDomainString;
@property (Ti,R,N) underlyingErrorDomain;
@property (Ti,R,N) underlyingErrorCode;
@property (TQ,R,N) startTimeUnixNano;
@property (TQ,R,N) endTimeUnixNano;
@property (T@"NSUUID",&,N,V_externallyVisibleActivityUUID) externallyVisibleActivityUUID;
@property (T@"NSUUID",&,N,V_externallyVisibleParentUUID) externallyVisibleParentUUID;
@property (T@"NSDictionary",&,N,V_layer2Report) layer2Report;
@property (T@"NSDictionary",&,N,V_deviceReport) deviceReport;
@property (T@"NSString",&,N) bundleID;
```

## Class methods

```
+[NWActivityEpilogueStatistics createActivityEpilogueDictionary:];
```

## Instance methods

```
-[NWActivityEpilogueStatistics setReport:];
-[NWActivityEpilogueStatistics setDeviceReport:];
-[NWActivityEpilogueStatistics layer2Report];
-[NWActivityEpilogueStatistics setMetricType:];
-[NWActivityEpilogueStatistics metricType];
-[NWActivityEpilogueStatistics setParentUUID:];
-[NWActivityEpilogueStatistics endTimeUnixNano];
-[NWActivityEpilogueStatistics domain];
-[NWActivityEpilogueStatistics label];
-[NWActivityEpilogueStatistics setBundleID:];
-[NWActivityEpilogueStatistics setExternallyVisibleParentUUID:];
-[NWActivityEpilogueStatistics externallyVisibleActivityUUID];
-[NWActivityEpilogueStatistics fragmentsQuenched];
-[NWActivityEpilogueStatistics initWithJSONData:];
-[NWActivityEpilogueStatistics setExternallyVisibleActivityUUID:];
-[NWActivityEpilogueStatistics startTimeUnixNano];
-[NWActivityEpilogueStatistics setLayer2Report:];
-[NWActivityEpilogueStatistics activityUUID];
-[NWActivityEpilogueStatistics retry];
-[NWActivityEpilogueStatistics completionReason];
-[NWActivityEpilogueStatistics underlyingErrorDomainString];
-[NWActivityEpilogueStatistics setActivityUUID:];
-[NWActivityEpilogueStatistics investigation_identifier];
-[NWActivityEpilogueStatistics durationMsecs];
-[NWActivityEpilogueStatistics parentUUID];
-[NWActivityEpilogueStatistics underlyingErrorCode];
-[NWActivityEpilogueStatistics dictionaryReport];
-[NWActivityEpilogueStatistics bundleID];
-[NWActivityEpilogueStatistics setDictionaryReport:];
-[NWActivityEpilogueStatistics externallyVisibleParentUUID];
-[NWActivityEpilogueStatistics initWithNWActivityEpilogueReport:length:];
-[NWActivityEpilogueStatistics report];
-[NWActivityEpilogueStatistics underlyingErrorDomain];
-[NWActivityEpilogueStatistics deviceReport];
```
