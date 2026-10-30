# `MPSGraphDelegateDebugConfiguration`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _printIRAfterAll;
B _enableDebugInfo;
B _writeDebugInfo;
@"MPSGraphDelegateMLIRDumpConfiguration" _compiledModuleDumpConfiguration;
```

## Properties

```
@property (TB,V_printIRAfterAll) printIRAfterAll;
@property (T@"MPSGraphDelegateMLIRDumpConfiguration",&,V_compiledModuleDumpConfiguration) compiledModuleDumpConfiguration;
@property (TB,V_enableDebugInfo) enableDebugInfo;
@property (TB,V_writeDebugInfo) writeDebugInfo;
```

## Instance methods

```
-[MPSGraphDelegateDebugConfiguration compiledModuleDumpConfiguration];
-[MPSGraphDelegateDebugConfiguration enableDebugInfo];
-[MPSGraphDelegateDebugConfiguration printIRAfterAll];
-[MPSGraphDelegateDebugConfiguration setCompiledModuleDumpConfiguration:];
-[MPSGraphDelegateDebugConfiguration setEnableDebugInfo:];
-[MPSGraphDelegateDebugConfiguration setPrintIRAfterAll:];
-[MPSGraphDelegateDebugConfiguration setWriteDebugInfo:];
-[MPSGraphDelegateDebugConfiguration writeDebugInfo];
```
