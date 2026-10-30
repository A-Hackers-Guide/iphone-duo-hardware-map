# `UITableViewCellEditControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 12 instance variables, 5 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"UITableViewCell" _cell;
@"UIImageView" _imageView;
@"UIImageView" _shadowView;
@"UIView" _backgroundView;
d _focalY;
d _focalHeight;
b2 _style;
b1 _rotated;
b1 _rotating;
b27 _reserved;
@"UIColor" _accessoryTintColor;
@"UIColor" _accessoryBackgroundColor;
```

## Properties

```
@property (TB,N,GisRotated) rotated;
@property (TB,R,N) wantsMaskingWhileAnimatingDisabled;
@property (TB,R,N) wantsImageShadow;
@property (T@"UIColor",&,N,V_accessoryTintColor) accessoryTintColor;
@property (T@"UIColor",&,N,V_accessoryBackgroundColor) accessoryBackgroundColor;
```

## Instance methods

```
-[UITableViewCellEditControl _controlEventsForActionTriggered];
-[UITableViewCellEditControl _updateImageView];
-[UITableViewCellEditControl setSelected:];
-[UITableViewCellEditControl _imageView];
-[UITableViewCellEditControl _renderedImage];
-[UITableViewCellEditControl _dynamicUserInterfaceTraitDidChange];
-[UITableViewCellEditControl setHighlighted:animated:];
-[UITableViewCellEditControl viewForLastBaselineLayout];
-[UITableViewCellEditControl layoutSubviews];
-[UITableViewCellEditControl sizeThatFits:];
-[UITableViewCellEditControl setHighlighted:];
-[UITableViewCellEditControl accessoryBackgroundColor];
-[UITableViewCellEditControl viewForFirstBaselineLayout];
-[UITableViewCellEditControl isRotating];
-[UITableViewCellEditControl traitCollectionDidChange:];
-[UITableViewCellEditControl accessoryTintColor];
-[UITableViewCellEditControl setRotated:];
-[UITableViewCellEditControl _currentImage];
-[UITableViewCellEditControl setSelected:animated:];
-[UITableViewCellEditControl setAccessoryBackgroundColor:];
-[UITableViewCellEditControl setAccessoryTintColor:];
-[UITableViewCellEditControl isRotated];
-[UITableViewCellEditControl _createImageViewIfNecessary];
-[UITableViewCellEditControl _deleteImage];
-[UITableViewCellEditControl _insertImage];
-[UITableViewCellEditControl _multiSelectNotSelectedImage];
-[UITableViewCellEditControl _multiSelectSelectedImage];
-[UITableViewCellEditControl _multiselectColorChanged];
-[UITableViewCellEditControl _replaceOrToggleImageWithDrawAnimation:];
-[UITableViewCellEditControl _shadowImage];
-[UITableViewCellEditControl _toggleRotate];
-[UITableViewCellEditControl _toggleRotateAnimationDidStop];
-[UITableViewCellEditControl _updateBackgroundViewIfNecessary];
-[UITableViewCellEditControl _useSelectedState];
-[UITableViewCellEditControl adjustLayoutForFocalRect:];
-[UITableViewCellEditControl defaultSize];
-[UITableViewCellEditControl initWithTableViewCell:editingStyle:];
-[UITableViewCellEditControl setRotated:animated:];
-[UITableViewCellEditControl wantsImageShadow];
-[UITableViewCellEditControl wantsMaskingWhileAnimatingDisabled];
```
