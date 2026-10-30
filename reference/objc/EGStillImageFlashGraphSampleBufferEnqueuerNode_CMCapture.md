# `EGStillImageFlashGraphSampleBufferEnqueuerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- Protocols: `EGStillImageGraphSampleBufferEntryPoint`
- 4 instance variables, 7 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"EGStillImageOutput" _primaryAmbientSbufOutput;
@"EGStillImageOutput" _primaryFlashSbufOutput;
@"EGStillImageOutput" _secondaryFlashSbufOutput;
@"BWStillImageSettings" _stillImageSettings;
```

## Properties

```
@property (T@"EGOutput",R,N,V_primaryAmbientSbufOutput) primaryAmbientSbufOutput;
@property (T@"EGOutput",R,N,V_primaryFlashSbufOutput) primaryFlashSbufOutput;
@property (T@"EGOutput",R,N,V_secondaryFlashSbufOutput) secondaryFlashSbufOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageFlashGraphSampleBufferEnqueuerNode initialize];
```

## Instance methods

```
-[EGStillImageFlashGraphSampleBufferEnqueuerNode dealloc];
-[EGStillImageFlashGraphSampleBufferEnqueuerNode enqueueSampleBuffer:];
-[EGStillImageFlashGraphSampleBufferEnqueuerNode initWithName:stillImageSettings:];
-[EGStillImageFlashGraphSampleBufferEnqueuerNode primaryAmbientSbufOutput];
-[EGStillImageFlashGraphSampleBufferEnqueuerNode primaryFlashSbufOutput];
-[EGStillImageFlashGraphSampleBufferEnqueuerNode secondaryFlashSbufOutput];
```
