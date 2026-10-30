# `BWParallelJoinerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFunnelNode`
- 3 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
i _inputsCount;
@"NSMutableDictionary" _receivedBuffers;
@"NSMutableDictionary" _sentErrorCountForID;
```

## Instance methods

```
-[BWParallelJoinerNode renderSampleBuffer:forInput:];
-[BWParallelJoinerNode initWithNumberOfInputs:mediaType:];
-[BWParallelJoinerNode dealloc];
-[BWParallelJoinerNode handleNodeError:forInput:];
```
