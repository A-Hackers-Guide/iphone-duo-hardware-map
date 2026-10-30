# `MLConcatNDBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 6 instance variables, 10 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _shapeInfoNeeded;
@"NSNumber" _axis;
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
@property (TB,R,N,V_shapeInfoNeeded) shapeInfoNeeded;
@property (T@"NSNumber",R,N,V_axis) axis;
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
-[MLConcatNDBrick axis];
-[MLConcatNDBrick initWithParameters:];
-[MLConcatNDBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLConcatNDBrick hasGPUSupport];
-[MLConcatNDBrick setupForInputShapes:withParameters:];
-[MLConcatNDBrick shapeInfoNeeded];
-[MLConcatNDBrick inputRanks];
-[MLConcatNDBrick inputShapes];
-[MLConcatNDBrick outputRanks];
-[MLConcatNDBrick outputShapes];
```
