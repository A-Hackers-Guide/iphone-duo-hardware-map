# `CAPropertyAnimation`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAAnimation`
- 0 instance variables, 4 properties, 13 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",C) keyPath;
@property (TB,GisAdditive) additive;
@property (TB,GisCumulative) cumulative;
@property (T@"CAValueFunction",&) valueFunction;
```

## Class methods

```
+[CAPropertyAnimation animationWithKeyPath:];
```

## Instance methods

```
-[CAPropertyAnimation isAdditive];
-[CAPropertyAnimation keyPath];
-[CAPropertyAnimation setKeyPath:];
-[CAPropertyAnimation setAdditive:];
-[CAPropertyAnimation additive];
-[CAPropertyAnimation _setCARenderAnimation:layer:];
-[CAPropertyAnimation setCumulative:];
-[CAPropertyAnimation _propertyFlagsForLayer:];
-[CAPropertyAnimation isCumulative];
-[CAPropertyAnimation applyForTime:presentationObject:modelObject:];
-[CAPropertyAnimation cumulative];
-[CAPropertyAnimation setValueFunction:];
-[CAPropertyAnimation valueFunction];
```
