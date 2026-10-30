# `MTLCompileFunctionRequestData`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 40 instance methods, 1 class methods

## Instance variables

```
B _sync;
@"MTLFunction" _function;
Q _functionOptions;
Q _pipelineOptions;
@"NSObject<OS_dispatch_data>" _frameworkData;
@"NSObject<OS_dispatch_data>" _driverKeyData;
@"NSObject<OS_dispatch_data>" _airScript;
@"NSObject<OS_dispatch_data>" _archiverId;
@"<MTLPipelineCache>" _pipelineCache;
{?="key"[32C]} _archiveHashKey;
@"<MTLBinaryArchive>" _destinationBinaryArchive;
@"NSArray" _binaryArchives;
@"NSArray" _visibleFunctions;
@"NSArray" _privateVisibleFunctions;
@"NSDictionary" _visibleFunctionGroups;
B _useAIRNTInterfaces;
I _maxAccelerationStructureTraversalDepth;
@"NSDictionary" _gpuCompilerSPIOptions;
{?="key"[32C]} _vendorPluginFunctionId;
```

## Properties

```
@property (TB,N,V_sync) sync;
@property (TQ,N,V_functionOptions) functionOptions;
@property (TQ,N,V_pipelineOptions) pipelineOptions;
@property (T@"MTLFunction",&,N,V_function) function;
@property (T@"NSObject<OS_dispatch_data>",N) frameworkData;
@property (T@"NSObject<OS_dispatch_data>",N) driverKeyData;
@property (T@"<MTLPipelineCache>",&,N,V_pipelineCache) pipelineCache;
@property (T{?=[32C]},N,V_archiveHashKey) archiveHashKey;
@property (T@"<MTLBinaryArchive>",&,N,V_destinationBinaryArchive) destinationBinaryArchive;
@property (T@"NSArray",C,N,V_binaryArchives) binaryArchives;
@property (T@"NSArray",C,N,V_visibleFunctions) visibleFunctions;
@property (T@"NSArray",C,N,V_privateVisibleFunctions) privateVisibleFunctions;
@property (T@"NSDictionary",C,N,V_visibleFunctionGroups) visibleFunctionGroups;
@property (TI,N,V_maxAccelerationStructureTraversalDepth) maxAccelerationStructureTraversalDepth;
@property (T@"NSObject<OS_dispatch_data>",N) airScript;
@property (T{?=[32C]},N,V_vendorPluginFunctionId) vendorPluginFunctionId;
@property (T@"NSObject<OS_dispatch_data>",N) archiverId;
@property (T@"NSDictionary",C,N,V_gpuCompilerSPIOptions) gpuCompilerSPIOptions;
@property (TB,V_useAIRNTInterfaces) useAIRNTInterfaces;
```

## Class methods

```
+[MTLCompileFunctionRequestData newVisibleRequestWithFunction:descriptor:];
```

## Instance methods

```
-[MTLCompileFunctionRequestData airScript];
-[MTLCompileFunctionRequestData setSync:];
-[MTLCompileFunctionRequestData setVisibleFunctions:];
-[MTLCompileFunctionRequestData setFunctionOptions:];
-[MTLCompileFunctionRequestData binaryArchives];
-[MTLCompileFunctionRequestData gpuCompilerSPIOptions];
-[MTLCompileFunctionRequestData visibleFunctions];
-[MTLCompileFunctionRequestData setPipelineOptions:];
-[MTLCompileFunctionRequestData function];
-[MTLCompileFunctionRequestData setPrivateVisibleFunctions:];
-[MTLCompileFunctionRequestData visibleFunctionGroups];
-[MTLCompileFunctionRequestData init];
-[MTLCompileFunctionRequestData dealloc];
-[MTLCompileFunctionRequestData setArchiveHashKey:];
-[MTLCompileFunctionRequestData setGpuCompilerSPIOptions:];
-[MTLCompileFunctionRequestData archiveHashKey];
-[MTLCompileFunctionRequestData maxAccelerationStructureTraversalDepth];
-[MTLCompileFunctionRequestData useAIRNTInterfaces];
-[MTLCompileFunctionRequestData pipelineOptions];
-[MTLCompileFunctionRequestData setDriverKeyData:];
-[MTLCompileFunctionRequestData setBinaryArchives:];
-[MTLCompileFunctionRequestData setMaxAccelerationStructureTraversalDepth:];
-[MTLCompileFunctionRequestData functionOptions];
-[MTLCompileFunctionRequestData setFunction:];
-[MTLCompileFunctionRequestData frameworkData];
-[MTLCompileFunctionRequestData setAirScript:];
-[MTLCompileFunctionRequestData setDestinationBinaryArchive:];
-[MTLCompileFunctionRequestData pipelineCache];
-[MTLCompileFunctionRequestData setVendorPluginFunctionId:];
-[MTLCompileFunctionRequestData setUseAIRNTInterfaces:];
-[MTLCompileFunctionRequestData setArchiverId:];
-[MTLCompileFunctionRequestData vendorPluginFunctionId];
-[MTLCompileFunctionRequestData privateVisibleFunctions];
-[MTLCompileFunctionRequestData setVisibleFunctionGroups:];
-[MTLCompileFunctionRequestData driverKeyData];
-[MTLCompileFunctionRequestData archiverId];
-[MTLCompileFunctionRequestData setFrameworkData:];
-[MTLCompileFunctionRequestData sync];
-[MTLCompileFunctionRequestData setPipelineCache:];
-[MTLCompileFunctionRequestData destinationBinaryArchive];
```
