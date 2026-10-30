# `WiFiUsageLQMKernelSamplePerACTxStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
```

## Properties

```
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSamplePerACTxStats sampleWithTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSamplePerACTxStats timestamp];
-[WiFiUsageLQMKernelSamplePerACTxStats duration];
-[WiFiUsageLQMKernelSamplePerACTxStats initWithTimestamp:];
-[WiFiUsageLQMKernelSamplePerACTxStats description];
-[WiFiUsageLQMKernelSamplePerACTxStats setDuration:];
-[WiFiUsageLQMKernelSamplePerACTxStats populateTXStats:With:ForQueue:];
-[WiFiUsageLQMKernelSamplePerACTxStats transformTXStats];
```
