# `WiFiAnalyticsAWDWiFiDPSEpilogue`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 14 instance variables, 24 properties, 69 instance methods, 2 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _accessPointInfos;
i _action;
I _actionIntVal;
i _afterRecommendedAction;
@"NSMutableArray" _associationChanges;
i _beforeAction;
@"WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences" _changes;
@"WiFiAnalyticsAWDWAPeerDiscoveryInfo" _discoveredPeerInfo;
@"WiFiAnalyticsAWDWAQuickDpsStats" _qDpsStats;
i _studyType;
@"WiFiAnalyticsAWDWASymptomsDnsStats" _symptomsDnsStats;
B _isAssociatedAtStudyEnd;
{?="timestamp"b1"action"b1"actionIntVal"b1"afterRecommendedAction"b1"beforeAction"b1"studyType"b1"isAssociatedAtStudyEnd"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasBeforeAction;
@property (Ti,N,V_beforeAction) beforeAction;
@property (TB,N) hasAction;
@property (Ti,N,V_action) action;
@property (TB,N) hasAfterRecommendedAction;
@property (Ti,N,V_afterRecommendedAction) afterRecommendedAction;
@property (TB,R,N) hasChanges;
@property (T@"WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences",&,N,V_changes) changes;
@property (T@"NSMutableArray",&,N,V_associationChanges) associationChanges;
@property (TB,R,N) hasQDpsStats;
@property (T@"WiFiAnalyticsAWDWAQuickDpsStats",&,N,V_qDpsStats) qDpsStats;
@property (TB,N) hasActionIntVal;
@property (TI,N,V_actionIntVal) actionIntVal;
@property (TB,N) hasStudyType;
@property (Ti,N,V_studyType) studyType;
@property (TB,N) hasIsAssociatedAtStudyEnd;
@property (TB,N,V_isAssociatedAtStudyEnd) isAssociatedAtStudyEnd;
@property (TB,R,N) hasSymptomsDnsStats;
@property (T@"WiFiAnalyticsAWDWASymptomsDnsStats",&,N,V_symptomsDnsStats) symptomsDnsStats;
@property (TB,R,N) hasDiscoveredPeerInfo;
@property (T@"WiFiAnalyticsAWDWAPeerDiscoveryInfo",&,N,V_discoveredPeerInfo) discoveredPeerInfo;
@property (T@"NSMutableArray",&,N,V_accessPointInfos) accessPointInfos;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiDPSEpilogue accessPointInfoType];
+[WiFiAnalyticsAWDWiFiDPSEpilogue associationChangesType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSEpilogue changes];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasTimestamp];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue writeTo:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue timestamp];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue action];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setChanges:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasChanges];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hash];
-[WiFiAnalyticsAWDWiFiDPSEpilogue copyTo:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue description];
-[WiFiAnalyticsAWDWiFiDPSEpilogue readFrom:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue isEqual:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasAction];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue StringAsAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue actionAsString:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue afterRecommendedActionAsString:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasActionIntVal];
-[WiFiAnalyticsAWDWiFiDPSEpilogue StringAsAfterRecommendedAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue StringAsBeforeAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue StringAsStudyType:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasBeforeAction];
-[WiFiAnalyticsAWDWiFiDPSEpilogue accessPointInfoAtIndex:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue accessPointInfos];
-[WiFiAnalyticsAWDWiFiDPSEpilogue accessPointInfosCount];
-[WiFiAnalyticsAWDWiFiDPSEpilogue actionIntVal];
-[WiFiAnalyticsAWDWiFiDPSEpilogue addAccessPointInfo:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue addAssociationChanges:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue afterRecommendedAction];
-[WiFiAnalyticsAWDWiFiDPSEpilogue associationChanges];
-[WiFiAnalyticsAWDWiFiDPSEpilogue associationChangesAtIndex:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue associationChangesCount];
-[WiFiAnalyticsAWDWiFiDPSEpilogue beforeAction];
-[WiFiAnalyticsAWDWiFiDPSEpilogue beforeActionAsString:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue clearAccessPointInfos];
-[WiFiAnalyticsAWDWiFiDPSEpilogue clearAssociationChanges];
-[WiFiAnalyticsAWDWiFiDPSEpilogue discoveredPeerInfo];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasAfterRecommendedAction];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasDiscoveredPeerInfo];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasIsAssociatedAtStudyEnd];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasQDpsStats];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasStudyType];
-[WiFiAnalyticsAWDWiFiDPSEpilogue hasSymptomsDnsStats];
-[WiFiAnalyticsAWDWiFiDPSEpilogue isAssociatedAtStudyEnd];
-[WiFiAnalyticsAWDWiFiDPSEpilogue qDpsStats];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setAccessPointInfos:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setActionIntVal:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setAfterRecommendedAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setAssociationChanges:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setBeforeAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setDiscoveredPeerInfo:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasActionIntVal:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasAfterRecommendedAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasBeforeAction:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasIsAssociatedAtStudyEnd:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setHasStudyType:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setIsAssociatedAtStudyEnd:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setQDpsStats:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setStudyType:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue setSymptomsDnsStats:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue studyType];
-[WiFiAnalyticsAWDWiFiDPSEpilogue studyTypeAsString:];
-[WiFiAnalyticsAWDWiFiDPSEpilogue symptomsDnsStats];
```
