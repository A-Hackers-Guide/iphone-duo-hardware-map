# `MLLayerExecutionSchedule`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
q _layerError;
@"NSString" _layerName;
Q _preferredComputeUnit;
@"NSString" _layerTypeName;
Q _supportedComputeUnits;
q _layerIndex;
@"NSDictionary" _supportMessagesPerComputeUnit;
d _computeTimeRatio;
```

## Properties

```
@property (Tq,R,N,V_layerError) layerError;
@property (T@"NSString",R,C,N,V_layerName) layerName;
@property (TQ,R,N,V_preferredComputeUnit) preferredComputeUnit;
@property (T@"NSString",R,C,N,V_layerTypeName) layerTypeName;
@property (TQ,R,N,V_supportedComputeUnits) supportedComputeUnits;
@property (Tq,R,N,V_layerIndex) layerIndex;
@property (T@"NSDictionary",R,C,N,V_supportMessagesPerComputeUnit) supportMessagesPerComputeUnit;
@property (Td,R,N,V_computeTimeRatio) computeTimeRatio;
```

## Instance methods

```
-[MLLayerExecutionSchedule layerName];
-[MLLayerExecutionSchedule computeTimeRatio];
-[MLLayerExecutionSchedule initWithComputeUnits:layerName:layerError:layerTypeName:supportedComputeUnits:layerIndex:];
-[MLLayerExecutionSchedule initWithComputeUnits:layerName:layerError:layerTypeName:supportedComputeUnits:layerIndex:supportMessages:computeTimeRatio:];
-[MLLayerExecutionSchedule initWithLayerError:];
-[MLLayerExecutionSchedule layerError];
-[MLLayerExecutionSchedule layerIndex];
-[MLLayerExecutionSchedule layerTypeName];
-[MLLayerExecutionSchedule preferredComputeUnit];
-[MLLayerExecutionSchedule supportMessagesPerComputeUnit];
-[MLLayerExecutionSchedule supportedComputeUnits];
```
