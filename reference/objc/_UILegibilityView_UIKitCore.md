# `_UILegibilityView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 10 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _hidesImage;
@"_UILegibilitySettings" _settings;
@"UIImage" _image;
@"UIImage" _shadowImage;
d _strength;
@"UIImageView" _imageView;
@"UIImageView" _shadowImageView;
q _options;
```

## Properties

```
@property (T@"_UILegibilitySettings",&,N,V_settings) settings;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIImage",&,N,V_shadowImage) shadowImage;
@property (T@"UIImageView",&,N,V_imageView) imageView;
@property (T@"UIImageView",&,N,V_shadowImageView) shadowImageView;
@property (Tq,N,V_options) options;
@property (Tq,R,D,N) style;
@property (Td,N,V_strength) strength;
@property (TB,N,V_hidesImage) hidesImage;
@property (TB,R,N) usesColorFilters;
```

## Instance methods

```
-[_UILegibilityView usesColorFilters];
-[_UILegibilityView strength];
-[_UILegibilityView updateForChangedSettings:];
-[_UILegibilityView setOptions:];
-[_UILegibilityView updateImage];
-[_UILegibilityView shadowImage];
-[_UILegibilityView setSettings:];
-[_UILegibilityView setImageView:];
-[_UILegibilityView setStrength:];
-[_UILegibilityView setHidesImage:];
-[_UILegibilityView settings];
-[_UILegibilityView dealloc];
-[_UILegibilityView usesSecondaryColor];
-[_UILegibilityView layoutSubviews];
-[_UILegibilityView style];
-[_UILegibilityView _updateFilters];
-[_UILegibilityView sizeThatFits:];
-[_UILegibilityView setShadowImage:];
-[_UILegibilityView options];
-[_UILegibilityView image];
-[_UILegibilityView imageView];
-[_UILegibilityView drawingColor];
-[_UILegibilityView initWithSettings:strength:image:];
-[_UILegibilityView hidesImage];
-[_UILegibilityView setImage:];
-[_UILegibilityView shadowImageView];
-[_UILegibilityView initWithSettings:strength:image:shadowImage:];
-[_UILegibilityView initWithSettings:strength:image:shadowImage:options:];
-[_UILegibilityView initWithStyle:image:];
-[_UILegibilityView initWithStyle:image:shadowImage:];
-[_UILegibilityView setImage:shadowImage:];
-[_UILegibilityView setSettings:image:shadowImage:];
-[_UILegibilityView setShadowImageView:];
-[_UILegibilityView setStyle:image:shadowImage:];
```
