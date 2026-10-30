# `MLMultiFunctionProgramContainer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLProgramContainer`
- 4 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
{map<std::string, InputNameToShapes, std::less<std::string>, std::allocator<std::pair<const std::string, InputNameToShapes>>>="__tree_"{__tree<std::__value_type<std::string, InputNameToShapes>, std::__map_value_compare<std::string, std::pair<const std::string, InputNameToShapes>, std::less<std::string>>, std::allocator<std::pair<const std::string, InputNameToShapes>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} functionNameToInputShapes;
@"NSString" _activeFunction;
@"NSDictionary" _functionNameToOutputLayersNames;
@"NSDictionary" _functionNameToInputLayersNames;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_functionNameToOutputLayersNames) functionNameToOutputLayersNames;
@property (T@"NSDictionary",&,N,V_functionNameToInputLayersNames) functionNameToInputLayersNames;
@property (T@"NSString",&,N) activeFunction;
```

## Class methods

```
+[MLMultiFunctionProgramContainer containerFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLMultiFunctionProgramContainer setActiveFunction:];
-[MLMultiFunctionProgramContainer functionNameToInputLayersNames];
-[MLMultiFunctionProgramContainer initWithContainer:program:error:];
-[MLMultiFunctionProgramContainer functionNameToOutputLayersNames];
-[MLMultiFunctionProgramContainer activeFunction];
-[MLMultiFunctionProgramContainer setFunctionNameToOutputLayersNames:];
-[MLMultiFunctionProgramContainer setFunctionNameToInputLayersNames:];
```
