# `MPSGraphAneSessionDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _energyEffecientWorkload;
Q _aneSessionSignal;
@"MPSGraphCompilationDescriptor" _compilationDescriptor;
@"MPSGraphExecutableEntryPoint" _shapedEntryPoint;
@"MPSGraphExecutableEntryPointToSymbolAndFileNameMap" _perEntryPointToSymbolAndFileNameMap;
```

## Properties

```
@property (TQ,V_aneSessionSignal) aneSessionSignal;
@property (T@"MPSGraphExecutableEntryPoint",&,V_shapedEntryPoint) shapedEntryPoint;
@property (T@"MPSGraphExecutableEntryPointToSymbolAndFileNameMap",&,V_perEntryPointToSymbolAndFileNameMap) perEntryPointToSymbolAndFileNameMap;
@property (T@"MPSGraphCompilationDescriptor",&,V_compilationDescriptor) compilationDescriptor;
@property (TB,V_energyEffecientWorkload) energyEffecientWorkload;
```

## Instance methods

```
-[MPSGraphAneSessionDescriptor init];
-[MPSGraphAneSessionDescriptor compilerOptions];
-[MPSGraphAneSessionDescriptor compilationDescriptor];
-[MPSGraphAneSessionDescriptor perEntryPointToSymbolAndFileNameMap];
-[MPSGraphAneSessionDescriptor setCompilationDescriptor:];
-[MPSGraphAneSessionDescriptor setCompilerOptions:];
-[MPSGraphAneSessionDescriptor setPerEntryPointToSymbolAndFileNameMap:];
-[MPSGraphAneSessionDescriptor aneSessionSignal];
-[MPSGraphAneSessionDescriptor energyEffecientWorkload];
-[MPSGraphAneSessionDescriptor setAneSessionSignal:];
-[MPSGraphAneSessionDescriptor setEnergyEffecientWorkload:];
-[MPSGraphAneSessionDescriptor setShapedEntryPoint:];
-[MPSGraphAneSessionDescriptor shapedEntryPoint];
```
