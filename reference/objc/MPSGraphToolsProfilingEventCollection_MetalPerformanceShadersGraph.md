# `MPSGraphToolsProfilingEventCollection`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 6 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
{vector<std::unique_ptr<std::vector<mpsgraph_tools_profiling_event_t>>, std::allocator<std::unique_ptr<std::vector<mpsgraph_tools_profiling_event_t>>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _eventVectors;
{vector<std::unique_ptr<std::vector<std::vector<unsigned int>>>, std::allocator<std::unique_ptr<std::vector<std::vector<unsigned int>>>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _opIdVectors;
Q _totalEvents;
Q _currentVectorIndex;
Q _currentEventIndex;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TQ,R,N) count;
```

## Instance methods

```
-[MPSGraphToolsProfilingEventCollection currentEvent];
-[MPSGraphToolsProfilingEventCollection next];
-[MPSGraphToolsProfilingEventCollection init];
-[MPSGraphToolsProfilingEventCollection count];
-[MPSGraphToolsProfilingEventCollection reset];
-[MPSGraphToolsProfilingEventCollection allEventBuffers];
-[MPSGraphToolsProfilingEventCollection addEvents:opIds:];
-[MPSGraphToolsProfilingEventCollection allOpIdBuffers];
-[MPSGraphToolsProfilingEventCollection currentOpIds];
```
