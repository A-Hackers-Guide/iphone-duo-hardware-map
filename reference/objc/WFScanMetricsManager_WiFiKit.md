# `WFScanMetricsManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _submited;
@"NSMutableDictionary" _sectionCounts;
@"NSDate" _timestamp;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_sectionCounts) sectionCounts;
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TB,N,V_submited) submited;
```

## Instance methods

```
-[WFScanMetricsManager setTimestamp:];
-[WFScanMetricsManager init];
-[WFScanMetricsManager submit];
-[WFScanMetricsManager timestamp];
-[WFScanMetricsManager reset];
-[WFScanMetricsManager ingestScanResults:];
-[WFScanMetricsManager sectionCounts];
-[WFScanMetricsManager sectionNameForRecord:];
-[WFScanMetricsManager setSectionCounts:];
-[WFScanMetricsManager setSubmited:];
-[WFScanMetricsManager submited];
```
