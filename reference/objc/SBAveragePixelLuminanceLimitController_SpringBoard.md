# `SBAveragePixelLuminanceLimitController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 3 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _globalFilter;
B _aplLimitsEnabled;
@"UIView" _targetView;
```

## Properties

```
@property (TB,N,GisGlobalFilter,V_globalFilter) globalFilter;
@property (T@"UIView",W,N,V_targetView) targetView;
@property (TB,N,GareAplLimitsEnabled,V_aplLimitsEnabled) aplLimitsEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAveragePixelLuminanceLimitController targetView];
-[SBAveragePixelLuminanceLimitController animationDidStop:finished:];
-[SBAveragePixelLuminanceLimitController setTargetView:];
-[SBAveragePixelLuminanceLimitController _addFilter];
-[SBAveragePixelLuminanceLimitController _removeFilter];
-[SBAveragePixelLuminanceLimitController _targetLayer];
-[SBAveragePixelLuminanceLimitController areAplLimitsEnabled];
-[SBAveragePixelLuminanceLimitController isGlobalFilter];
-[SBAveragePixelLuminanceLimitController setAplLimitsEnabled:];
-[SBAveragePixelLuminanceLimitController setGlobalFilter:];
```
