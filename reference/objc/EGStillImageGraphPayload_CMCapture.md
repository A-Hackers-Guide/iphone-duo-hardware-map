# `EGStillImageGraphPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
@ _payload;
i _type;
```

## Properties

```
@property (Ti,R,N,V_type) type;
@property (T^{opaqueCMSampleBuffer=},R,N) sampleBuffer;
@property (T@"BWStillImageProcessorController",R,N) processorController;
@property (T@"BWStillImageInferences",R,N) stillImageInferences;
@property (T@"NSNumber",R,N) number;
@property (T@"NSDictionary",R,N) dictionary;
```

## Class methods

```
+[EGStillImageGraphPayload initialize];
```

## Instance methods

```
-[EGStillImageGraphPayload debugDescription];
-[EGStillImageGraphPayload initWithDictionary:];
-[EGStillImageGraphPayload dealloc];
-[EGStillImageGraphPayload dictionary];
-[EGStillImageGraphPayload number];
-[EGStillImageGraphPayload initWithSampleBuffer:];
-[EGStillImageGraphPayload type];
-[EGStillImageGraphPayload initWithNumber:];
-[EGStillImageGraphPayload description];
-[EGStillImageGraphPayload sampleBuffer];
-[EGStillImageGraphPayload initWithEmptyPayload];
-[EGStillImageGraphPayload initWithProcessorController:];
-[EGStillImageGraphPayload initWithStillImageInferences:];
-[EGStillImageGraphPayload processorController];
-[EGStillImageGraphPayload stillImageInferences];
```
