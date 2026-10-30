# `MLSlidingWindowsBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 8 instance variables, 12 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _shapeInfoNeeded;
@"NSNumber" _axis;
@"NSNumber" _step;
@"NSNumber" _size;
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
@property (TB,R,N,V_shapeInfoNeeded) shapeInfoNeeded;
@property (T@"NSNumber",R,N,V_axis) axis;
@property (T@"NSNumber",R,N,V_step) step;
@property (T@"NSNumber",R,N,V_size) size;
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
-[MLSlidingWindowsBrick step];
-[MLSlidingWindowsBrick axis];
-[MLSlidingWindowsBrick initWithParameters:];
-[MLSlidingWindowsBrick size];
-[MLSlidingWindowsBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLSlidingWindowsBrick hasGPUSupport];
-[MLSlidingWindowsBrick setupForInputShapes:withParameters:];
-[MLSlidingWindowsBrick shapeInfoNeeded];
-[MLSlidingWindowsBrick inputRanks];
-[MLSlidingWindowsBrick inputShapes];
-[MLSlidingWindowsBrick outputRanks];
-[MLSlidingWindowsBrick outputShapes];
```
