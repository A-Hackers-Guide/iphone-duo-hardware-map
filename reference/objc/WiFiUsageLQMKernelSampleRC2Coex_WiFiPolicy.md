# `WiFiUsageLQMKernelSampleRC2Coex`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _rc2DurationPerc;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_rc2DurationPerc) rc2DurationPerc;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleRC2Coex sampleWithStruct:andTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleRC2Coex setTimestamp:];
-[WiFiUsageLQMKernelSampleRC2Coex timestamp];
-[WiFiUsageLQMKernelSampleRC2Coex duration];
-[WiFiUsageLQMKernelSampleRC2Coex setDuration:];
-[WiFiUsageLQMKernelSampleRC2Coex rc2DurationPerc];
-[WiFiUsageLQMKernelSampleRC2Coex initWithStruct:andTimestamp:];
-[WiFiUsageLQMKernelSampleRC2Coex setRc2DurationPerc:];
```
