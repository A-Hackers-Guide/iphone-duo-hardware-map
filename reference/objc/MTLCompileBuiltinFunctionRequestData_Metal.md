# `MTLCompileBuiltinFunctionRequestData`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _sync;
@"NSObject<OS_dispatch_data>" _driverKeyData;
@"NSObject<OS_dispatch_data>" _builtinScript;
B _useAIRNTInterfaces;
{?="key"[32C]} _vendorPluginFunctionId;
@"NSArray" _binaryArchives;
B _failOnBinaryArchiveMiss;
@"<MTLPipelineCache>" _pipelineCache;
```

## Properties

```
@property (TB,N,V_sync) sync;
@property (T@"NSObject<OS_dispatch_data>",N) driverKeyData;
@property (T@"NSObject<OS_dispatch_data>",N) builtinScript;
@property (TB,N,V_useAIRNTInterfaces) useAIRNTInterfaces;
@property (T{?=[32C]},N,V_vendorPluginFunctionId) vendorPluginFunctionId;
@property (T@"NSArray",C,N,V_binaryArchives) binaryArchives;
@property (TB,N,V_failOnBinaryArchiveMiss) failOnBinaryArchiveMiss;
@property (T@"<MTLPipelineCache>",&,N,V_pipelineCache) pipelineCache;
```

## Instance methods

```
-[MTLCompileBuiltinFunctionRequestData setSync:];
-[MTLCompileBuiltinFunctionRequestData binaryArchives];
-[MTLCompileBuiltinFunctionRequestData init];
-[MTLCompileBuiltinFunctionRequestData dealloc];
-[MTLCompileBuiltinFunctionRequestData useAIRNTInterfaces];
-[MTLCompileBuiltinFunctionRequestData setDriverKeyData:];
-[MTLCompileBuiltinFunctionRequestData setBinaryArchives:];
-[MTLCompileBuiltinFunctionRequestData failOnBinaryArchiveMiss];
-[MTLCompileBuiltinFunctionRequestData pipelineCache];
-[MTLCompileBuiltinFunctionRequestData setVendorPluginFunctionId:];
-[MTLCompileBuiltinFunctionRequestData setUseAIRNTInterfaces:];
-[MTLCompileBuiltinFunctionRequestData setBuiltinScript:];
-[MTLCompileBuiltinFunctionRequestData vendorPluginFunctionId];
-[MTLCompileBuiltinFunctionRequestData driverKeyData];
-[MTLCompileBuiltinFunctionRequestData builtinScript];
-[MTLCompileBuiltinFunctionRequestData sync];
-[MTLCompileBuiltinFunctionRequestData setPipelineCache:];
-[MTLCompileBuiltinFunctionRequestData setFailOnBinaryArchiveMiss:];
```
