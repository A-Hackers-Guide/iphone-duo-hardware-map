# `PLNetworkUsageSnapshot`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _timestamp;
@"NSString" _cellType;
@"NSString" _quality;
@"NSString" _wifi;
```

## Properties

```
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (T@"NSString",&,V_cellType) cellType;
@property (T@"NSString",&,V_quality) quality;
@property (T@"NSString",&,V_wifi) wifi;
```

## Instance methods

```
-[PLNetworkUsageSnapshot cellType];
-[PLNetworkUsageSnapshot quality];
-[PLNetworkUsageSnapshot setTimestamp:];
-[PLNetworkUsageSnapshot setQuality:];
-[PLNetworkUsageSnapshot setWifi:];
-[PLNetworkUsageSnapshot timestamp];
-[PLNetworkUsageSnapshot initWithInfo:];
-[PLNetworkUsageSnapshot setCellType:];
-[PLNetworkUsageSnapshot description];
-[PLNetworkUsageSnapshot wifi];
-[PLNetworkUsageSnapshot computeEnergyDiff:];
-[PLNetworkUsageSnapshot computeEnergyDiffUntilNow:];
-[PLNetworkUsageSnapshot snapshotNetworkState];
```
