# `EGStillImageAdaptiveFusionRoutingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- 8 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _sampleBufferInputs;
@"EGStillImageOutput" _referenceEVZeroOutput;
@"NSMutableArray" _evZeroOutputs;
@"EGStillImageOutput" _evMinusOutput;
@"NSMutableArray" _longOutputs;
@"EGStillImageOutput" _hdrErrorRecoveryEVZeroOutput;
i _evZeroEmitIndex;
i _longEmitIndex;
```

## Properties

```
@property (T@"NSArray",R,N,V_sampleBufferInputs) sampleBufferInputs;
@property (T@"EGOutput",R,N,V_referenceEVZeroOutput) referenceEVZeroOutput;
@property (T@"EGOutput",R,N,V_evMinusOutput) evMinusOutput;
@property (T@"NSArray",R,N,V_evZeroOutputs) evZeroOutputs;
@property (T@"NSArray",R,N,V_longOutputs) longOutputs;
@property (T@"EGOutput",R,N,V_hdrErrorRecoveryEVZeroOutput) hdrErrorRecoveryEVZeroOutput;
```

## Class methods

```
+[EGStillImageAdaptiveFusionRoutingNode initialize];
```

## Instance methods

```
-[EGStillImageAdaptiveFusionRoutingNode dealloc];
-[EGStillImageAdaptiveFusionRoutingNode evMinusOutput];
-[EGStillImageAdaptiveFusionRoutingNode evZeroOutputs];
-[EGStillImageAdaptiveFusionRoutingNode hdrErrorRecoveryEVZeroOutput];
-[EGStillImageAdaptiveFusionRoutingNode initWithName:evZeroCount:hasEVMinus:longCount:hasHDRErrorRecoveryEVZero:];
-[EGStillImageAdaptiveFusionRoutingNode longOutputs];
-[EGStillImageAdaptiveFusionRoutingNode receiveData:fromInput:];
-[EGStillImageAdaptiveFusionRoutingNode referenceEVZeroOutput];
-[EGStillImageAdaptiveFusionRoutingNode sampleBufferInputs];
```
