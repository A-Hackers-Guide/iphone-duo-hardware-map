# `MLPowBroadcastableBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 5 instance variables, 9 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _shapeInfoNeeded;
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
@property (TB,R,N,V_shapeInfoNeeded) shapeInfoNeeded;
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
-[MLPowBroadcastableBrick initWithParameters:];
-[MLPowBroadcastableBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLPowBroadcastableBrick hasGPUSupport];
-[MLPowBroadcastableBrick setupForInputShapes:withParameters:];
-[MLPowBroadcastableBrick shapeInfoNeeded];
-[MLPowBroadcastableBrick inputRanks];
-[MLPowBroadcastableBrick inputShapes];
-[MLPowBroadcastableBrick outputRanks];
-[MLPowBroadcastableBrick outputShapes];
```
