# `_TtC6CoreML12MLOdieEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelSwiftEngine`
- Protocols: `MLStatefulModelEngine`
- 4 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
Foundation.URL mlirBytecodeURL;
Foundation.URL precompiledLibrary;
_$sSS functionName;
CoreML.MLOdieFunctionPool functionPool;
```

## Properties

```
@property (TQ,N,R) predictionTypeForKTrace;
```

## Class methods

```
+[_TtC6CoreML12MLOdieEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[_TtC6CoreML12MLOdieEngine predictionTypeForKTrace];
-[_TtC6CoreML12MLOdieEngine submitPredictionRequest:completionHandler:];
-[_TtC6CoreML12MLOdieEngine newStateWithClientBuffers:];
-[_TtC6CoreML12MLOdieEngine newRequestForModel:inputFeatures:usingState:options:error:];
-[_TtC6CoreML12MLOdieEngine predictionFromFeatures:options:error:];
-[_TtC6CoreML12MLOdieEngine predictionFromFeatures:usingState:options:error:];
-[_TtC6CoreML12MLOdieEngine initWithDescription:configuration:];
```
