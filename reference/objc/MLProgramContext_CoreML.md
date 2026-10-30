# `MLProgramContext`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _functionNameToInputLayersNames;
@"NSDictionary" _functionNameToOutputLayersNames;
@"<MLFeatureProvider>" _executionState;
@"NSString" _trainFunctionLossName;
@"NSString" _forwardFunctionLossName;
@"NSDictionary" _functionNameToStateMap;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_functionNameToInputLayersNames) functionNameToInputLayersNames;
@property (T@"NSDictionary",&,N,V_functionNameToOutputLayersNames) functionNameToOutputLayersNames;
@property (T@"<MLFeatureProvider>",&,N,V_executionState) executionState;
@property (T@"NSString",&,N,V_trainFunctionLossName) trainFunctionLossName;
@property (T@"NSString",&,N,V_forwardFunctionLossName) forwardFunctionLossName;
@property (T@"NSDictionary",&,N,V_functionNameToStateMap) functionNameToStateMap;
```

## Instance methods

```
-[MLProgramContext functionNameToInputLayersNames];
-[MLProgramContext functionNameToOutputLayersNames];
-[MLProgramContext setFunctionNameToOutputLayersNames:];
-[MLProgramContext setFunctionNameToInputLayersNames:];
-[MLProgramContext executionState];
-[MLProgramContext forwardFunctionLossName];
-[MLProgramContext functionNameToStateMap];
-[MLProgramContext initWithExecutionState:functionNameToStateMap:];
-[MLProgramContext setExecutionState:];
-[MLProgramContext setForwardFunctionLossName:];
-[MLProgramContext setFunctionNameToStateMap:];
-[MLProgramContext setTrainFunctionLossName:];
-[MLProgramContext trainFunctionLossName];
```
