# `BWStillImageConditionalRouterConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _numberOfOutputs;
@? _shouldEmitSampleBufferDecisionProvider;
@? _shouldEmitNodeErrorDecisionProvider;
I _numberOfInputs;
```

## Properties

```
@property (TI,R,N,V_numberOfInputs) numberOfInputs;
@property (TI,R,N,V_numberOfOutputs) numberOfOutputs;
@property (T@?,C,N,V_shouldEmitSampleBufferDecisionProvider) shouldEmitSampleBufferDecisionProvider;
@property (T@?,C,N,V_shouldEmitNodeErrorDecisionProvider) shouldEmitNodeErrorDecisionProvider;
```

## Instance methods

```
-[BWStillImageConditionalRouterConfiguration dealloc];
-[BWStillImageConditionalRouterConfiguration numberOfOutputs];
-[BWStillImageConditionalRouterConfiguration initWithNumberOfOutputs:];
-[BWStillImageConditionalRouterConfiguration numberOfInputs];
-[BWStillImageConditionalRouterConfiguration setShouldEmitNodeErrorDecisionProvider:];
-[BWStillImageConditionalRouterConfiguration setShouldEmitSampleBufferDecisionProvider:];
-[BWStillImageConditionalRouterConfiguration shouldEmitNodeErrorDecisionProvider];
-[BWStillImageConditionalRouterConfiguration shouldEmitSampleBufferDecisionProvider];
```
