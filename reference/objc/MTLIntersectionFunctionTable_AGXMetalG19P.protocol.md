# `MTLIntersectionFunctionTable` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResource`
- 0 instance variables, 1 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Instance methods

```
-[MTLIntersectionFunctionTable setBuffers:offsets:withRange:];
-[MTLIntersectionFunctionTable setVisibleFunctionTables:withBufferRange:];
-[MTLIntersectionFunctionTable setBuffer:offset:atIndex:];
-[MTLIntersectionFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[MTLIntersectionFunctionTable setFunction:atIndex:];
-[MTLIntersectionFunctionTable setFunctions:withRange:];
-[MTLIntersectionFunctionTable gpuResourceID];
-[MTLIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:atIndex:];
-[MTLIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:withRange:];
-[MTLIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:];
-[MTLIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:withRange:];
```
