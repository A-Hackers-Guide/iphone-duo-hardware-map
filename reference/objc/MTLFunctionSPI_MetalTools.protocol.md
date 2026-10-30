# `MTLFunctionSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLFunction`
- 0 instance variables, 12 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C) filePath;
@property (Tq,R) lineNumber;
@property (T@"NSString",R,C) unpackedFilePath;
@property (TQ,R) renderTargetArrayIndexType;
@property (T@"MTLType",R) returnType;
@property (T@"NSArray",R) arguments;
@property (T@"NSArray",R) bindings;
@property (T@"NSArray",R) importedSymbols;
@property (T@"NSArray",R) importedLibraries;
@property (T@"MTLDebugInstrumentationData",R,N) debugInstrumentationData;
@property (T@"<MTLFunctionHandle>",R,N) functionHandle;
@property (T@"NSArray",C,N) relocations;
```

## Instance methods

```
-[MTLFunctionSPI setRelocations:];
-[MTLFunctionSPI arguments];
-[MTLFunctionSPI renderTargetArrayIndexType];
-[MTLFunctionSPI importedLibraries];
-[MTLFunctionSPI newArgumentEncoderWithBufferIndex:reflection:pipelineLibrary:];
-[MTLFunctionSPI reflectionWithOptions:binaryArchives:];
-[MTLFunctionSPI functionHandle];
-[MTLFunctionSPI reflectionWithOptions:];
-[MTLFunctionSPI lineNumber];
-[MTLFunctionSPI reflectionWithOptions:completionHandler:];
-[MTLFunctionSPI reflectionWithOptions:pipelineLibrary:];
-[MTLFunctionSPI debugInstrumentationData];
-[MTLFunctionSPI relocations];
-[MTLFunctionSPI filePath];
-[MTLFunctionSPI importedSymbols];
-[MTLFunctionSPI bitCodeHash];
-[MTLFunctionSPI newArgumentEncoderWithBufferIndex:reflection:binaryArchives:];
-[MTLFunctionSPI bindings];
-[MTLFunctionSPI returnType];
-[MTLFunctionSPI newArgumentEncoderWithBufferIndex:pipelineLibrary:];
-[MTLFunctionSPI newFunctionWithPluginData:bitcodeType:];
-[MTLFunctionSPI unpackedFilePath];
-[MTLFunctionSPI bitcodeData];
```
