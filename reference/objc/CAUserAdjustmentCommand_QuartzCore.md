# `CAUserAdjustmentCommand`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _minXDelta;
d _maxXDelta;
d _minYDelta;
d _maxYDelta;
d _minLuminanceScale;
d _maxLuminanceScale;
@"CAUserAdjustment" _userAdjustment;
```

## Properties

```
@property (Td,R,V_minXDelta) minXDelta;
@property (Td,R,V_maxXDelta) maxXDelta;
@property (Td,R,V_minYDelta) minYDelta;
@property (Td,R,V_maxYDelta) maxYDelta;
@property (Td,R,V_minLuminanceScale) minLuminanceScale;
@property (Td,R,V_maxLuminanceScale) maxLuminanceScale;
@property (T@"CAUserAdjustment",R,V_userAdjustment) userAdjustment;
```

## Instance methods

```
-[CAUserAdjustmentCommand dealloc];
-[CAUserAdjustmentCommand initWithUserAdjustment:autoLuminanceBoost:];
-[CAUserAdjustmentCommand maxLuminanceScale];
-[CAUserAdjustmentCommand maxXDelta];
-[CAUserAdjustmentCommand maxYDelta];
-[CAUserAdjustmentCommand minLuminanceScale];
-[CAUserAdjustmentCommand minXDelta];
-[CAUserAdjustmentCommand minYDelta];
-[CAUserAdjustmentCommand transformWhitePointByXDelta:yDelta:luminanceScale:];
-[CAUserAdjustmentCommand userAdjustment];
```
