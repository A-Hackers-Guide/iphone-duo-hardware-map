# `_MLNeuralNetworkBasicTensorDataStore`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_MLNeuralNetworkTensorDataStoring`
- 1 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableData" _data;
```

## Properties

```
@property (T@"NSMutableData",R,N,V_data) data;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MLNeuralNetworkBasicTensorDataStore initWithContentsOfFile:error:];
-[_MLNeuralNetworkBasicTensorDataStore data];
-[_MLNeuralNetworkBasicTensorDataStore initWithData:];
-[_MLNeuralNetworkBasicTensorDataStore tensorDataForOffset:expectedLength:];
-[_MLNeuralNetworkBasicTensorDataStore writeToFile:error:];
```
