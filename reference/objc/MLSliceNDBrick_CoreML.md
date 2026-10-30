# `MLSliceNDBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 11 instance variables, 15 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _shapeInfoNeeded;
i _rank;
@"NSArray" _begin_ids;
@"NSArray" _begin_masks;
@"NSArray" _end_ids;
@"NSArray" _end_masks;
@"NSArray" _strides;
@"NSArray" _inputRanks;
@"NSArray" _outputRanks;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
```

## Properties

```
@property (Ti,R,N,V_rank) rank;
@property (TB,R,N,V_shapeInfoNeeded) shapeInfoNeeded;
@property (T@"NSArray",R,N,V_begin_ids) begin_ids;
@property (T@"NSArray",R,N,V_begin_masks) begin_masks;
@property (T@"NSArray",R,N,V_end_ids) end_ids;
@property (T@"NSArray",R,N,V_end_masks) end_masks;
@property (T@"NSArray",R,N,V_strides) strides;
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
-[MLSliceNDBrick rank];
-[MLSliceNDBrick initWithParameters:];
-[MLSliceNDBrick strides];
-[MLSliceNDBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLSliceNDBrick hasGPUSupport];
-[MLSliceNDBrick setupForInputShapes:withParameters:];
-[MLSliceNDBrick end_ids];
-[MLSliceNDBrick shapeInfoNeeded];
-[MLSliceNDBrick begin_ids];
-[MLSliceNDBrick begin_masks];
-[MLSliceNDBrick end_masks];
-[MLSliceNDBrick inputRanks];
-[MLSliceNDBrick inputShapes];
-[MLSliceNDBrick outputRanks];
-[MLSliceNDBrick outputShapes];
```
