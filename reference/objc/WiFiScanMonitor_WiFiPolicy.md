# `WiFiScanMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"WiFiScanStatisticsAggregator" _scanAggregator;
```

## Properties

```
@property (T@"WiFiScanStatisticsAggregator",&,N,V_scanAggregator) scanAggregator;
```

## Class methods

```
+[WiFiScanMonitor sharedScanMonitor];
```

## Instance methods

```
-[WiFiScanMonitor init];
-[WiFiScanMonitor gatherScanStatisticsForClient:error:is2GScan:is2GScanScanCore:is5GScan:is5GScanScanCore:is6GScan:is6GScanScanCore:scanDuration2G:scanDuration5G:scanDuration6G:scanCore2GScanDuration:scanCore5GScanDuration:scanCore6GScanDuration:];
-[WiFiScanMonitor scanAggregator];
-[WiFiScanMonitor setScanAggregator:];
```
