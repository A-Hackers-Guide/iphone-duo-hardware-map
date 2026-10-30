# `WiFiAnalyticsAWDWiFiNWActivityScanActivity`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 24 properties, 57 instance methods, 0 class methods

## Instance variables

```
I _assocCount;
I _assocDur;
I _otherCount;
I _otherDur;
I _pnoBSSIDCount;
I _pnoBSSIDDur;
I _pnoSSIDCount;
I _pnoSSIDDur;
I _roamCount;
I _roamDur;
I _userCount;
I _userDur;
{?="assocCount"b1"assocDur"b1"otherCount"b1"otherDur"b1"pnoBSSIDCount"b1"pnoBSSIDDur"b1"pnoSSIDCount"b1"pnoSSIDDur"b1"roamCount"b1"roamDur"b1"userCount"b1"userDur"b1} _has;
```

## Properties

```
@property (TB,N) hasUserCount;
@property (TI,N,V_userCount) userCount;
@property (TB,N) hasUserDur;
@property (TI,N,V_userDur) userDur;
@property (TB,N) hasRoamCount;
@property (TI,N,V_roamCount) roamCount;
@property (TB,N) hasRoamDur;
@property (TI,N,V_roamDur) roamDur;
@property (TB,N) hasAssocCount;
@property (TI,N,V_assocCount) assocCount;
@property (TB,N) hasAssocDur;
@property (TI,N,V_assocDur) assocDur;
@property (TB,N) hasPnoBSSIDCount;
@property (TI,N,V_pnoBSSIDCount) pnoBSSIDCount;
@property (TB,N) hasPnoBSSIDDur;
@property (TI,N,V_pnoBSSIDDur) pnoBSSIDDur;
@property (TB,N) hasPnoSSIDCount;
@property (TI,N,V_pnoSSIDCount) pnoSSIDCount;
@property (TB,N) hasPnoSSIDDur;
@property (TI,N,V_pnoSSIDDur) pnoSSIDDur;
@property (TB,N) hasOtherCount;
@property (TI,N,V_otherCount) otherCount;
@property (TB,N) hasOtherDur;
@property (TI,N,V_otherDur) otherDur;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasPnoBSSIDDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasPnoSSIDCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasAssocDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity assocCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setPnoBSSIDCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasRoamDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasUserCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasOtherCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasAssocCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setAssocDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setUserDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity otherDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setAssocCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setPnoSSIDCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasUserDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasAssocCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasPnoBSSIDCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasOtherDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasUserDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setPnoBSSIDDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setUserCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setOtherCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasPnoSSIDDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity roamDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasOtherDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasOtherCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasRoamCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasAssocDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hash];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasUserCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasRoamDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasPnoSSIDDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasRoamCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity description];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity otherCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity assocDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity pnoSSIDDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setHasPnoBSSIDCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setRoamDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity pnoSSIDCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasPnoBSSIDDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity userCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setPnoSSIDDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity roamCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setOtherDur:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity userDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity pnoBSSIDCount];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity setRoamCount:];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity pnoBSSIDDur];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityScanActivity hasPnoSSIDCount];
```
