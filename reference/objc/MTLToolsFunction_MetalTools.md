# `MTLToolsFunction`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLFunctionSPI`
- 1 instance variables, 26 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _relocations;
```

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
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) functionType;
@property (TQ,R) patchType;
@property (Tq,R) patchControlPointCount;
@property (T@"NSArray",R) vertexAttributes;
@property (T@"NSArray",R) stageInputAttributes;
@property (T@"NSString",R) name;
@property (T@"NSDictionary",R) functionConstantsDictionary;
@property (TQ,R) options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsFunction setRelocations:];
-[MTLToolsFunction functionType];
-[MTLToolsFunction stageInputAttributes];
-[MTLToolsFunction arguments];
-[MTLToolsFunction renderTargetArrayIndexType];
-[MTLToolsFunction formattedDescription:];
-[MTLToolsFunction label];
-[MTLToolsFunction functionConstantsDictionary];
-[MTLToolsFunction importedLibraries];
-[MTLToolsFunction vertexAttributes];
-[MTLToolsFunction setLabel:];
-[MTLToolsFunction functionInputs];
-[MTLToolsFunction dealloc];
-[MTLToolsFunction precompiledOutput];
-[MTLToolsFunction newArgumentEncoderWithBufferIndex:reflection:pipelineLibrary:];
-[MTLToolsFunction reflectionWithOptions:binaryArchives:];
-[MTLToolsFunction functionHandle];
-[MTLToolsFunction reflectionWithOptions:];
-[MTLToolsFunction lineNumber];
-[MTLToolsFunction reflectionWithOptions:completionHandler:];
-[MTLToolsFunction reflectionWithOptions:pipelineLibrary:];
-[MTLToolsFunction patchType];
-[MTLToolsFunction newArgumentEncoderWithBufferIndex:];
-[MTLToolsFunction debugInstrumentationData];
-[MTLToolsFunction relocations];
-[MTLToolsFunction filePath];
-[MTLToolsFunction options];
-[MTLToolsFunction newArgumentEncoderWithBufferIndex:reflection:];
-[MTLToolsFunction importedSymbols];
-[MTLToolsFunction bitCodeHash];
-[MTLToolsFunction newArgumentEncoderWithBufferIndex:reflection:binaryArchives:];
-[MTLToolsFunction bindings];
-[MTLToolsFunction returnType];
-[MTLToolsFunction name];
-[MTLToolsFunction newArgumentEncoderWithBufferIndex:pipelineLibrary:];
-[MTLToolsFunction patchControlPointCount];
-[MTLToolsFunction functionConstants];
-[MTLToolsFunction newFunctionWithPluginData:bitcodeType:];
-[MTLToolsFunction unpackedFilePath];
-[MTLToolsFunction bitcodeData];
-[MTLToolsFunction initWithFunction:library:];
```
