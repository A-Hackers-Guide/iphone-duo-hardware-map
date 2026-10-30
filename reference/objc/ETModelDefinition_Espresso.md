# `ETModelDefinition`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _layerNames;
@"NSArray" _inputs;
@"NSArray" _outputs;
@"NSArray" _trainingInputs;
@"NSArray" _trainingOutputs;
@"NSURL" _modelURL;
@"NSString" _isTrainingGlobalName;
@"NSString" _initializer;
```

## Properties

```
@property (T@"NSArray",R,V_layerNames) layerNames;
@property (T@"NSArray",R,V_inputs) inputs;
@property (T@"NSArray",R,V_outputs) outputs;
@property (T@"NSArray",R,V_trainingInputs) trainingInputs;
@property (T@"NSArray",R,V_trainingOutputs) trainingOutputs;
@property (T@"NSURL",R,V_modelURL) modelURL;
@property (T@"NSString",R,V_isTrainingGlobalName) isTrainingGlobalName;
@property (T@"NSString",R,V_initializer) initializer;
```

## Instance methods

```
-[ETModelDefinition outputs];
-[ETModelDefinition inputs];
-[ETModelDefinition modelURL];
-[ETModelDefinition layerNames];
-[ETModelDefinition trainingOutputs];
-[ETModelDefinition initWithInferenceNetworkPath:error:];
-[ETModelDefinition initWithInferenceNetworkPath:inferenceInputs:inferenceOutputs:error:];
-[ETModelDefinition initWithTrainingNetworkPath:inferenceInputs:inferenceOutputs:trainingInputs:trainingOutputs:trainingControlVariableName:withInitializer:error:];
-[ETModelDefinition initializer];
-[ETModelDefinition isTrainingGlobalName];
-[ETModelDefinition trainingInputs];
```
