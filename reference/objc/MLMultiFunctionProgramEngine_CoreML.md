# `MLMultiFunctionProgramEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLProgramInternal`, `MLNeuralNetwork`, `MLClassifier`, `MLRegressor`, `MLCompiledModelLoader`, `MLProgram`
- 3 instance variables, 14 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _functionNameToEngineMap;
@"MLMultiFunctionProgramContainer" _container;
@"NSString" _modelFileBasePath;
```

## Properties

```
@property (T@"MLMultiFunctionProgramContainer",R,N,V_container) container;
@property (T@"NSString",R,N,V_modelFileBasePath) modelFileBasePath;
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) serializedMILText;
```

## Class methods

```
+[MLMultiFunctionProgramEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLMultiFunctionProgramEngine predictionTypeForKTrace];
-[MLMultiFunctionProgramEngine predictionsFromBatch:options:error:];
-[MLMultiFunctionProgramEngine classLabels];
-[MLMultiFunctionProgramEngine executionSchedule];
-[MLMultiFunctionProgramEngine enableInstrumentsTracing];
-[MLMultiFunctionProgramEngine regress:options:error:];
-[MLMultiFunctionProgramEngine modelPath];
-[MLMultiFunctionProgramEngine program];
-[MLMultiFunctionProgramEngine evaluateFunction:arguments:error:];
-[MLMultiFunctionProgramEngine newContextAndReturnError:];
-[MLMultiFunctionProgramEngine predictionFromFeatures:options:error:];
-[MLMultiFunctionProgramEngine serializedMILText];
-[MLMultiFunctionProgramEngine classify:options:error:];
-[MLMultiFunctionProgramEngine signpostID];
-[MLMultiFunctionProgramEngine container];
-[MLMultiFunctionProgramEngine evaluate:error:];
-[MLMultiFunctionProgramEngine programEngineForFunction:error:];
-[MLMultiFunctionProgramEngine initWithProgramContainer:configuration:error:];
-[MLMultiFunctionProgramEngine modelFileBasePath];
-[MLMultiFunctionProgramEngine removeEngineForFunctionName:];
-[MLMultiFunctionProgramEngine setModelPath:modelName:];
-[MLMultiFunctionProgramEngine updateModelFilePath:];
-[MLMultiFunctionProgramEngine verifyArgumentNames:functionName:error:];
```
