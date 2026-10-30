# `EGStillImageSampleBufferEmitterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- 3 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _description;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _captureCompleteOutput;
```

## Properties

```
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_captureCompleteOutput) captureCompleteOutput;
```

## Class methods

```
+[EGStillImageSampleBufferEmitterNode initialize];
```

## Instance methods

```
-[EGStillImageSampleBufferEmitterNode dealloc];
-[EGStillImageSampleBufferEmitterNode initWithName:description:];
-[EGStillImageSampleBufferEmitterNode captureCompleteOutput];
-[EGStillImageSampleBufferEmitterNode receiveData:fromInput:];
-[EGStillImageSampleBufferEmitterNode sbufInput];
```
