# `WiFiUsageLQMKernelSampleBTCoex`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _btAntennaDurationPerc;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_btAntennaDurationPerc) btAntennaDurationPerc;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleBTCoex sampleWithStruct:andTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleBTCoex setTimestamp:];
-[WiFiUsageLQMKernelSampleBTCoex timestamp];
-[WiFiUsageLQMKernelSampleBTCoex duration];
-[WiFiUsageLQMKernelSampleBTCoex setDuration:];
-[WiFiUsageLQMKernelSampleBTCoex btAntennaDurationPerc];
-[WiFiUsageLQMKernelSampleBTCoex initWithStruct:andTimestamp:];
-[WiFiUsageLQMKernelSampleBTCoex setBtAntennaDurationPerc:];
```
