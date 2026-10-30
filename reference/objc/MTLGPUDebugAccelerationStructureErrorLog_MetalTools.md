# `MTLGPUDebugAccelerationStructureErrorLog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLGPUDebugGPULog`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
i _errorReason;
Q _expectedAccelerationStructureType;
Q _actualAccelerationStructureType;
```

## Properties

```
@property (TQ,N,V_expectedAccelerationStructureType) expectedAccelerationStructureType;
@property (TQ,N,V_actualAccelerationStructureType) actualAccelerationStructureType;
@property (Ti,N,V_errorReason) errorReason;
```

## Instance methods

```
-[MTLGPUDebugAccelerationStructureErrorLog dealloc];
-[MTLGPUDebugAccelerationStructureErrorLog description];
-[MTLGPUDebugAccelerationStructureErrorLog setErrorReason:];
-[MTLGPUDebugAccelerationStructureErrorLog errorReason];
-[MTLGPUDebugAccelerationStructureErrorLog actualAccelerationStructureType];
-[MTLGPUDebugAccelerationStructureErrorLog expectedAccelerationStructureType];
-[MTLGPUDebugAccelerationStructureErrorLog setActualAccelerationStructureType:];
-[MTLGPUDebugAccelerationStructureErrorLog setExpectedAccelerationStructureType:];
```
