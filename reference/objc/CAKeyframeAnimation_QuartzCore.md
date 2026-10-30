# `CAKeyframeAnimation`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAPropertyAnimation`
- 0 instance variables, 9 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",C) values;
@property (T^{CGPath=}) path;
@property (T@"NSArray",C) keyTimes;
@property (T@"NSArray",C) timingFunctions;
@property (T@"NSString",C) calculationMode;
@property (T@"NSArray",C) tensionValues;
@property (T@"NSArray",C) continuityValues;
@property (T@"NSArray",C) biasValues;
@property (T@"NSString",C) rotationMode;
```

## Instance methods

```
-[CAKeyframeAnimation values];
-[CAKeyframeAnimation _setCARenderAnimation:layer:];
-[CAKeyframeAnimation setValues:];
-[CAKeyframeAnimation CA_validateValue:forKey:];
-[CAKeyframeAnimation applyForTime:presentationObject:modelObject:];
-[CAKeyframeAnimation setPath:];
-[CAKeyframeAnimation CA_prepareRenderValue];
-[CAKeyframeAnimation path];
-[CAKeyframeAnimation _copyRenderAnimationForLayer:];
-[CAKeyframeAnimation calculationMode];
-[CAKeyframeAnimation timingFunctions];
-[CAKeyframeAnimation biasValues];
-[CAKeyframeAnimation continuityValues];
-[CAKeyframeAnimation keyTimes];
-[CAKeyframeAnimation rotationMode];
-[CAKeyframeAnimation setBiasValues:];
-[CAKeyframeAnimation setCalculationMode:];
-[CAKeyframeAnimation setContinuityValues:];
-[CAKeyframeAnimation setKeyTimes:];
-[CAKeyframeAnimation setRotationMode:];
-[CAKeyframeAnimation setTensionValues:];
-[CAKeyframeAnimation setTimingFunctions:];
-[CAKeyframeAnimation tensionValues];
```
