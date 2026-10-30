# `WiFiUsageLQMKernelSampleSecurityErrors`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 6 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _rxUcastReplayError;
Q _rxucastDecryptError;
Q _rxmcastReplayError;
Q _rxmcastDecryptError;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_rxUcastReplayError) rxUcastReplayError;
@property (TQ,N,V_rxucastDecryptError) rxucastDecryptError;
@property (TQ,N,V_rxmcastReplayError) rxmcastReplayError;
@property (TQ,N,V_rxmcastDecryptError) rxmcastDecryptError;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleSecurityErrors featureFromFieldName:];
+[WiFiUsageLQMKernelSampleSecurityErrors sampleWithStruct:andTimestamp:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleSecurityErrors setTimestamp:];
-[WiFiUsageLQMKernelSampleSecurityErrors timestamp];
-[WiFiUsageLQMKernelSampleSecurityErrors duration];
-[WiFiUsageLQMKernelSampleSecurityErrors setDuration:];
-[WiFiUsageLQMKernelSampleSecurityErrors initWithStruct:andTimestamp:];
-[WiFiUsageLQMKernelSampleSecurityErrors rxUcastReplayError];
-[WiFiUsageLQMKernelSampleSecurityErrors rxmcastDecryptError];
-[WiFiUsageLQMKernelSampleSecurityErrors rxmcastReplayError];
-[WiFiUsageLQMKernelSampleSecurityErrors rxucastDecryptError];
-[WiFiUsageLQMKernelSampleSecurityErrors setRxUcastReplayError:];
-[WiFiUsageLQMKernelSampleSecurityErrors setRxmcastDecryptError:];
-[WiFiUsageLQMKernelSampleSecurityErrors setRxmcastReplayError:];
-[WiFiUsageLQMKernelSampleSecurityErrors setRxucastDecryptError:];
```
