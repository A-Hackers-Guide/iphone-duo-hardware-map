# `WiFiUsageLQMKernelSampleRxAmpdu`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 16 instance variables, 16 properties, 33 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _rxAmpdu;
Q _rxMpduDensity;
Q _rxBarOverRxAmpdu;
Q _rxQueuedOverRxAmpdu;
Q _rxAmpduAll;
Q _rxHoles;
Q _rxDup;
Q _rxStuck;
Q _rxOow;
Q _rxOos;
Q _rxAddBaReq;
Q _txAddBaResp;
Q _txDelBa;
Q _rxDelBa;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_rxAmpdu) rxAmpdu;
@property (TQ,N,V_rxMpduDensity) rxMpduDensity;
@property (TQ,N,V_rxBarOverRxAmpdu) rxBarOverRxAmpdu;
@property (TQ,N,V_rxQueuedOverRxAmpdu) rxQueuedOverRxAmpdu;
@property (TQ,N,V_rxAddBaReq) rxAddBaReq;
@property (TQ,N,V_txAddBaResp) txAddBaResp;
@property (TQ,N,V_txDelBa) txDelBa;
@property (TQ,N,V_rxDelBa) rxDelBa;
@property (TQ,N,V_rxAmpduAll) rxAmpduAll;
@property (TQ,N,V_rxHoles) rxHoles;
@property (TQ,N,V_rxDup) rxDup;
@property (TQ,N,V_rxStuck) rxStuck;
@property (TQ,N,V_rxOow) rxOow;
@property (TQ,N,V_rxOos) rxOos;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleRxAmpdu featureFromFieldName:];
+[WiFiUsageLQMKernelSampleRxAmpdu sampleWithStruct:WithReferenceDate:AsNsec:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleRxAmpdu setTimestamp:];
-[WiFiUsageLQMKernelSampleRxAmpdu timestamp];
-[WiFiUsageLQMKernelSampleRxAmpdu duration];
-[WiFiUsageLQMKernelSampleRxAmpdu setDuration:];
-[WiFiUsageLQMKernelSampleRxAmpdu rxAmpdu];
-[WiFiUsageLQMKernelSampleRxAmpdu rxHoles];
-[WiFiUsageLQMKernelSampleRxAmpdu setTxAddBaResp:];
-[WiFiUsageLQMKernelSampleRxAmpdu txDelBa];
-[WiFiUsageLQMKernelSampleRxAmpdu rxDelBa];
-[WiFiUsageLQMKernelSampleRxAmpdu rxStuck];
-[WiFiUsageLQMKernelSampleRxAmpdu initWithStruct:WithReferenceDate:AsNsec:];
-[WiFiUsageLQMKernelSampleRxAmpdu rxAddBaReq];
-[WiFiUsageLQMKernelSampleRxAmpdu rxAmpduAll];
-[WiFiUsageLQMKernelSampleRxAmpdu rxBarOverRxAmpdu];
-[WiFiUsageLQMKernelSampleRxAmpdu rxDup];
-[WiFiUsageLQMKernelSampleRxAmpdu rxMpduDensity];
-[WiFiUsageLQMKernelSampleRxAmpdu rxOos];
-[WiFiUsageLQMKernelSampleRxAmpdu rxOow];
-[WiFiUsageLQMKernelSampleRxAmpdu rxQueuedOverRxAmpdu];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxAddBaReq:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxAmpdu:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxAmpduAll:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxBarOverRxAmpdu:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxDelBa:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxDup:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxHoles:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxMpduDensity:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxOos:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxOow:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxQueuedOverRxAmpdu:];
-[WiFiUsageLQMKernelSampleRxAmpdu setRxStuck:];
-[WiFiUsageLQMKernelSampleRxAmpdu setTxDelBa:];
-[WiFiUsageLQMKernelSampleRxAmpdu txAddBaResp];
```
