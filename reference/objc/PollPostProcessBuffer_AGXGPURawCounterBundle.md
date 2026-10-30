# `PollPostProcessBuffer`

- Image: [`/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle`](../userland/System__Library__Extensions__AGXGPURawCounterBundle.bundle__AGXGPURawCounterBundle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _srcBufferPrevOffset;
I _srcBufferPrevSize;
@"NSMutableData" _dstBuffer;
```

## Properties

```
@property (TI,V_srcBufferPrevOffset) srcBufferPrevOffset;
@property (TI,V_srcBufferPrevSize) srcBufferPrevSize;
@property (T@"NSMutableData",R,V_dstBuffer) dstBuffer;
```

## Instance methods

```
-[PollPostProcessBuffer init];
-[PollPostProcessBuffer dealloc];
-[PollPostProcessBuffer reset];
-[PollPostProcessBuffer dstBuffer];
-[PollPostProcessBuffer setSrcBufferPrevOffset:];
-[PollPostProcessBuffer setSrcBufferPrevSize:];
-[PollPostProcessBuffer srcBufferPrevOffset];
-[PollPostProcessBuffer srcBufferPrevSize];
```
