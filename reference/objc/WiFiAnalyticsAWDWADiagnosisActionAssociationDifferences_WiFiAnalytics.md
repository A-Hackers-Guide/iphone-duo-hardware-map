# `WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 43 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _additionalInfo;
i _eventType;
B _changedChannel;
B _changedDNSPrimary;
B _changedDNSSecondary;
B _changedMAC;
B _newBSSID;
{?="timestamp"b1"additionalInfo"b1"eventType"b1"changedChannel"b1"changedDNSPrimary"b1"changedDNSSecondary"b1"changedMAC"b1"newBSSID"b1} _has;
```

## Properties

```
@property (TB,N) hasNewBSSID;
@property (TB,N,V_newBSSID) newBSSID;
@property (TB,N) hasChangedChannel;
@property (TB,N,V_changedChannel) changedChannel;
@property (TB,N) hasChangedDNSPrimary;
@property (TB,N,V_changedDNSPrimary) changedDNSPrimary;
@property (TB,N) hasChangedDNSSecondary;
@property (TB,N,V_changedDNSSecondary) changedDNSSecondary;
@property (TB,N) hasChangedMAC;
@property (TB,N,V_changedMAC) changedMAC;
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasEventType;
@property (Ti,N,V_eventType) eventType;
@property (TB,N) hasAdditionalInfo;
@property (TI,N,V_additionalInfo) additionalInfo;
```

## Instance methods

```
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasTimestamp];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasTimestamp:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setTimestamp:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences eventType];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences writeTo:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setEventType:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasEventType];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences mergeFrom:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences eventTypeAsString:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences timestamp];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasEventType:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences additionalInfo];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences StringAsEventType:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hash];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences copyTo:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences description];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences readFrom:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences copyWithZone:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences isEqual:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setAdditionalInfo:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences dictionaryRepresentation];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasNewBSSID:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences changedChannel];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences changedDNSPrimary];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences changedDNSSecondary];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences changedMAC];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasAdditionalInfo];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasChangedChannel];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasChangedDNSPrimary];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasChangedDNSSecondary];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasChangedMAC];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences hasNewBSSID];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences newBSSID];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setChangedChannel:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setChangedDNSPrimary:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setChangedDNSSecondary:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setChangedMAC:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasAdditionalInfo:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasChangedChannel:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasChangedDNSPrimary:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasChangedDNSSecondary:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setHasChangedMAC:];
-[WiFiAnalyticsAWDWADiagnosisActionAssociationDifferences setNewBSSID:];
```
