# `WiFiUsageConnectionQualityRecord`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 3 class methods

## Instance variables

```
B _dryRunMode;
@"GEOWiFiConnectionQuality" _geoMessage;
@"NSString" _identifier;
```

## Properties

```
@property (T@"GEOWiFiConnectionQuality",&,N,V_geoMessage) geoMessage;
@property (T@"NSString",&,N,V_identifier) identifier;
@property (TB,N,V_dryRunMode) dryRunMode;
```

## Class methods

```
+[WiFiUsageConnectionQualityRecord _deviceHWIdentifier];
+[WiFiUsageConnectionQualityRecord _geoFormattedDeviceOSVersion];
+[WiFiUsageConnectionQualityRecord _geoFormattedOSVersion];
```

## Instance methods

```
-[WiFiUsageConnectionQualityRecord identifier];
-[WiFiUsageConnectionQualityRecord setIdentifier:];
-[WiFiUsageConnectionQualityRecord _writeGeoMessageToIPS];
-[WiFiUsageConnectionQualityRecord dryRunMode];
-[WiFiUsageConnectionQualityRecord geoMessage];
-[WiFiUsageConnectionQualityRecord initWithUsageSession:andNeighborBssList:andOtherBssList:];
-[WiFiUsageConnectionQualityRecord queryNetworkPerformanceFeedAndSubmitToGeoWiFi];
-[WiFiUsageConnectionQualityRecord setDryRunMode:];
-[WiFiUsageConnectionQualityRecord setGeoMessage:];
```
