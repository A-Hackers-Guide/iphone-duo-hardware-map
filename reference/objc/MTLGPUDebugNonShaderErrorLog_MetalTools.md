# `MTLGPUDebugNonShaderErrorLog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLGPUDebugGPULog`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"MTLGPUDebugDevice" _device;
@"<MTLAllocation>" m_resource;
Q _resourceID;
```

## Properties

```
@property (TQ,R,N,V_resourceID) resourceID;
```

## Instance methods

```
-[MTLGPUDebugNonShaderErrorLog dealloc];
-[MTLGPUDebugNonShaderErrorLog description];
-[MTLGPUDebugNonShaderErrorLog resourceID];
-[MTLGPUDebugNonShaderErrorLog initWithResourceID:resourceType:resourceInfo:device:];
-[MTLGPUDebugNonShaderErrorLog resourceDescription];
```
