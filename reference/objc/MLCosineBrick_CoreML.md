# `MLCosineBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 4 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
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
-[MLCosineBrick initWithParameters:];
-[MLCosineBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLCosineBrick hasGPUSupport];
-[MLCosineBrick setupForInputShapes:withParameters:];
-[MLCosineBrick inputRanks];
-[MLCosineBrick inputShapes];
-[MLCosineBrick outputRanks];
-[MLCosineBrick outputShapes];
```
