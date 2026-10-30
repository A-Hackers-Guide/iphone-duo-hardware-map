# `PKToolPickerCustomItemConfiguration`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _allowsColorSelection;
B _supportsLassoToolEditingView;
@"NSString" _identifier;
@"NSString" _name;
@? _imageProvider;
@? _viewControllerProvider;
d _defaultWidth;
@"NSDictionary" _widthVariants;
@"UIColor" _defaultColor;
Q _toolAttributeControls;
```

## Properties

```
@property (TB,N,S_setSupportsLassoToolEditingView:,V_supportsLassoToolEditingView) _supportsLassoToolEditingView;
@property (TB,N,S_setSupportsLassoBehaviors:) _supportsLassoBehaviors;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_name) name;
@property (T@?,C,N,V_imageProvider) imageProvider;
@property (T@?,C,N,V_viewControllerProvider) viewControllerProvider;
@property (Td,N,V_defaultWidth) defaultWidth;
@property (T@"NSDictionary",C,N,V_widthVariants) widthVariants;
@property (T@"UIColor",&,N,V_defaultColor) defaultColor;
@property (TB,N,V_allowsColorSelection) allowsColorSelection;
@property (TQ,N,V_toolAttributeControls) toolAttributeControls;
```

## Instance methods

```
-[PKToolPickerCustomItemConfiguration identifier];
-[PKToolPickerCustomItemConfiguration setDefaultColor:];
-[PKToolPickerCustomItemConfiguration defaultColor];
-[PKToolPickerCustomItemConfiguration setIdentifier:];
-[PKToolPickerCustomItemConfiguration imageProvider];
-[PKToolPickerCustomItemConfiguration hash];
-[PKToolPickerCustomItemConfiguration setName:];
-[PKToolPickerCustomItemConfiguration defaultWidth];
-[PKToolPickerCustomItemConfiguration copyWithZone:];
-[PKToolPickerCustomItemConfiguration setImageProvider:];
-[PKToolPickerCustomItemConfiguration name];
-[PKToolPickerCustomItemConfiguration initWithIdentifier:name:];
-[PKToolPickerCustomItemConfiguration _setSupportsLassoBehaviors:];
-[PKToolPickerCustomItemConfiguration _setSupportsLassoToolEditingView:];
-[PKToolPickerCustomItemConfiguration _supportsLassoBehaviors];
-[PKToolPickerCustomItemConfiguration _supportsLassoToolEditingView];
-[PKToolPickerCustomItemConfiguration allowsColorSelection];
-[PKToolPickerCustomItemConfiguration setAllowsColorSelection:];
-[PKToolPickerCustomItemConfiguration setDefaultWidth:];
-[PKToolPickerCustomItemConfiguration setToolAttributeControls:];
-[PKToolPickerCustomItemConfiguration setViewControllerProvider:];
-[PKToolPickerCustomItemConfiguration setWidthVariants:];
-[PKToolPickerCustomItemConfiguration toolAttributeControls];
-[PKToolPickerCustomItemConfiguration viewControllerProvider];
-[PKToolPickerCustomItemConfiguration widthVariants];
```
