# `MTLDebugLibrary`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsLibrary`
- 5 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _debugType;
@ _code;
@"MTLCompileOptions" _compileOptions;
@"NSArray" _imageFilterFunctions;
^{?=BQ^{?}} _imageFilterFunctionInfo;
```

## Properties

```
@property (TQ,N,V_debugType) debugType;
@property (T@,C,N,V_code) code;
@property (T@"MTLCompileOptions",C,N,V_compileOptions) compileOptions;
@property (T@"NSArray",R,N,V_imageFilterFunctions) imageFilterFunctions;
@property (T^{?=BQ^{?}},R,N,V_imageFilterFunctionInfo) imageFilterFunctionInfo;
```

## Instance methods

```
-[MTLDebugLibrary setCode:];
-[MTLDebugLibrary newIntersectionFunctionWithDescriptor:error:];
-[MTLDebugLibrary newFunctionWithDescriptor:error:];
-[MTLDebugLibrary dealloc];
-[MTLDebugLibrary code];
-[MTLDebugLibrary newFunctionWithName:];
-[MTLDebugLibrary newFunctionWithName:constantValues:error:];
-[MTLDebugLibrary newFunctionWithDescriptor:completionHandler:];
-[MTLDebugLibrary newFunctionWithName:constantValues:completionHandler:];
-[MTLDebugLibrary newIntersectionFunctionWithDescriptor:completionHandler:];
-[MTLDebugLibrary debugType];
-[MTLDebugLibrary compileOptions];
-[MTLDebugLibrary copyConstantValues:];
-[MTLDebugLibrary imageFilterFunctionInfo];
-[MTLDebugLibrary imageFilterFunctions];
-[MTLDebugLibrary initWithLibrary:parent:type:code:options:];
-[MTLDebugLibrary setCompileOptions:];
-[MTLDebugLibrary setDebugType:];
-[MTLDebugLibrary setImageFilterFunctions:imageFilterFunctionInfo:];
-[MTLDebugLibrary validateDescriptor:expectedClass:];
```
