# `MTLIndirectCommandBuffer` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResource`
- 0 instance variables, 2 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TQ,R) size;
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Instance methods

```
-[MTLIndirectCommandBuffer size];
-[MTLIndirectCommandBuffer gpuResourceID];
-[MTLIndirectCommandBuffer resetWithRange:];
-[MTLIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[MTLIndirectCommandBuffer indirectRenderCommandAtIndex:];
```
