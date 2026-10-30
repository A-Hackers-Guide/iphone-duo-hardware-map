# `BWRenderListProcessor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _configurationMutexQueue;
@"NSObject<OS_dispatch_group>" _renderingGroup;
@"BWRenderListProcessorPixelBufferJuggler" _bufferJuggler;
^{opaqueCMFormatDescription=} _mostRecentFormatDescription;
B _nextInputBufferRetainedExternally;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (TB,N,V_nextInputBufferRetainedExternally) nextInputBufferRetainedExternally;
```

## Class methods

```
+[BWRenderListProcessor initialize];
```

## Instance methods

```
-[BWRenderListProcessor dealloc];
-[BWRenderListProcessor name];
-[BWRenderListProcessor initWithName:];
-[BWRenderListProcessor adjustMetadataOfSampleBuffer:usingRenderList:];
-[BWRenderListProcessor nextInputBufferRetainedExternally];
-[BWRenderListProcessor processRenderList:inputPixelBuffer:inputSampleBuffer:pixelBufferProvider:resultHandler:];
-[BWRenderListProcessor processRenderList:withParameters:inputPixelBuffer:inputSampleBuffer:pixelBufferProvider:resultHandler:];
-[BWRenderListProcessor setNextInputBufferRetainedExternally:];
-[BWRenderListProcessor waitForAllProcessingToComplete];
```
