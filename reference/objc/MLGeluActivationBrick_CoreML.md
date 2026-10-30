# `MLGeluActivationBrick`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 1 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _size;
```

## Properties

```
@property (TQ,R,N,V_size) size;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLGeluActivationBrick initWithParameters:];
-[MLGeluActivationBrick size];
-[MLGeluActivationBrick computeOnCPUWithInputTensors:outputTensors:];
-[MLGeluActivationBrick hasGPUSupport];
-[MLGeluActivationBrick setupForInputShapes:withParameters:];
```
