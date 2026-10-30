# `UITableViewCellReorderControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 6 instance variables, 2 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UITableViewCell" _cell;
{CGPoint="x"d"y"d} _downPoint;
d _focalY;
d _focalHeight;
@"UIImageView" _imageView;
@"UIColor" _accessoryTintColor;
```

## Properties

```
@property (TB,R,N) wantsMaskingWhileAnimatingDisabled;
@property (T@"UIColor",&,N,V_accessoryTintColor) accessoryTintColor;
```

## Instance methods

```
-[UITableViewCellReorderControl _updateImageView];
-[UITableViewCellReorderControl _imageView];
-[UITableViewCellReorderControl _dynamicUserInterfaceTraitDidChange];
-[UITableViewCellReorderControl setTracking:];
-[UITableViewCellReorderControl cancelTrackingWithEvent:];
-[UITableViewCellReorderControl endTrackingWithTouch:withEvent:];
-[UITableViewCellReorderControl continueTrackingWithTouch:withEvent:];
-[UITableViewCellReorderControl layoutSubviews];
-[UITableViewCellReorderControl beginTrackingWithTouch:withEvent:];
-[UITableViewCellReorderControl sizeThatFits:];
-[UITableViewCellReorderControl setFrame:];
-[UITableViewCellReorderControl accessoryTintColor];
-[UITableViewCellReorderControl setAccessoryTintColor:];
-[UITableViewCellReorderControl adjustLayoutForFocalRect:];
-[UITableViewCellReorderControl grabberImage];
-[UITableViewCellReorderControl initWithTableViewCell:];
-[UITableViewCellReorderControl shouldTrack];
-[UITableViewCellReorderControl wantsMaskingWhileAnimatingDisabled];
```
