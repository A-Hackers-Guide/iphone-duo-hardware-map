# `_MTLLibrary`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLLibrarySPI`
- 5 instance variables, 20 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
^v _libraryData;
@"NSMutableDictionary" _functionDictionary;
^{MTLLibraryContainer=^{MTLPipelineCollection}Ai{?=[32C]}^{MTLLibraryData}@@@@@} _cacheEntry;
B _shaderValidationEnabled;
```

## Properties

```
@property (T@"NSMutableDictionary",R,&,N,V_functionDictionary) functionDictionary;
@property (T@"NSString",C,D) label;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSArray",R,&,D) functionNames;
@property (T@"NSArray",R,&,D) externFunctionNames;
@property (T^v,R,V_libraryData) libraryData;
@property (T^{MTLLibraryContainer=^{MTLPipelineCollection}Ai{?=[32C]}^{MTLLibraryData}@@@@@},R,V_cacheEntry) cacheEntry;
@property (T@"NSString",C,D) overrideTriple;
@property (TB,N,V_shaderValidationEnabled) shaderValidationEnabled;
@property (T@"NSUUID",R,C,D) libraryIdentifier;
@property (T@"NSArray",R) variableList;
@property (TB,R) isStub;
@property (T@"NSArray",R,&) functionHashes;
@property (T@"NSData",R,D) bitcodeData;
@property (Tq,R,D) type;
@property (T@"NSString",R) installName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLLibrary getFunctionAliasAndNameForHash:functionName:alias:];
-[_MTLLibrary newFunctionWithName:constantValues:functionCache:error:];
-[_MTLLibrary newIntersectionFunctionWithDescriptor:error:];
-[_MTLLibrary newExternFunctionWithName:];
-[_MTLLibrary formattedDescription:];
-[_MTLLibrary device];
-[_MTLLibrary setOverrideTriple:];
-[_MTLLibrary newFunctionWithDescriptor:error:];
-[_MTLLibrary functionHashes];
-[_MTLLibrary dealloc];
-[_MTLLibrary newFunctionWithHash:linkResolver:];
-[_MTLLibrary isStub];
-[_MTLLibrary functionDictionary];
-[_MTLLibrary newFunctionWithName:constantValues:functionCache:specializedName:completionHandler:];
-[_MTLLibrary newFunctionWithName:];
-[_MTLLibrary cacheEntry];
-[_MTLLibrary libraryDataContents];
-[_MTLLibrary newFunctionWithDescriptor:destinationArchive:error:];
-[_MTLLibrary installName];
-[_MTLLibrary newFunctionWithName:constantValues:error:];
-[_MTLLibrary type];
-[_MTLLibrary newMetalScript];
-[_MTLLibrary newFunctionWithName:constantValues:pipelineLibrary:error:];
-[_MTLLibrary overrideTriple];
-[_MTLLibrary newFunctionWithName:constantValues:pipelineLibrary:completionHandler:];
-[_MTLLibrary libraryIdentifier];
-[_MTLLibrary shaderValidationEnabled];
-[_MTLLibrary libraryData];
-[_MTLLibrary newFunctionWithDescriptor:completionHandler:];
-[_MTLLibrary newFunctionWithDescriptor:destinationArchive:functionCache:completionHandler:];
-[_MTLLibrary newSpecializedFunctionWithDescriptorInternal:destinationArchive:functionCache:error:];
-[_MTLLibrary description];
-[_MTLLibrary serializeToURL:error:];
-[_MTLLibrary setShaderValidationEnabled:];
-[_MTLLibrary newFunctionWithNameInternal:];
-[_MTLLibrary functionNames];
-[_MTLLibrary newFunctionWithName:constantValues:completionHandler:];
-[_MTLLibrary newFunctionWithName:constantValues:functionCache:specializedName:error:];
-[_MTLLibrary initWithLibraryContainer:device:];
-[_MTLLibrary variableList];
-[_MTLLibrary reflectionForFunctionWithName:];
-[_MTLLibrary newIntersectionFunctionWithDescriptor:completionHandler:];
-[_MTLLibrary bitCodeWithHash:];
-[_MTLLibrary externFunctionNames];
-[_MTLLibrary bitcodeData];
```
