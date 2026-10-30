# `MTLLibrary` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSArray",R) functionNames;
@property (Tq,R) type;
@property (T@"NSString",R) installName;
```

## Instance methods

```
-[MTLLibrary newIntersectionFunctionWithDescriptor:error:];
-[MTLLibrary device];
-[MTLLibrary label];
-[MTLLibrary newFunctionWithDescriptor:error:];
-[MTLLibrary setLabel:];
-[MTLLibrary newFunctionWithName:];
-[MTLLibrary installName];
-[MTLLibrary newFunctionWithName:constantValues:error:];
-[MTLLibrary type];
-[MTLLibrary newFunctionWithDescriptor:completionHandler:];
-[MTLLibrary functionNames];
-[MTLLibrary newFunctionWithName:constantValues:completionHandler:];
-[MTLLibrary reflectionForFunctionWithName:];
-[MTLLibrary newIntersectionFunctionWithDescriptor:completionHandler:];
```
