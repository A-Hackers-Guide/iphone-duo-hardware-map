# `_MTLMLLibrary`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLLibrarySPI`
- 11 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
[3@"<MPSGraphExecutableProxy>"] _executables;
@"NSURL" _mpsgraphPackageURL;
@"<MPSGraphExecutableReflectionProxy>" _reflection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B shaderValidationEnabled;
@"<MTLDevice>" _device;
q _type;
@"NSData" bitcodeData;
@"NSArray" externFunctionNames;
@"NSUUID" libraryIdentifier;
@"NSString" overrideTriple;
```

## Properties

```
@property (T@"NSString",C,VoverrideTriple) overrideTriple;
@property (TB,N,VshaderValidationEnabled) shaderValidationEnabled;
@property (T@"NSArray",R,VexternFunctionNames) externFunctionNames;
@property (T@"NSData",R,VbitcodeData) bitcodeData;
@property (T@"NSUUID",R,C,VlibraryIdentifier) libraryIdentifier;
@property (T@"NSString",C,D) label;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSArray",R,D) functionNames;
@property (Tq,R,V_type) type;
@property (T@"NSString",R) installName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLMLLibrary newFunctionWithName:constantValues:functionCache:error:];
-[_MTLMLLibrary newIntersectionFunctionWithDescriptor:error:];
-[_MTLMLLibrary newExternFunctionWithName:];
-[_MTLMLLibrary device];
-[_MTLMLLibrary setOverrideTriple:];
-[_MTLMLLibrary newFunctionWithDescriptor:error:];
-[_MTLMLLibrary dealloc];
-[_MTLMLLibrary newFunctionWithName:];
-[_MTLMLLibrary newFunctionWithDescriptor:destinationArchive:error:];
-[_MTLMLLibrary installName];
-[_MTLMLLibrary newFunctionWithName:constantValues:error:];
-[_MTLMLLibrary type];
-[_MTLMLLibrary newFunctionWithName:constantValues:pipelineLibrary:error:];
-[_MTLMLLibrary overrideTriple];
-[_MTLMLLibrary newFunctionWithName:constantValues:pipelineLibrary:completionHandler:];
-[_MTLMLLibrary libraryIdentifier];
-[_MTLMLLibrary shaderValidationEnabled];
-[_MTLMLLibrary newFunctionWithDescriptor:completionHandler:];
-[_MTLMLLibrary serializeToURL:error:];
-[_MTLMLLibrary setShaderValidationEnabled:];
-[_MTLMLLibrary functionNames];
-[_MTLMLLibrary newFunctionWithName:constantValues:completionHandler:];
-[_MTLMLLibrary reflectionForFunctionWithName:];
-[_MTLMLLibrary newIntersectionFunctionWithDescriptor:completionHandler:];
-[_MTLMLLibrary externFunctionNames];
-[_MTLMLLibrary bitcodeData];
-[_MTLMLLibrary executableSize];
-[_MTLMLLibrary executableWithDeviceSelection:];
-[_MTLMLLibrary initWithDevice:executable:url:reflection:];
```
