# `MLRangeBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 6 instance variables, 10 properties, 12 instance methods, 0 class methods

## Instance variables

```
i _size;
f _start;
f _stepSize;
f _startValueParameter;
f _endValueParameter;
f _stepSizeValueParameter;
```

## Properties

```
@property (Ti,R,N,V_size) size;
@property (Tf,R,N,V_start) start;
@property (Tf,R,N,V_stepSize) stepSize;
@property (Tf,R,N,V_startValueParameter) startValueParameter;
@property (Tf,R,N,V_endValueParameter) endValueParameter;
@property (Tf,R,N,V_stepSizeValueParameter) stepSizeValueParameter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLRangeBrick initWithParameters:];
-[MLRangeBrick start];
-[MLRangeBrick size];
-[MLRangeBrick stepSize];
-[MLRangeBrick computeDynamicOutputShape:];
-[MLRangeBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLRangeBrick hasDynamicOutputShape:];
-[MLRangeBrick hasGPUSupport];
-[MLRangeBrick setupForInputShapes:withParameters:];
-[MLRangeBrick endValueParameter];
-[MLRangeBrick startValueParameter];
-[MLRangeBrick stepSizeValueParameter];
```
