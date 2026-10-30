# `MTLLibrarySPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLLibrary`
- 0 instance variables, 5 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) overrideTriple;
@property (TB,N) shaderValidationEnabled;
@property (T@"NSArray",R) externFunctionNames;
@property (T@"NSData",R) bitcodeData;
@property (T@"NSUUID",R,C) libraryIdentifier;
```

## Instance methods

```
-[MTLLibrarySPI newExternFunctionWithName:];
-[MTLLibrarySPI setOverrideTriple:];
-[MTLLibrarySPI newFunctionWithDescriptor:destinationArchive:error:];
-[MTLLibrarySPI newFunctionWithName:constantValues:pipelineLibrary:error:];
-[MTLLibrarySPI overrideTriple];
-[MTLLibrarySPI newFunctionWithName:constantValues:pipelineLibrary:completionHandler:];
-[MTLLibrarySPI libraryIdentifier];
-[MTLLibrarySPI shaderValidationEnabled];
-[MTLLibrarySPI serializeToURL:error:];
-[MTLLibrarySPI setShaderValidationEnabled:];
-[MTLLibrarySPI externFunctionNames];
-[MTLLibrarySPI bitcodeData];
```
