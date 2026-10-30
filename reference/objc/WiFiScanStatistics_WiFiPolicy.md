# `WiFiScanStatistics`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 18 properties, 44 instance methods, 0 class methods

## Instance variables

```
i _err;
Q _client;
Q _successCount;
Q _failureCount;
Q _is2GScan;
Q _is2GScanScanCore;
Q _is5GScan;
Q _is5GScanScanCore;
Q _is6GScan;
Q _is6GScanScanCore;
Q _scanDuration2G;
Q _scanDuration5G;
Q _scanDuration6G;
Q _scanCore2GScanDuration;
Q _scanCore5GScanDuration;
Q _scanCore6GScanDuration;
Q _scanDurationAllBands;
Q _scanCoreScanDurationAllBands;
```

## Properties

```
@property (TQ,N,V_client) client;
@property (Ti,N,V_err) err;
@property (TQ,N,V_successCount) successCount;
@property (TQ,N,V_failureCount) failureCount;
@property (TQ,N,V_is2GScan) is2GScan;
@property (TQ,N,V_is2GScanScanCore) is2GScanScanCore;
@property (TQ,N,V_is5GScan) is5GScan;
@property (TQ,N,V_is5GScanScanCore) is5GScanScanCore;
@property (TQ,N,V_is6GScan) is6GScan;
@property (TQ,N,V_is6GScanScanCore) is6GScanScanCore;
@property (TQ,N,V_scanDuration2G) scanDuration2G;
@property (TQ,N,V_scanDuration5G) scanDuration5G;
@property (TQ,N,V_scanDuration6G) scanDuration6G;
@property (TQ,N,V_scanCore2GScanDuration) scanCore2GScanDuration;
@property (TQ,N,V_scanCore5GScanDuration) scanCore5GScanDuration;
@property (TQ,N,V_scanCore6GScanDuration) scanCore6GScanDuration;
@property (TQ,N,V_scanDurationAllBands) scanDurationAllBands;
@property (TQ,N,V_scanCoreScanDurationAllBands) scanCoreScanDurationAllBands;
```

## Instance methods

```
-[WiFiScanStatistics failureCount];
-[WiFiScanStatistics setFailureCount:];
-[WiFiScanStatistics add:with:];
-[WiFiScanStatistics initForClient:];
-[WiFiScanStatistics is6GScanScanCore];
-[WiFiScanStatistics gatherDataToBePosted:];
-[WiFiScanStatistics setScanDurationAllBands:];
-[WiFiScanStatistics setScanCore2GScanDuration:];
-[WiFiScanStatistics setErr:];
-[WiFiScanStatistics successCount];
-[WiFiScanStatistics scanDuration5G];
-[WiFiScanStatistics setScanCore5GScanDuration:];
-[WiFiScanStatistics is5GScanScanCore];
-[WiFiScanStatistics reset];
-[WiFiScanStatistics setIs6GScan:];
-[WiFiScanStatistics setScanCore6GScanDuration:];
-[WiFiScanStatistics setSuccessCount:];
-[WiFiScanStatistics postIndividualScanMetricsToCA];
-[WiFiScanStatistics setClient:];
-[WiFiScanStatistics aggregateValues:];
-[WiFiScanStatistics is2GScanScanCore];
-[WiFiScanStatistics scanCore5GScanDuration];
-[WiFiScanStatistics scanDuration6G];
-[WiFiScanStatistics scanDurationAllBands];
-[WiFiScanStatistics err];
-[WiFiScanStatistics is5GScan];
-[WiFiScanStatistics postDailyScanMetricsToCA];
-[WiFiScanStatistics twoSigFig:];
-[WiFiScanStatistics setScanDuration2G:];
-[WiFiScanStatistics scanCore2GScanDuration];
-[WiFiScanStatistics scanDuration2G];
-[WiFiScanStatistics scanCore6GScanDuration];
-[WiFiScanStatistics setIs5GScan:];
-[WiFiScanStatistics setIs2GScan:];
-[WiFiScanStatistics setScanDuration6G:];
-[WiFiScanStatistics client];
-[WiFiScanStatistics setIs2GScanScanCore:];
-[WiFiScanStatistics is2GScan];
-[WiFiScanStatistics setIs6GScanScanCore:];
-[WiFiScanStatistics is6GScan];
-[WiFiScanStatistics setScanCoreScanDurationAllBands:];
-[WiFiScanStatistics setIs5GScanScanCore:];
-[WiFiScanStatistics setScanDuration5G:];
-[WiFiScanStatistics scanCoreScanDurationAllBands];
```
