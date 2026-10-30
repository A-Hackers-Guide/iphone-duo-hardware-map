# `CATransition`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAAnimation`
- 0 instance variables, 7 properties, 17 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",C) options;
@property (TI) transitionFlags;
@property (T@"NSString",C) type;
@property (T@"NSString",C) subtype;
@property (Tf) startProgress;
@property (Tf) endProgress;
@property (T@,&) filter;
```

## Instance methods

```
-[CATransition setSubtype:];
-[CATransition subtype];
-[CATransition startProgress];
-[CATransition filter];
-[CATransition setFilter:];
-[CATransition setTransitionFlags:];
-[CATransition setOptions:];
-[CATransition _setCARenderAnimation:layer:];
-[CATransition _propertyFlagsForLayer:];
-[CATransition setEndProgress:];
-[CATransition endProgress];
-[CATransition setStartProgress:];
-[CATransition setType:];
-[CATransition type];
-[CATransition options];
-[CATransition transitionFlags];
-[CATransition _copyRenderAnimationForLayer:];
```
