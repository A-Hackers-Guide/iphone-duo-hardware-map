# `MLModelStructureProgram`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _functions;
```

## Properties

```
@property (T@"MLModelStructureProgramFunction",R,N) mainFunction;
@property (T@"NSDictionary",R,C,N,V_functions) functions;
```

## Class methods

```
+[MLModelStructureProgram loadModelStructureFromCompiledArchive:modelVersionInfo:compilerVersionInfo:path:error:];
```

## Instance methods

```
-[MLModelStructureProgram functions];
-[MLModelStructureProgram initWithFunctions:];
-[MLModelStructureProgram mainFunction];
```
