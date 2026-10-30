# `MPSGraphNDXANEProcedureInfo`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _calleeName;
@"NSNumber" _procedureIndex;
@"NSArray" _machoInputsIndices;
@"NSArray" _machoOutputsIndices;
@"NSArray" _entrypointInputIndices;
@"NSArray" _entrypointOutputIndices;
@"NSArray" _weightSymbols;
```

## Properties

```
@property (T@"NSString",R,N,V_calleeName) calleeName;
@property (T@"NSNumber",&,N,V_procedureIndex) procedureIndex;
@property (T@"NSArray",R,N,V_machoInputsIndices) machoInputsIndices;
@property (T@"NSArray",R,N,V_machoOutputsIndices) machoOutputsIndices;
@property (T@"NSArray",R,N,V_entrypointInputIndices) entrypointInputIndices;
@property (T@"NSArray",R,N,V_entrypointOutputIndices) entrypointOutputIndices;
@property (T@"NSArray",R,N,V_weightSymbols) weightSymbols;
```

## Instance methods

```
-[MPSGraphNDXANEProcedureInfo procedureIndex];
-[MPSGraphNDXANEProcedureInfo calleeName];
-[MPSGraphNDXANEProcedureInfo entrypointInputIndices];
-[MPSGraphNDXANEProcedureInfo entrypointOutputIndices];
-[MPSGraphNDXANEProcedureInfo initWithCalleeName:procedureIndex:machoInputsIndices:machoOutputsIndices:entrypointInputIndices:entrypointOutputIndices:weightSymbols:];
-[MPSGraphNDXANEProcedureInfo machoInputsIndices];
-[MPSGraphNDXANEProcedureInfo machoOutputsIndices];
-[MPSGraphNDXANEProcedureInfo setProcedureIndex:];
-[MPSGraphNDXANEProcedureInfo weightSymbols];
```
