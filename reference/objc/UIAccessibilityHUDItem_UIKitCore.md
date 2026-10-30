# `UIAccessibilityHUDItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 22 instance methods, 2 class methods

## Instance variables

```
B _disabledAppearance;
B _flattenImage;
B _scaleImage;
q _customUserInterfaceStyle;
@"NSString" _title;
@"UIImage" _image;
@"UIView" _customView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _imageInsets;
```

## Properties

```
@property (TB,N,V_disabledAppearance) disabledAppearance;
@property (TB,N,V_flattenImage) flattenImage;
@property (TB,N,V_scaleImage) scaleImage;
@property (Tq,N,V_customUserInterfaceStyle) customUserInterfaceStyle;
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIImage",&,N,V_image) image;
@property (T{UIEdgeInsets=dddd},N,V_imageInsets) imageInsets;
@property (T@"UIView",&,N,V_customView) customView;
```

## Class methods

```
+[UIAccessibilityHUDItem HUDItemForTabBarItem:];
+[UIAccessibilityHUDItem HUDItemForBarButtonItem:atPoint:inView:isBackButton:];
```

## Instance methods

```
-[UIAccessibilityHUDItem customView];
-[UIAccessibilityHUDItem title];
-[UIAccessibilityHUDItem setCustomView:];
-[UIAccessibilityHUDItem setImageInsets:];
-[UIAccessibilityHUDItem hash];
-[UIAccessibilityHUDItem setTitle:];
-[UIAccessibilityHUDItem imageInsets];
-[UIAccessibilityHUDItem image];
-[UIAccessibilityHUDItem copyWithZone:];
-[UIAccessibilityHUDItem isEqual:];
-[UIAccessibilityHUDItem setImage:];
-[UIAccessibilityHUDItem customUserInterfaceStyle];
-[UIAccessibilityHUDItem disabledAppearance];
-[UIAccessibilityHUDItem flattenImage];
-[UIAccessibilityHUDItem initWithCustomView:];
-[UIAccessibilityHUDItem initWithTitle:image:imageInsets:];
-[UIAccessibilityHUDItem initWithTitle:image:imageInsets:scaleImage:];
-[UIAccessibilityHUDItem scaleImage];
-[UIAccessibilityHUDItem setCustomUserInterfaceStyle:];
-[UIAccessibilityHUDItem setDisabledAppearance:];
-[UIAccessibilityHUDItem setFlattenImage:];
-[UIAccessibilityHUDItem setScaleImage:];
```
