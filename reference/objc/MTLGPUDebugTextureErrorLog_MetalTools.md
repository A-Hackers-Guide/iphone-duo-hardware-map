# `MTLGPUDebugTextureErrorLog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLGPUDebugGPULog`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
C _expectedTextureType;
C _actualTextureType;
i _errorReason;
```

## Properties

```
@property (Ti,N,V_errorReason) errorReason;
@property (TC,N,V_expectedTextureType) expectedTextureType;
@property (TC,N,V_actualTextureType) actualTextureType;
```

## Instance methods

```
-[MTLGPUDebugTextureErrorLog description];
-[MTLGPUDebugTextureErrorLog setErrorReason:];
-[MTLGPUDebugTextureErrorLog errorReason];
-[MTLGPUDebugTextureErrorLog actualTextureType];
-[MTLGPUDebugTextureErrorLog expectedTextureType];
-[MTLGPUDebugTextureErrorLog setActualTextureType:];
-[MTLGPUDebugTextureErrorLog setExpectedTextureType:];
```
