# `MLProgramEvaluator`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<MLProgramInternal>" _program;
```

## Properties

```
@property (T@"<MLProgramInternal>",&,N,V_program) program;
@property (T@"<MLModeling>",R,C) model;
```

## Instance methods

```
-[MLProgramEvaluator model];
-[MLProgramEvaluator program];
-[MLProgramEvaluator newContextAndReturnError:];
-[MLProgramEvaluator setProgram:];
-[MLProgramEvaluator evaluateFunction:arguments:context:error:];
-[MLProgramEvaluator evaluateFunction:arguments:context:updateContext:error:];
-[MLProgramEvaluator initWithProgram:error:];
-[MLProgramEvaluator prepareArgumentsFromFeatures:context:forFunctionName:];
-[MLProgramEvaluator updateContext:functionName:result:];
```
