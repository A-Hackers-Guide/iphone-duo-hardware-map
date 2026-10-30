# `WiFiUsageLQMKernelSampleCCA`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 11 instance variables, 11 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _selfCca;
Q _otherCca;
Q _interference;
Q _selfCcaSleepPerc;
Q _otherCcaSleepPerc;
Q _interferenceSleepPerc;
Q _selfCcaWakePerc;
Q _otherCcaWakePerc;
Q _interferenceWakePerc;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (Td,N,V_duration) duration;
@property (TQ,R,N,V_selfCca) selfCca;
@property (TQ,R,N,V_otherCca) otherCca;
@property (TQ,R,N,V_interference) interference;
@property (TQ,R,N,V_selfCcaSleepPerc) selfCcaSleepPerc;
@property (TQ,R,N,V_otherCcaSleepPerc) otherCcaSleepPerc;
@property (TQ,R,N,V_interferenceSleepPerc) interferenceSleepPerc;
@property (TQ,R,N,V_selfCcaWakePerc) selfCcaWakePerc;
@property (TQ,R,N,V_otherCcaWakePerc) otherCcaWakePerc;
@property (TQ,R,N,V_interferenceWakePerc) interferenceWakePerc;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleCCA sampleWithStruct:andTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleCCA otherCca];
-[WiFiUsageLQMKernelSampleCCA setTimestamp:];
-[WiFiUsageLQMKernelSampleCCA timestamp];
-[WiFiUsageLQMKernelSampleCCA selfCca];
-[WiFiUsageLQMKernelSampleCCA duration];
-[WiFiUsageLQMKernelSampleCCA interference];
-[WiFiUsageLQMKernelSampleCCA setDuration:];
-[WiFiUsageLQMKernelSampleCCA selfCcaWakePerc];
-[WiFiUsageLQMKernelSampleCCA initWithStruct:andTimestamp:];
-[WiFiUsageLQMKernelSampleCCA interferenceSleepPerc];
-[WiFiUsageLQMKernelSampleCCA interferenceWakePerc];
-[WiFiUsageLQMKernelSampleCCA otherCcaSleepPerc];
-[WiFiUsageLQMKernelSampleCCA otherCcaWakePerc];
-[WiFiUsageLQMKernelSampleCCA selfCcaSleepPerc];
```
