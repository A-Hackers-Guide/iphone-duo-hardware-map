# `MTLDebugAccelerationStructure`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsAccelerationStructure`
- Protocols: `MTLDebugResourcePurgeable`
- 3 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
@"MTLDebugBuffer" _debugBuffer;
```

## Instance methods

```
-[MTLDebugAccelerationStructure buffer];
-[MTLDebugAccelerationStructure formattedDescription:];
-[MTLDebugAccelerationStructure dealloc];
-[MTLDebugAccelerationStructure setPurgeableState:];
-[MTLDebugAccelerationStructure description];
-[MTLDebugAccelerationStructure initWithBaseObject:parent:];
-[MTLDebugAccelerationStructure purgeableStateValidForRendering];
-[MTLDebugAccelerationStructure initWithBaseObject:parent:heap:];
-[MTLDebugAccelerationStructure lockPurgeableState];
-[MTLDebugAccelerationStructure unlockPurgeableState];
```
