# `EGStillImageSampleBufferEnqueuerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- Protocols: `EGStillImageGraphSampleBufferEntryPoint`
- 5 instance variables, 6 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _primarySbufOutputs;
@"NSMutableArray" _secondarySbufOutputs;
@"NSString" _primaryPortType;
i _primarySbufCount;
i _secondarySbufCount;
```

## Properties

```
@property (T@"NSArray",R,N,V_primarySbufOutputs) primarySbufOutputs;
@property (T@"NSArray",R,N,V_secondarySbufOutputs) secondarySbufOutputs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageSampleBufferEnqueuerNode initialize];
```

## Instance methods

```
-[EGStillImageSampleBufferEnqueuerNode dealloc];
-[EGStillImageSampleBufferEnqueuerNode enqueueSampleBuffer:];
-[EGStillImageSampleBufferEnqueuerNode initWithName:primaryPortType:numPrimarySbufOutputs:numSecondarySbufOutputs:stillImageSettings:];
-[EGStillImageSampleBufferEnqueuerNode primarySbufOutputs];
-[EGStillImageSampleBufferEnqueuerNode secondarySbufOutputs];
```
