# `MTLCountersTraceCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _timer;
^{BinaryBuffer=^^?{StreamBuffer=***}{mach_timebase_info=II}} _stream;
Q _flags;
{_NSRange="location"Q"length"Q} _segment;
```

## Properties

```
@property (TQ,R,N,V_flags) flags;
@property (T{_NSRange=QQ},R,N,V_segment) segment;
```

## Instance methods

```
-[MTLCountersTraceCommandEncoder insertDebugSignpost:];
-[MTLCountersTraceCommandEncoder pushDebugGroup:];
-[MTLCountersTraceCommandEncoder popDebugGroup];
-[MTLCountersTraceCommandEncoder flags];
-[MTLCountersTraceCommandEncoder setLabel:];
-[MTLCountersTraceCommandEncoder endEncoding];
-[MTLCountersTraceCommandEncoder segment];
-[MTLCountersTraceCommandEncoder init:flags:];
```
