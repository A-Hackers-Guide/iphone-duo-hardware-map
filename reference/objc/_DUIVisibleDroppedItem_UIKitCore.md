# `_DUIVisibleDroppedItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 13 properties, 31 instance methods, 1 class methods

## Instance variables

```
{CAPoint3D="x"d"y"d"z"d} _center;
(?=""{?="x"d"y"d"z"d"_padding"d}"vector") _velocity3D;
(?=""{?="x"d"y"d"z"d"_padding"d}"vector") _targetVelocity3D;
B _constrainSize;
B _flipped;
B _precisionMode;
Q _itemIndex;
@"_DUIImageComponent" _imageComponent;
@"_DUIPreview" _preview;
d _rotation;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _appliedTransform;
```

## Properties

```
@property (TQ,N,V_itemIndex) itemIndex;
@property (T@"_DUIImageComponent",&,N,V_imageComponent) imageComponent;
@property (T@"_DUIPreview",C,N,V_preview) preview;
@property (T{CGPoint=dd},D,N) center;
@property (T{CGAffineTransform=dddddd},N,V_appliedTransform) appliedTransform;
@property (T{CGVector=dd},N) velocity;
@property (T{CGVector=dd},N) targetVelocity;
@property (T(?={?=dddd}),N,V_velocity3D) velocity3D;
@property (T(?={?=dddd}),N,V_targetVelocity3D) targetVelocity3D;
@property (TB,N,V_constrainSize) constrainSize;
@property (TB,N,V_flipped) flipped;
@property (TB,N,V_precisionMode) precisionMode;
@property (Td,N,V_rotation) rotation;
```

## Class methods

```
+[_DUIVisibleDroppedItem supportsSecureCoding];
```

## Instance methods

```
-[_DUIVisibleDroppedItem preview];
-[_DUIVisibleDroppedItem appliedTransform];
-[_DUIVisibleDroppedItem rotation];
-[_DUIVisibleDroppedItem setFlipped:];
-[_DUIVisibleDroppedItem init];
-[_DUIVisibleDroppedItem precisionMode];
-[_DUIVisibleDroppedItem setPreview:];
-[_DUIVisibleDroppedItem setCenter:];
-[_DUIVisibleDroppedItem velocity];
-[_DUIVisibleDroppedItem setPrecisionMode:];
-[_DUIVisibleDroppedItem constrainSize];
-[_DUIVisibleDroppedItem setRotation:];
-[_DUIVisibleDroppedItem setConstrainSize:];
-[_DUIVisibleDroppedItem imageComponent];
-[_DUIVisibleDroppedItem center];
-[_DUIVisibleDroppedItem encodeWithCoder:];
-[_DUIVisibleDroppedItem velocity3D];
-[_DUIVisibleDroppedItem description];
-[_DUIVisibleDroppedItem setAppliedTransform:];
-[_DUIVisibleDroppedItem initWithCoder:];
-[_DUIVisibleDroppedItem flipped];
-[_DUIVisibleDroppedItem setVelocity:];
-[_DUIVisibleDroppedItem createSnapshotView];
-[_DUIVisibleDroppedItem itemIndex];
-[_DUIVisibleDroppedItem setImageComponent:];
-[_DUIVisibleDroppedItem setItemIndex:];
-[_DUIVisibleDroppedItem setTargetVelocity3D:];
-[_DUIVisibleDroppedItem setTargetVelocity:];
-[_DUIVisibleDroppedItem setVelocity3D:];
-[_DUIVisibleDroppedItem targetVelocity];
-[_DUIVisibleDroppedItem targetVelocity3D];
```
