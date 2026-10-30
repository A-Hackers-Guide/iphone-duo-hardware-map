# `WiFiUsageLQMKernelSampleScanSummary`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 4 instance variables, 4 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _scanDurationMS;
@"NSString" _scanClient;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_scanDurationMS) scanDurationMS;
@property (T@"NSString",&,N,V_scanClient) scanClient;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleScanSummary allLQMProperties];
+[WiFiUsageLQMKernelSampleScanSummary featureFromFieldName:];
+[WiFiUsageLQMKernelSampleScanSummary sampleWithStruct:andTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleScanSummary setTimestamp:];
-[WiFiUsageLQMKernelSampleScanSummary timestamp];
-[WiFiUsageLQMKernelSampleScanSummary duration];
-[WiFiUsageLQMKernelSampleScanSummary setDuration:];
-[WiFiUsageLQMKernelSampleScanSummary initWithStruct:andTimestamp:];
-[WiFiUsageLQMKernelSampleScanSummary scanClient];
-[WiFiUsageLQMKernelSampleScanSummary scanDurationMS];
-[WiFiUsageLQMKernelSampleScanSummary setScanClient:];
-[WiFiUsageLQMKernelSampleScanSummary setScanDurationMS:];
```
