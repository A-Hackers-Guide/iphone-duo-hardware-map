# `MPSGraphNDXRuntime`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 9 instance variables, 1 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"_ANEModel" _model;
@"_ANEClient" _clientConnection;
@"NSDictionary" _anefOptions;
I _qos;
@"NSMutableDictionary" _prewireRequests;
@"NSDictionary" _entryPointANEProcedures;
@"MPSGraphNDXRuntime" _baseModel;
@"MPSGraphNDXAdapterCache" _adapterCache;
B _enableOverflowAsAsserts;
```

## Properties

```
@property (TB,R,N) hasIFPWeightSymbols;
```

## Class methods

```
+[MPSGraphNDXRuntime _buildEntryPointProceduresFromManifestUrl:model:];
+[MPSGraphNDXRuntime currentANESoCString];
```

## Instance methods

```
-[MPSGraphNDXRuntime dealloc];
-[MPSGraphNDXRuntime _finishLoadingModel:useOnlyCacheURLIdentifier:error:];
-[MPSGraphNDXRuntime _syncProcedureIndicesFromAdaptedModel:];
-[MPSGraphNDXRuntime adaptModel:error:];
-[MPSGraphNDXRuntime collectProcedureModels:];
-[MPSGraphNDXRuntime getANEHandles];
-[MPSGraphNDXRuntime getANERequest:outputs:entryFunctionName:error:];
-[MPSGraphNDXRuntime getProcedureInfo:];
-[MPSGraphNDXRuntime hasIFPWeightSymbols];
-[MPSGraphNDXRuntime inferValue:outputs:entryFunctionName:error:];
-[MPSGraphNDXRuntime initFromMacho:manifestUrl:error:];
-[MPSGraphNDXRuntime initFromManifest:error:];
-[MPSGraphNDXRuntime initFromModel:aneClient:baseModel:options:];
-[MPSGraphNDXRuntime prewire:outputs:entryFunctionName:error:];
-[MPSGraphNDXRuntime undoPrewire:error:];
```
