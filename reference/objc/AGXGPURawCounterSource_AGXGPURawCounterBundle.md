# `AGXGPURawCounterSource`

- Image: [`/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle`](../userland/System__Library__Extensions__AGXGPURawCounterBundle.bundle__AGXGPURawCounterBundle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_GPURawCounterSource`
- 6 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
^{Source=^^?} _impl;
@"NSArray" _counterList;
@"NSArray" _selectedCounterList;
@"NSArray" _triggerList;
@"NSArray" _selectedTriggerList;
@"NSMutableArray" _pollPostProcessBufferList;
```

## Instance methods

```
-[AGXGPURawCounterSource setOptions:];
-[AGXGPURawCounterSource availableCounters];
-[AGXGPURawCounterSource dealloc];
-[AGXGPURawCounterSource isEnabled];
-[AGXGPURawCounterSource setEnabled:];
-[AGXGPURawCounterSource postProcessRawDataWithRingBufferIndex:source:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:];
-[AGXGPURawCounterSource requestCounter:];
-[AGXGPURawCounterSource availableTriggers];
-[AGXGPURawCounterSource drainRingBufferAtIndex:dataSize:];
-[AGXGPURawCounterSource flushRingBuffers];
-[AGXGPURawCounterSource initWithSourceGroup:impl:];
-[AGXGPURawCounterSource pollCountersAtBufferIndex:withBlock:];
-[AGXGPURawCounterSource postProcessRawDataWithRingBufferSource:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:];
-[AGXGPURawCounterSource postProcessRawDataWithSource:sourceSize:sourceRead:output:outputSize:outputWritten:isLast:];
-[AGXGPURawCounterSource requestCounters:firstErrorIndex:];
-[AGXGPURawCounterSource requestTriggers:firstErrorIndex:];
-[AGXGPURawCounterSource resetRawDataPostProcessor];
-[AGXGPURawCounterSource ringBufferInfoAtIndex:base:size:dataOffset:dataSize:];
-[AGXGPURawCounterSource ringBufferNum];
-[AGXGPURawCounterSource selectedCounters];
-[AGXGPURawCounterSource selectedTriggers];
```
