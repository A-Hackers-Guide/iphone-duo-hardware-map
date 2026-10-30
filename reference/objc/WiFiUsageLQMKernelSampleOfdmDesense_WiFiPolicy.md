# `WiFiUsageLQMKernelSampleOfdmDesense`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 5 instance variables, 5 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _ofdmDesense;
Q _bPhyDesense;
@"NSString" _desenseReason;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_ofdmDesense) ofdmDesense;
@property (TQ,N,V_bPhyDesense) bPhyDesense;
@property (T@"NSString",&,N,V_desenseReason) desenseReason;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleOfdmDesense allLQMProperties];
+[WiFiUsageLQMKernelSampleOfdmDesense featureFromFieldName:];
+[WiFiUsageLQMKernelSampleOfdmDesense sampleWithStruct:andTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleOfdmDesense setTimestamp:];
-[WiFiUsageLQMKernelSampleOfdmDesense timestamp];
-[WiFiUsageLQMKernelSampleOfdmDesense setOfdmDesense:];
-[WiFiUsageLQMKernelSampleOfdmDesense duration];
-[WiFiUsageLQMKernelSampleOfdmDesense ofdmDesense];
-[WiFiUsageLQMKernelSampleOfdmDesense setDuration:];
-[WiFiUsageLQMKernelSampleOfdmDesense setBPhyDesense:];
-[WiFiUsageLQMKernelSampleOfdmDesense bPhyDesense];
-[WiFiUsageLQMKernelSampleOfdmDesense desenseReason];
-[WiFiUsageLQMKernelSampleOfdmDesense initWithStruct:andTimestamp:];
-[WiFiUsageLQMKernelSampleOfdmDesense setDesenseReason:];
```
