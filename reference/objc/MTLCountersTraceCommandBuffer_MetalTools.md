# `MTLCountersTraceCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
{BinaryBuffer="_vptr$AppendBuffer"^^?"stream"{StreamBuffer="bytes"*"pWrite"*"pEnd"*}"_timebase"{mach_timebase_info="numer"I"denom"I}} _commands;
@"NSMutableArray" _encoders;
{AppendBuffer="_vptr$AppendBuffer"^^?"stream"{StreamBuffer="bytes"*"pWrite"*"pEnd"*}} _samples;
Q _flags;
Q _timestamp;
```

## Instance methods

```
-[MTLCountersTraceCommandBuffer waitUntilScheduled];
-[MTLCountersTraceCommandBuffer waitUntilCompleted];
-[MTLCountersTraceCommandBuffer presentDrawable:];
-[MTLCountersTraceCommandBuffer presentDrawable:atTime:];
-[MTLCountersTraceCommandBuffer computeCommandEncoder];
-[MTLCountersTraceCommandBuffer dealloc];
-[MTLCountersTraceCommandBuffer init:];
-[MTLCountersTraceCommandBuffer blitCommandEncoder];
-[MTLCountersTraceCommandBuffer resourceStateCommandEncoder];
-[MTLCountersTraceCommandBuffer renderCommandEncoder];
-[MTLCountersTraceCommandBuffer appendSamples:length:];
-[MTLCountersTraceCommandBuffer saveCommandBuffer:queue:profilingResults:];
```
