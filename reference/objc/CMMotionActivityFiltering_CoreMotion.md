# `CMMotionActivityFiltering`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
d _trueRunInBout;
d _trueWalkInBout;
```

## Properties

```
@property (Td,V_trueRunInBout) trueRunInBout;
@property (Td,V_trueWalkInBout) trueWalkInBout;
```

## Class methods

```
+[CMMotionActivityFiltering isActivity:sustainedForAttribute:];
+[CMMotionActivityFiltering isTimeFromActivity:toActivity:withinLimitForAttribute:];
```

## Instance methods

```
-[CMMotionActivityFiltering init];
-[CMMotionActivityFiltering evaluateNextActivity:attribute:result:];
-[CMMotionActivityFiltering setTrueRunInBout:];
-[CMMotionActivityFiltering setTrueWalkInBout:];
-[CMMotionActivityFiltering trueRunInBout];
-[CMMotionActivityFiltering trueWalkInBout];
```
