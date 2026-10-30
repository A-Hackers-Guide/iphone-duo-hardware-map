# `MLComputePlanDeviceUsageSupportStatePattern`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
q _supportState;
@"NSRegularExpression" _regex;
```

## Properties

```
@property (T@"NSRegularExpression",R,N,V_regex) regex;
@property (Tq,R,N,V_supportState) supportState;
```

## Class methods

```
+[MLComputePlanDeviceUsageSupportStatePattern deviceUsageSupportStatePatternWithPattern:supportState:];
```

## Instance methods

```
-[MLComputePlanDeviceUsageSupportStatePattern regex];
-[MLComputePlanDeviceUsageSupportStatePattern description];
-[MLComputePlanDeviceUsageSupportStatePattern initWithPattern:supportState:];
-[MLComputePlanDeviceUsageSupportStatePattern isMatchForValidationMessage:];
-[MLComputePlanDeviceUsageSupportStatePattern supportState];
```
