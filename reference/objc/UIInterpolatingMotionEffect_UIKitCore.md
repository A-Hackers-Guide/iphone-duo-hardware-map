# `UIInterpolatingMotionEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMotionEffect`
- 6 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
d _horizontalAccelerationBoostFactor;
d _verticalAccelerationBoostFactor;
@"NSString" _keyPath;
q _type;
@ _minimumRelativeValue;
@ _maximumRelativeValue;
```

## Properties

```
@property (T@"NSString",R,N,V_keyPath) keyPath;
@property (Tq,R,N,V_type) type;
@property (T@,&,N,V_minimumRelativeValue) minimumRelativeValue;
@property (T@,&,N,V_maximumRelativeValue) maximumRelativeValue;
```

## Instance methods

```
-[UIInterpolatingMotionEffect keyPath];
-[UIInterpolatingMotionEffect init];
-[UIInterpolatingMotionEffect type];
-[UIInterpolatingMotionEffect encodeWithCoder:];
-[UIInterpolatingMotionEffect description];
-[UIInterpolatingMotionEffect initWithCoder:];
-[UIInterpolatingMotionEffect copyWithZone:];
-[UIInterpolatingMotionEffect _setType:];
-[UIInterpolatingMotionEffect _horizontalAccelerationBoostFactor];
-[UIInterpolatingMotionEffect _keyPathsAndRelativeValuesForPose:];
-[UIInterpolatingMotionEffect _setHorizontalAccelerationBoostFactor:];
-[UIInterpolatingMotionEffect _setKeyPath:];
-[UIInterpolatingMotionEffect _setVerticalAccelerationBoostFactor:];
-[UIInterpolatingMotionEffect _verticalAccelerationBoostFactor];
-[UIInterpolatingMotionEffect initWithKeyPath:type:];
-[UIInterpolatingMotionEffect keyPathsAndRelativeValuesForViewerOffset:];
-[UIInterpolatingMotionEffect maximumRelativeValue];
-[UIInterpolatingMotionEffect minimumRelativeValue];
-[UIInterpolatingMotionEffect setMaximumRelativeValue:];
-[UIInterpolatingMotionEffect setMinimumRelativeValue:];
```
