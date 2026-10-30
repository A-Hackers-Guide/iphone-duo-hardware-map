# `_MTLFunction`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLFunctionSPI`
- 20 instance variables, 35 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
Q _functionType;
@"NSString" _name;
^v _libraryData;
@ _vendorPrivate;
@"NSArray" _vertexAttributes;
@"NSArray" _functionConstants;
@"NSDictionary" _functionConstantDictionary;
Q _options;
@"NSObject<OS_dispatch_data>" _precompiledOutput;
@"MTLDebugInstrumentationData" _debugInstrumentationData;
@"MTLType" _returnType;
@"NSArray" _arguments;
@"NSArray" _bindings;
@"NSString" _unpackedFilePath;
{?="key"[32C]} _functionConstantSpecializationHash;
@"NSArray" _relocations;
@"NSObject<OS_dispatch_data>" _reflectionData;
@"NSArray" _importedSymbols;
@"NSArray" _importedLibraries;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R,V_functionType) functionType;
@property (T@"NSString",R,V_name) name;
@property (T^v,R,V_libraryData) libraryData;
@property (T@"NSArray",R,V_importedSymbols) importedSymbols;
@property (T@"NSArray",R,V_importedLibraries) importedLibraries;
@property (T@"NSString",C,D) filePath;
@property (Tq,D) lineNumber;
@property (T@"NSString",C,V_unpackedFilePath) unpackedFilePath;
@property (TC,D,N) bitcodeType;
@property (T@"NSData",D) pluginData;
@property (T@,R,V_vendorPrivate) vendorPrivate;
@property (TQ,R,D) bitCodeOffset;
@property (TQ,R,D) renderTargetArrayIndexType;
@property (T@"NSArray",D) vertexAttributes;
@property (T@"MTLType",D) returnType;
@property (T@"NSArray",D) arguments;
@property (T@"NSArray",D) functionConstants;
@property (T@"NSObject<OS_dispatch_data>",R,D) functionInputs;
@property (TB,R,D) needsFunctionConstantValues;
@property (T@"NSString",C,D) label;
@property (TQ,R,V_options) options;
@property (T@"NSObject<OS_dispatch_data>",D) precompiledOutput;
@property (T@"MTLDebugInstrumentationData",&,N,V_debugInstrumentationData) debugInstrumentationData;
@property (T@"NSArray",R,D) bindings;
@property (T@"<MTLFunctionHandle>",R,N) functionHandle;
@property (T@"NSArray",C,D,N) relocations;
@property (TQ,R,D) patchType;
@property (Tq,R,D) patchControlPointCount;
@property (T@"NSArray",R,D) stageInputAttributes;
@property (T@"NSDictionary",R) functionConstantsDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLFunction functionType];
-[_MTLFunction requiredLLVMVersion];
-[_MTLFunction formattedDescription:];
-[_MTLFunction device];
-[_MTLFunction functionConstantsDictionary];
-[_MTLFunction importedLibraries];
-[_MTLFunction dealloc];
-[_MTLFunction newArgumentEncoderWithBufferIndex:reflection:pipelineLibrary:];
-[_MTLFunction reflectionWithOptions:binaryArchives:];
-[_MTLFunction functionHandle];
-[_MTLFunction bitCodeFileSize];
-[_MTLFunction reflectionWithOptions:];
-[_MTLFunction setDebugInstrumentationData:];
-[_MTLFunction reflectionWithOptions:completionHandler:];
-[_MTLFunction reflectionWithOptions:pipelineLibrary:];
-[_MTLFunction newArgumentEncoderWithBufferIndex:reflection:functionReflection:];
-[_MTLFunction newArgumentEncoderWithBufferIndex:];
-[_MTLFunction libraryData];
-[_MTLFunction functionConstantSpecializationHash];
-[_MTLFunction setUnpackedFilePath:];
-[_MTLFunction description];
-[_MTLFunction setVendorPrivate:];
-[_MTLFunction debugInstrumentationData];
-[_MTLFunction initWithName:type:libraryData:device:];
-[_MTLFunction options];
-[_MTLFunction newArgumentEncoderWithBufferIndex:reflection:];
-[_MTLFunction functionRef];
-[_MTLFunction importedSymbols];
-[_MTLFunction bitCodeHash];
-[_MTLFunction newArgumentEncoderWithBufferIndex:reflection:binaryArchives:];
-[_MTLFunction name];
-[_MTLFunction newArgumentEncoderWithBufferIndex:pipelineLibrary:];
-[_MTLFunction vendorPrivate];
-[_MTLFunction newFunctionWithPluginData:bitcodeType:];
-[_MTLFunction unpackedFilePath];
-[_MTLFunction bitcodeData];
```
