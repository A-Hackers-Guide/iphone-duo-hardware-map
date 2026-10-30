# `MLNeuralNetworkFunctionInfo`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _isClassifier;
@"NSArray" _classLabels;
@"NSString" _classScoreVectorName;
@"NSArray" _outputNames;
```

## Properties

```
@property (TB,R,N,V_isClassifier) isClassifier;
@property (T@"NSArray",R,C,N,V_classLabels) classLabels;
@property (T@"NSString",R,C,N,V_classScoreVectorName) classScoreVectorName;
@property (T@"NSArray",R,C,N,V_outputNames) outputNames;
```

## Instance methods

```
-[MLNeuralNetworkFunctionInfo classLabels];
-[MLNeuralNetworkFunctionInfo initWithCompiledModelArchive:compilerVersionInfo:error:];
-[MLNeuralNetworkFunctionInfo isClassifier];
-[MLNeuralNetworkFunctionInfo description];
-[MLNeuralNetworkFunctionInfo outputNames];
-[MLNeuralNetworkFunctionInfo classScoreVectorName];
```
