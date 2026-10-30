# `EspressoDataFrameExecutor`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
{vector<void *, std::allocator<void *>>="__begin_"^^v"__end_"^^v""{?="__cap_"^^v}} pointers_to_free;
{vector<__CVBuffer *, std::allocator<__CVBuffer *>>="__begin_"^^{__CVBuffer}"__end_"^^{__CVBuffer}""{?="__cap_"^^{__CVBuffer}}} pixelbuffers_to_release;
i _use_cvpixelbuffer;
@"NSArray" _outputMatchingBuffers;
```

## Properties

```
@property (T@"NSArray",&,V_outputMatchingBuffers) outputMatchingBuffers;
@property (Ti,N,V_use_cvpixelbuffer) use_cvpixelbuffer;
```

## Instance methods

```
-[EspressoDataFrameExecutor dealloc];
-[EspressoDataFrameExecutor bindOutputsFromFrame:toNetwork:];
-[EspressoDataFrameExecutor bindInput:fromImageAttachment:toNetwork:];
-[EspressoDataFrameExecutor bindInput:fromTensorAttachment:toNetwork:];
-[EspressoDataFrameExecutor bindInputsFromFrame:toNetwork:];
-[EspressoDataFrameExecutor bindOutputsFromFrame:toNetwork:executionStatus:];
-[EspressoDataFrameExecutor bindOutputsFromFrame:toNetwork:referenceNetwork:];
-[EspressoDataFrameExecutor freeTemporaryResources];
-[EspressoDataFrameExecutor outputMatchingBuffers];
-[EspressoDataFrameExecutor setOutputMatchingBuffers:];
-[EspressoDataFrameExecutor setUse_cvpixelbuffer:];
-[EspressoDataFrameExecutor useCVPixelBuffers];
-[EspressoDataFrameExecutor useCVPixelBuffersForOutputs:];
-[EspressoDataFrameExecutor use_cvpixelbuffer];
```
