# `CWFPowerTableElectionTelemetry`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDateFormatter" _dateFormatter;
@"NSDate" _handoffAvailableDate;
@"NSString" _handoffWiFiAssetVersionInfo;
@"NSString" _handoffBTAssetVersionInfo;
@"NSString" _initialAssetFilename;
@"NSString" _initialAssetVersionInfoVersion;
@"NSDate" _initialAssetVersionInfoDate;
C _readinessReply;
@"NSDate" _readinessReplyDeliveredDate;
@"NSDate" _electionStartNotificationDate;
C _voteResult;
@"NSDate" _voteDeliveredDate;
@"NSString" _finalAssetVersionInfoVersion;
@"NSDate" _finalAssetVersionInfoDate;
C _wifiInitiatedPTUpdate;
C _btInitiatedPTUpdate;
@"NSString" _finalResultString;
```

## Class methods

```
+[CWFPowerTableElectionTelemetry sharedObj];
```

## Instance methods

```
-[CWFPowerTableElectionTelemetry init];
-[CWFPowerTableElectionTelemetry setFinalResultAndSendTelemetry:];
-[CWFPowerTableElectionTelemetry getElectionSummaryStringForABC];
-[CWFPowerTableElectionTelemetry getNSDateFromString:];
-[CWFPowerTableElectionTelemetry sendTelemetryAndClear];
-[CWFPowerTableElectionTelemetry setCandidatePowerTableVersionBluetooth:];
-[CWFPowerTableElectionTelemetry setCandidatePowerTableVersionWiFi:];
-[CWFPowerTableElectionTelemetry setCurrentPowerTableVersionAtReadiness:fileName:];
-[CWFPowerTableElectionTelemetry setFinalPowerTableVersion:];
-[CWFPowerTableElectionTelemetry setPowerTableReadiness:];
-[CWFPowerTableElectionTelemetry setPowerTableVote:];
```
