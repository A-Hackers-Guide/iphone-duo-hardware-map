# `WiFiAnalyticsAWDWiFiDPSReport`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 10 properties, 43 instance methods, 4 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _dpsCounterSamples;
@"WiFiAnalyticsAWDWiFiDPSEpilogue" _dpsEpiloge;
@"NSMutableArray" _probeResults;
@"WiFiAnalyticsAWDWiFiDPSSnapshot" _snapshot;
@"NSMutableArray" _stallNotifications;
@"NSMutableArray" _usbEvents;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_stallNotifications) stallNotifications;
@property (T@"NSMutableArray",&,N,V_probeResults) probeResults;
@property (T@"NSMutableArray",&,N,V_dpsCounterSamples) dpsCounterSamples;
@property (TB,R,N) hasDpsEpiloge;
@property (T@"WiFiAnalyticsAWDWiFiDPSEpilogue",&,N,V_dpsEpiloge) dpsEpiloge;
@property (TB,R,N) hasSnapshot;
@property (T@"WiFiAnalyticsAWDWiFiDPSSnapshot",&,N,V_snapshot) snapshot;
@property (T@"NSMutableArray",&,N,V_usbEvents) usbEvents;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiDPSReport probeResultType];
+[WiFiAnalyticsAWDWiFiDPSReport dpsCounterSampleType];
+[WiFiAnalyticsAWDWiFiDPSReport stallNotificationType];
+[WiFiAnalyticsAWDWiFiDPSReport usbEventType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSReport hasTimestamp];
-[WiFiAnalyticsAWDWiFiDPSReport setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSReport setTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSReport writeTo:];
-[WiFiAnalyticsAWDWiFiDPSReport setSnapshot:];
-[WiFiAnalyticsAWDWiFiDPSReport snapshot];
-[WiFiAnalyticsAWDWiFiDPSReport mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSReport timestamp];
-[WiFiAnalyticsAWDWiFiDPSReport hasSnapshot];
-[WiFiAnalyticsAWDWiFiDPSReport hash];
-[WiFiAnalyticsAWDWiFiDPSReport copyTo:];
-[WiFiAnalyticsAWDWiFiDPSReport description];
-[WiFiAnalyticsAWDWiFiDPSReport readFrom:];
-[WiFiAnalyticsAWDWiFiDPSReport copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSReport isEqual:];
-[WiFiAnalyticsAWDWiFiDPSReport dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSReport addProbeResult:];
-[WiFiAnalyticsAWDWiFiDPSReport addDpsCounterSample:];
-[WiFiAnalyticsAWDWiFiDPSReport addStallNotification:];
-[WiFiAnalyticsAWDWiFiDPSReport addUsbEvent:];
-[WiFiAnalyticsAWDWiFiDPSReport clearDpsCounterSamples];
-[WiFiAnalyticsAWDWiFiDPSReport clearProbeResults];
-[WiFiAnalyticsAWDWiFiDPSReport clearStallNotifications];
-[WiFiAnalyticsAWDWiFiDPSReport clearUsbEvents];
-[WiFiAnalyticsAWDWiFiDPSReport dpsCounterSampleAtIndex:];
-[WiFiAnalyticsAWDWiFiDPSReport dpsCounterSamples];
-[WiFiAnalyticsAWDWiFiDPSReport dpsCounterSamplesCount];
-[WiFiAnalyticsAWDWiFiDPSReport dpsEpiloge];
-[WiFiAnalyticsAWDWiFiDPSReport hasDpsEpiloge];
-[WiFiAnalyticsAWDWiFiDPSReport probeResultAtIndex:];
-[WiFiAnalyticsAWDWiFiDPSReport probeResults];
-[WiFiAnalyticsAWDWiFiDPSReport probeResultsCount];
-[WiFiAnalyticsAWDWiFiDPSReport setDpsCounterSamples:];
-[WiFiAnalyticsAWDWiFiDPSReport setDpsEpiloge:];
-[WiFiAnalyticsAWDWiFiDPSReport setProbeResults:];
-[WiFiAnalyticsAWDWiFiDPSReport setStallNotifications:];
-[WiFiAnalyticsAWDWiFiDPSReport setUsbEvents:];
-[WiFiAnalyticsAWDWiFiDPSReport stallNotificationAtIndex:];
-[WiFiAnalyticsAWDWiFiDPSReport stallNotifications];
-[WiFiAnalyticsAWDWiFiDPSReport stallNotificationsCount];
-[WiFiAnalyticsAWDWiFiDPSReport usbEventAtIndex:];
-[WiFiAnalyticsAWDWiFiDPSReport usbEvents];
-[WiFiAnalyticsAWDWiFiDPSReport usbEventsCount];
```
