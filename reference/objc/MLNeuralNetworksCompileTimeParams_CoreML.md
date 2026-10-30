# `MLNeuralNetworksCompileTimeParams`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _lossType;
q _optimizerType;
@"NSDictionary" _optimizerParameters;
@"NSDictionary" _lossParameters;
@"NSArray" _trainableLayerNames;
@"NSDictionary" _updateParameters;
```

## Properties

```
@property (Tq,N,V_lossType) lossType;
@property (Tq,N,V_optimizerType) optimizerType;
@property (T@"NSDictionary",&,N,V_optimizerParameters) optimizerParameters;
@property (T@"NSDictionary",&,N,V_lossParameters) lossParameters;
@property (T@"NSArray",&,N,V_trainableLayerNames) trainableLayerNames;
@property (T@"NSDictionary",&,N,V_updateParameters) updateParameters;
```

## Class methods

```
+[MLNeuralNetworksCompileTimeParams supportsSecureCoding];
```

## Instance methods

```
-[MLNeuralNetworksCompileTimeParams updateParameters];
-[MLNeuralNetworksCompileTimeParams encodeWithCoder:];
-[MLNeuralNetworksCompileTimeParams initWithCoder:];
-[MLNeuralNetworksCompileTimeParams initWithLossType:optimizerType:optimizerParameters:lossParameters:trainableLayerNames:updateParameters:];
-[MLNeuralNetworksCompileTimeParams lossParameters];
-[MLNeuralNetworksCompileTimeParams lossType];
-[MLNeuralNetworksCompileTimeParams optimizerParameters];
-[MLNeuralNetworksCompileTimeParams optimizerType];
-[MLNeuralNetworksCompileTimeParams setLossParameters:];
-[MLNeuralNetworksCompileTimeParams setLossType:];
-[MLNeuralNetworksCompileTimeParams setOptimizerParameters:];
-[MLNeuralNetworksCompileTimeParams setOptimizerType:];
-[MLNeuralNetworksCompileTimeParams setTrainableLayerNames:];
-[MLNeuralNetworksCompileTimeParams setUpdateParameters:];
-[MLNeuralNetworksCompileTimeParams trainableLayerNames];
-[MLNeuralNetworksCompileTimeParams unarchiveUpdatableParamsAtURL:error:];
-[MLNeuralNetworksCompileTimeParams writeUpdatableParamsToURL:error:];
```
