# `BWMetalInferenceContext`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"<MTLCommandQueue>" _commandQueue;
@"<MTLDevice>" _device;
@"NSArray" _previewCommandQueues;
@"BWInferenceScheduler" _weakInferenceScheduler;
I _contextPriority;
```

## Properties

```
@property (T@"<MTLCommandQueue>",R,N,V_commandQueue) commandQueue;
@property (T@"<MTLDevice>",R,N,V_device) device;
```

## Class methods

```
+[BWMetalInferenceContext initialize];
```

## Instance methods

```
-[BWMetalInferenceContext newCommandQueue];
-[BWMetalInferenceContext initWithScheduler:priority:];
-[BWMetalInferenceContext device];
-[BWMetalInferenceContext dealloc];
-[BWMetalInferenceContext commandQueue];
-[BWMetalInferenceContext commandQueueUsingStorage:];
-[BWMetalInferenceContext newLowLatencyCommandQueue];
```
