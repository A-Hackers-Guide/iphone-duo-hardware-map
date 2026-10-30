# `WiFiAnalyticsAWDWiFiSlowWiFiReport`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 6 properties, 28 instance methods, 2 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _linkQualSamples;
@"WiFiAnalyticsAWDSlowWiFiNotification" _slowNotice;
@"NSMutableArray" _usbEvents;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,R,N) hasSlowNotice;
@property (T@"WiFiAnalyticsAWDSlowWiFiNotification",&,N,V_slowNotice) slowNotice;
@property (T@"NSMutableArray",&,N,V_linkQualSamples) linkQualSamples;
@property (T@"NSMutableArray",&,N,V_usbEvents) usbEvents;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiSlowWiFiReport linkQualSampleType];
+[WiFiAnalyticsAWDWiFiSlowWiFiReport usbEventType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiSlowWiFiReport hasTimestamp];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport setTimestamp:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport writeTo:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport mergeFrom:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport timestamp];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport hash];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport copyTo:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport description];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport readFrom:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport copyWithZone:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport isEqual:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport linkQualSamples];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport addLinkQualSample:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport addUsbEvent:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport clearLinkQualSamples];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport clearUsbEvents];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport hasSlowNotice];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport linkQualSampleAtIndex:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport linkQualSamplesCount];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport setLinkQualSamples:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport setSlowNotice:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport setUsbEvents:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport slowNotice];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport usbEventAtIndex:];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport usbEvents];
-[WiFiAnalyticsAWDWiFiSlowWiFiReport usbEventsCount];
```
