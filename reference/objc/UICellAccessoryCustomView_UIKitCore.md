# `UICellAccessoryCustomView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICellAccessory`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _maintainsFixedSize;
@"UIView" _customView;
q _placement;
@? _position;
```

## Properties

```
@property (T@"UIView",R,N,V_customView) customView;
@property (Tq,R,N,V_placement) placement;
@property (TB,N,V_maintainsFixedSize) maintainsFixedSize;
@property (T@?,C,N,V_position) position;
```

## Class methods

```
+[UICellAccessoryCustomView supportsSecureCoding];
```

## Instance methods

```
-[UICellAccessoryCustomView customView];
-[UICellAccessoryCustomView position];
-[UICellAccessoryCustomView placement];
-[UICellAccessoryCustomView _canDirectlyUpdateExistingAccessoryViewFrom:];
-[UICellAccessoryCustomView encodeWithCoder:];
-[UICellAccessoryCustomView hash];
-[UICellAccessoryCustomView initWithCoder:];
-[UICellAccessoryCustomView setPosition:];
-[UICellAccessoryCustomView copyWithZone:];
-[UICellAccessoryCustomView isEqual:];
-[UICellAccessoryCustomView _identifier];
-[UICellAccessoryCustomView _defaultPlacementForHeader:];
-[UICellAccessoryCustomView _isSystemType];
-[UICellAccessoryCustomView initWithCustomView:placement:];
-[UICellAccessoryCustomView maintainsFixedSize];
-[UICellAccessoryCustomView setMaintainsFixedSize:];
```
