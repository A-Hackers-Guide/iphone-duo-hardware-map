# `MLTileBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 6 instance variables, 10 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _shapeInfoNeeded;
@"NSArray" _reps;
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
@property (TB,R,N,V_shapeInfoNeeded) shapeInfoNeeded;
@property (T@"NSArray",R,N,V_reps) reps;
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
-[MLTileBrick initWithParameters:];
-[MLTileBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLTileBrick hasGPUSupport];
-[MLTileBrick setupForInputShapes:withParameters:];
-[MLTileBrick shapeInfoNeeded];
-[MLTileBrick inputRanks];
-[MLTileBrick inputShapes];
-[MLTileBrick outputRanks];
-[MLTileBrick outputShapes];
-[MLTileBrick reps];
```
