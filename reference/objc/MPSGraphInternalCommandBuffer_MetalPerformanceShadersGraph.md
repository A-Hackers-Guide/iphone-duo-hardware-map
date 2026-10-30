# `MPSGraphInternalCommandBuffer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCommandBuffer`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"MPSCommandBuffer" _original;
@"MPSGraphExecutableExecutionDescriptor" _executableExecutionDescriptor;
I _commandBufferIndex;
```

## Instance methods

```
-[MPSGraphInternalCommandBuffer commit];
-[MPSGraphInternalCommandBuffer methodSignatureForSelector:];
-[MPSGraphInternalCommandBuffer respondsToSelector:];
-[MPSGraphInternalCommandBuffer forwardInvocation:];
-[MPSGraphInternalCommandBuffer commitAndContinue];
-[MPSGraphInternalCommandBuffer initWithMPSCommandBuffer:executableExecutionDescriptor:];
-[MPSGraphInternalCommandBuffer mpsCommandBufferDescriptor];
```
