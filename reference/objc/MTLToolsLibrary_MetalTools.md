# `MTLToolsLibrary`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLLibrarySPI`
- 0 instance variables, 14 properties, 27 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) overrideTriple;
@property (TB,N) shaderValidationEnabled;
@property (T@"NSArray",R) externFunctionNames;
@property (T@"NSData",R) bitcodeData;
@property (T@"NSUUID",R,C) libraryIdentifier;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSArray",R) functionNames;
@property (Tq,R) type;
@property (T@"NSString",R) installName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsLibrary newIntersectionFunctionWithDescriptor:error:];
-[MTLToolsLibrary newExternFunctionWithName:];
-[MTLToolsLibrary device];
-[MTLToolsLibrary label];
-[MTLToolsLibrary setOverrideTriple:];
-[MTLToolsLibrary newFunctionWithDescriptor:error:];
-[MTLToolsLibrary setLabel:];
-[MTLToolsLibrary dealloc];
-[MTLToolsLibrary newFunctionWithName:];
-[MTLToolsLibrary newFunctionWithDescriptor:destinationArchive:error:];
-[MTLToolsLibrary installName];
-[MTLToolsLibrary newFunctionWithName:constantValues:error:];
-[MTLToolsLibrary type];
-[MTLToolsLibrary newFunctionWithName:constantValues:pipelineLibrary:error:];
-[MTLToolsLibrary overrideTriple];
-[MTLToolsLibrary newFunctionWithName:constantValues:pipelineLibrary:completionHandler:];
-[MTLToolsLibrary libraryIdentifier];
-[MTLToolsLibrary shaderValidationEnabled];
-[MTLToolsLibrary newFunctionWithDescriptor:completionHandler:];
-[MTLToolsLibrary serializeToURL:error:];
-[MTLToolsLibrary setShaderValidationEnabled:];
-[MTLToolsLibrary functionNames];
-[MTLToolsLibrary newFunctionWithName:constantValues:completionHandler:];
-[MTLToolsLibrary reflectionForFunctionWithName:];
-[MTLToolsLibrary newIntersectionFunctionWithDescriptor:completionHandler:];
-[MTLToolsLibrary externFunctionNames];
-[MTLToolsLibrary bitcodeData];
```
