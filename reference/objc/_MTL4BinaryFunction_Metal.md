# `_MTL4BinaryFunction`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4BinaryFunctionGGDSPI`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _relocations;
@"NSString" _name;
@"MTLDebugInstrumentationData" debugInstrumentationData;
@"MTL4BinaryFunctionReflection" _reflection;
Q _functionType;
```

## Properties

```
@property (T@"NSString",R,V_name) name;
@property (T@"MTL4BinaryFunctionReflection",R,V_reflection) reflection;
@property (TQ,R,V_functionType) functionType;
@property (T@"MTLDebugInstrumentationData",R,N,VdebugInstrumentationData) debugInstrumentationData;
@property (T@"NSArray",C,N) relocations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4BinaryFunction setRelocations:];
-[_MTL4BinaryFunction functionType];
-[_MTL4BinaryFunction init];
-[_MTL4BinaryFunction dealloc];
-[_MTL4BinaryFunction initWithFunctionDescriptor:];
-[_MTL4BinaryFunction hash];
-[_MTL4BinaryFunction debugInstrumentationData];
-[_MTL4BinaryFunction relocations];
-[_MTL4BinaryFunction reflection];
-[_MTL4BinaryFunction copyWithZone:];
-[_MTL4BinaryFunction isEqual:];
-[_MTL4BinaryFunction name];
```
