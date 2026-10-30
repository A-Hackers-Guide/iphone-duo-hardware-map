# `MLBatchedMatMulBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 7 instance variables, 11 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _shapeInfoNeeded;
@"NSNumber" _transposeA;
@"NSNumber" _transposeB;
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
@property (TB,R,N,V_shapeInfoNeeded) shapeInfoNeeded;
@property (T@"NSNumber",R,N,V_transposeA) transposeA;
@property (T@"NSNumber",R,N,V_transposeB) transposeB;
@property (T@"NSArray",R,N,V_inputRanks) inputRanks;
@property (T@"NSArray",R,N,V_outputRanks) outputRanks;
@property (T@"NSArray",R,N,V_inputShapes) inputShapes;
@property (T@"NSArray",R,N,V_outputShapes) outputShapes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLBatchedMatMulBrick initWithParameters:];
-[MLBatchedMatMulBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLBatchedMatMulBrick hasGPUSupport];
-[MLBatchedMatMulBrick setupForInputShapes:withParameters:];
-[MLBatchedMatMulBrick shapeInfoNeeded];
-[MLBatchedMatMulBrick inputRanks];
-[MLBatchedMatMulBrick inputShapes];
-[MLBatchedMatMulBrick outputRanks];
-[MLBatchedMatMulBrick outputShapes];
-[MLBatchedMatMulBrick transposeA];
-[MLBatchedMatMulBrick transposeB];
```
