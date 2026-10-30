# `MLModelStructure`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"MLModelStructureNeuralNetwork" _neuralNetwork;
@"MLModelStructureProgram" _program;
@"MLModelStructurePipeline" _pipeline;
```

## Properties

```
@property (T@"MLModelStructureNeuralNetwork",R,N,V_neuralNetwork) neuralNetwork;
@property (T@"MLModelStructureProgram",R,N,V_program) program;
@property (T@"MLModelStructurePipeline",R,N,V_pipeline) pipeline;
```

## Class methods

```
+[MLModelStructure loadContentsOfURL:completionHandler:];
+[MLModelStructure loadModelAsset:completionHandler:];
+[MLModelStructure loadModelStructureFromCompiledArchive:path:error:];
```

## Instance methods

```
-[MLModelStructure program];
-[MLModelStructure pipeline];
-[MLModelStructure neuralNetwork];
-[MLModelStructure initWithPipeline:];
-[MLModelStructure initWithNeuralNetwork:];
-[MLModelStructure initWithNeuralNetwork:program:pipeline:];
-[MLModelStructure initWithProgram:];
```
