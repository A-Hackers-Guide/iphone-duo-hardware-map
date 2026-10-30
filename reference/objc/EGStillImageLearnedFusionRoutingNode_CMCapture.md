# `EGStillImageLearnedFusionRoutingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- 5 instance variables, 5 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _sampleBufferInputs;
@"EGStillImageOutput" _evZeroOutput;
@"EGStillImageOutput" _longOutput;
@"EGStillImageOutput" _evMinusOutput;
@"EGStillImageOutput" _secondEvZeroOutput;
```

## Properties

```
@property (T@"NSArray",R,N,V_sampleBufferInputs) sampleBufferInputs;
@property (T@"EGOutput",R,N,V_evZeroOutput) evZeroOutput;
@property (T@"EGOutput",R,N,V_longOutput) longOutput;
@property (T@"EGOutput",R,N,V_evMinusOutput) evMinusOutput;
@property (T@"EGOutput",R,N,V_secondEvZeroOutput) secondEvZeroOutput;
```

## Class methods

```
+[EGStillImageLearnedFusionRoutingNode initialize];
```

## Instance methods

```
-[EGStillImageLearnedFusionRoutingNode dealloc];
-[EGStillImageLearnedFusionRoutingNode evMinusOutput];
-[EGStillImageLearnedFusionRoutingNode evZeroOutput];
-[EGStillImageLearnedFusionRoutingNode initWithName:numSampleBufferInputs:];
-[EGStillImageLearnedFusionRoutingNode longOutput];
-[EGStillImageLearnedFusionRoutingNode receiveData:fromInput:];
-[EGStillImageLearnedFusionRoutingNode sampleBufferInputs];
-[EGStillImageLearnedFusionRoutingNode secondEvZeroOutput];
```
