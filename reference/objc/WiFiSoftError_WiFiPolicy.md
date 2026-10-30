# `WiFiSoftError`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 66 instance methods, 4 class methods

## Instance variables

```
B _isRecommendedPriority;
q _maxOccurrences;
q _metricSubmissionSamplingRate;
q _maxNonUIActions;
q _intervalForMaxNonUIActions;
q _maxUIActions;
q _intervalForMaxUIActions;
q _maxLogMessageLength;
@"NSString" _name;
q _enabled;
q _metricsEnabled;
d _creationDate;
@"NSMutableArray" _occurrenceTimestamps;
@"NSNumber" _lastTimestamp;
@"NSMutableString" _logMessage;
@"NSString" _metricEventName;
@"SDRDiagnosticReporter" _abcReporter;
@"NSMutableArray" _abcSubmissionTimestamps;
@"NSMutableArray" _simulateCrashTimestamps;
@"NSMutableArray" _hudTimestamps;
@"NSMutableArray" _askToLaunchTapToRadarTimestamps;
@"NSMutableArray" _tapToRadarTimestamps;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (Tq,N,V_enabled) enabled;
@property (Tq,N,V_metricsEnabled) metricsEnabled;
@property (Td,N,V_creationDate) creationDate;
@property (T@"NSMutableArray",&,N,V_occurrenceTimestamps) occurrenceTimestamps;
@property (T@"NSNumber",&,N,V_lastTimestamp) lastTimestamp;
@property (T@"NSMutableString",&,N,V_logMessage) logMessage;
@property (T@"NSString",&,N,V_metricEventName) metricEventName;
@property (T@"SDRDiagnosticReporter",&,N,V_abcReporter) abcReporter;
@property (T@"NSMutableArray",&,N,V_abcSubmissionTimestamps) abcSubmissionTimestamps;
@property (T@"NSMutableArray",&,N,V_simulateCrashTimestamps) simulateCrashTimestamps;
@property (T@"NSMutableArray",&,N,V_hudTimestamps) hudTimestamps;
@property (T@"NSMutableArray",&,N,V_askToLaunchTapToRadarTimestamps) askToLaunchTapToRadarTimestamps;
@property (T@"NSMutableArray",&,N,V_tapToRadarTimestamps) tapToRadarTimestamps;
@property (Tq,R,N,V_maxOccurrences) maxOccurrences;
@property (Tq,R,N,V_metricSubmissionSamplingRate) metricSubmissionSamplingRate;
@property (Tq,R,N,V_maxNonUIActions) maxNonUIActions;
@property (Tq,R,N,V_intervalForMaxNonUIActions) intervalForMaxNonUIActions;
@property (Tq,R,N,V_maxUIActions) maxUIActions;
@property (Tq,R,N,V_intervalForMaxUIActions) intervalForMaxUIActions;
@property (Tq,R,N,V_maxLogMessageLength) maxLogMessageLength;
@property (TB,R,N,V_isRecommendedPriority) isRecommendedPriority;
```

## Class methods

```
+[WiFiSoftError _updateHUDWithHost:messageDict:];
+[WiFiSoftError _cloudAssetsFetchHandler:];
+[WiFiSoftError _submitSummaryReportMetric];
+[WiFiSoftError _updateHUDWithMessage:];
```

## Instance methods

```
-[WiFiSoftError enabled];
-[WiFiSoftError resetCount];
-[WiFiSoftError dealloc];
-[WiFiSoftError count];
-[WiFiSoftError creationDate];
-[WiFiSoftError lastTimestamp];
-[WiFiSoftError metricsEnabled];
-[WiFiSoftError setLastTimestamp:];
-[WiFiSoftError setCreationDate:];
-[WiFiSoftError setEnabled:];
-[WiFiSoftError setName:];
-[WiFiSoftError name];
-[WiFiSoftError initWithName:];
-[WiFiSoftError incrementCount];
-[WiFiSoftError logMessage];
-[WiFiSoftError askToLaunchTapToRadarTimestamps];
-[WiFiSoftError maxNonUIActions];
-[WiFiSoftError metricEventName];
-[WiFiSoftError setAbcReporter:];
-[WiFiSoftError writeLogMessage];
-[WiFiSoftError clearLogMessage];
-[WiFiSoftError _addConfigurationData:];
-[WiFiSoftError _addGenericMetricData:];
-[WiFiSoftError _countOf:withinInterval:];
-[WiFiSoftError _maxNonUIActionsReachedFor:];
-[WiFiSoftError _maxUIActionsReachedFor:];
-[WiFiSoftError _recordCurrentTimestampIn:];
-[WiFiSoftError _resetCount];
-[WiFiSoftError abcReporter];
-[WiFiSoftError abcSubmissionTimestamps];
-[WiFiSoftError appendLogMessage:includeTimestamp:];
-[WiFiSoftError askToLaunchTapToRadarWithMessage:];
-[WiFiSoftError askToLaunchTapToRadarWithMessage:completionHandler:];
-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:];
-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:completionHandler:];
-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:];
-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:keywords:displayReason:completionHandler:];
-[WiFiSoftError hudTimestamps];
-[WiFiSoftError initWithName:andParams:];
-[WiFiSoftError intervalForMaxNonUIActions];
-[WiFiSoftError intervalForMaxUIActions];
-[WiFiSoftError isRecommendedPriority];
-[WiFiSoftError maxLogMessageLength];
-[WiFiSoftError maxOccurrences];
-[WiFiSoftError maxUIActions];
-[WiFiSoftError metricSubmissionSamplingRate];
-[WiFiSoftError occurrenceTimestamps];
-[WiFiSoftError recentCountWithinTimeInterval:];
-[WiFiSoftError setAbcSubmissionTimestamps:];
-[WiFiSoftError setAskToLaunchTapToRadarTimestamps:];
-[WiFiSoftError setHudTimestamps:];
-[WiFiSoftError setLogMessage:];
-[WiFiSoftError setMetricEventName:];
-[WiFiSoftError setMetricsEnabled:];
-[WiFiSoftError setOccurrenceTimestamps:];
-[WiFiSoftError setSimulateCrashTimestamps:];
-[WiFiSoftError setTapToRadarTimestamps:];
-[WiFiSoftError simulateCrashTimestamps];
-[WiFiSoftError submitABCReportWithReason:];
-[WiFiSoftError submitABCReportWithReason:event:];
-[WiFiSoftError submitMetric];
-[WiFiSoftError submitMetricWithData:];
-[WiFiSoftError tapToRadarTimestamps];
-[WiFiSoftError tapToRadarWithURL:completionHandler:];
-[WiFiSoftError updateHUDWithHost:messageDict:];
-[WiFiSoftError updateHUDWithMessage:];
```
