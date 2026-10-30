# `SLAInterfaceStats`

- Image: [`/System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim`](../userland/System__Library__PrivateFrameworks__SymptomLinkAdvisoryAOPShim.framework__SymptomLinkAdvisoryAOPShim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
S _activeFlowCount;
S _connProbeFailureCount;
S _readProbeFailureCount;
S _writeProbeFailureCount;
Q _txBytes;
Q _rxBytes;
@"NSNumber" _avgRTTMs;
@"NSNumber" _minRTTMs;
@"NSNumber" _maxRTTVarianceMs;
Q _retransmittedBytes;
Q _duplicateBytes;
Q _outOfOrderBytes;
```

## Properties

```
@property (TQ,N,V_txBytes) txBytes;
@property (TQ,N,V_rxBytes) rxBytes;
@property (TS,N,V_activeFlowCount) activeFlowCount;
@property (T@"NSNumber",&,N,V_avgRTTMs) avgRTTMs;
@property (T@"NSNumber",&,N,V_minRTTMs) minRTTMs;
@property (T@"NSNumber",&,N,V_maxRTTVarianceMs) maxRTTVarianceMs;
@property (TQ,N,V_retransmittedBytes) retransmittedBytes;
@property (TQ,N,V_duplicateBytes) duplicateBytes;
@property (TQ,N,V_outOfOrderBytes) outOfOrderBytes;
@property (TS,N,V_connProbeFailureCount) connProbeFailureCount;
@property (TS,N,V_readProbeFailureCount) readProbeFailureCount;
@property (TS,N,V_writeProbeFailureCount) writeProbeFailureCount;
```

## Instance methods

```
-[SLAInterfaceStats setTxBytes:];
-[SLAInterfaceStats setRxBytes:];
-[SLAInterfaceStats init];
-[SLAInterfaceStats rxBytes];
-[SLAInterfaceStats txBytes];
-[SLAInterfaceStats setActiveFlowCount:];
-[SLAInterfaceStats setAvgRTTMs:];
-[SLAInterfaceStats setConnProbeFailureCount:];
-[SLAInterfaceStats setDuplicateBytes:];
-[SLAInterfaceStats setMaxRTTVarianceMs:];
-[SLAInterfaceStats setMinRTTMs:];
-[SLAInterfaceStats setOutOfOrderBytes:];
-[SLAInterfaceStats setReadProbeFailureCount:];
-[SLAInterfaceStats setRetransmittedBytes:];
-[SLAInterfaceStats setWriteProbeFailureCount:];
-[SLAInterfaceStats activeFlowCount];
-[SLAInterfaceStats outOfOrderBytes];
-[SLAInterfaceStats avgRTTMs];
-[SLAInterfaceStats connProbeFailureCount];
-[SLAInterfaceStats duplicateBytes];
-[SLAInterfaceStats maxRTTVarianceMs];
-[SLAInterfaceStats minRTTMs];
-[SLAInterfaceStats readProbeFailureCount];
-[SLAInterfaceStats retransmittedBytes];
-[SLAInterfaceStats writeProbeFailureCount];
```
