# `MTLFunctionReflectionInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLFunctionReflection`
- 10 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _builtInArguments;
@"NSArray" _arguments;
@"NSArray" _bindings;
@"NSData" _pluginReturnData;
Q _primitiveKind;
@"NSArray" _tags;
@"MTLType" _returnType;
@"NSString" _userAnnotation;
@"NSArray" _attributes;
@"NSArray" _visibleFunctionReferences;
```

## Instance methods

```
-[MTLFunctionReflectionInternal tags];
-[MTLFunctionReflectionInternal arguments];
-[MTLFunctionReflectionInternal formattedDescription:];
-[MTLFunctionReflectionInternal dealloc];
-[MTLFunctionReflectionInternal description];
-[MTLFunctionReflectionInternal attributes];
-[MTLFunctionReflectionInternal bindings];
-[MTLFunctionReflectionInternal returnType];
-[MTLFunctionReflectionInternal builtInArguments];
-[MTLFunctionReflectionInternal initWithArguments:argumentCount:builtInArgumentCount:globalBindings:globalBindingCount:pluginReturnData:primitiveKind:tags:tagCount:returnType:userAnnotation:attributes:visibleFunctionReferences:];
-[MTLFunctionReflectionInternal initWithDevice:libReflectionData:functionType:];
-[MTLFunctionReflectionInternal initWithDevice:reflectionData:functionType:options:];
-[MTLFunctionReflectionInternal pluginReturnData];
-[MTLFunctionReflectionInternal primitiveKind];
-[MTLFunctionReflectionInternal userAnnotation];
-[MTLFunctionReflectionInternal visibleFunctionReferences];
```
