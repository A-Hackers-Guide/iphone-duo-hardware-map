# `UIBarButtonItemStateAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIBarButtonItemAppearance" _owner;
q _state;
@"_UIBarButtonItemData" _data;
@"NSArray" _itemEffects;
```

## Properties

```
@property (T@"_UIBarButtonItemData",&,N,V_data) data;
@property (T@"NSArray",C,N,V_itemEffects) itemEffects;
@property (T@"NSDictionary",C,N) titleTextAttributes;
@property (T{UIOffset=dd},N) titlePositionAdjustment;
@property (T@"UIImage",&,N) backgroundImage;
@property (T{UIOffset=dd},N) backgroundImagePositionAdjustment;
```

## Instance methods

```
-[UIBarButtonItemStateAppearance setBackgroundImage:];
-[UIBarButtonItemStateAppearance backgroundImage];
-[UIBarButtonItemStateAppearance setTitlePositionAdjustment:];
-[UIBarButtonItemStateAppearance init];
-[UIBarButtonItemStateAppearance data];
-[UIBarButtonItemStateAppearance setData:];
-[UIBarButtonItemStateAppearance setTitleTextAttributes:];
-[UIBarButtonItemStateAppearance titleTextAttributes];
-[UIBarButtonItemStateAppearance titlePositionAdjustment];
-[UIBarButtonItemStateAppearance _writeToStorage:];
-[UIBarButtonItemStateAppearance setItemEffects:];
-[UIBarButtonItemStateAppearance _clearOwner];
-[UIBarButtonItemStateAppearance _initWithOwner:data:state:];
-[UIBarButtonItemStateAppearance backgroundImagePositionAdjustment];
-[UIBarButtonItemStateAppearance itemEffects];
-[UIBarButtonItemStateAppearance setBackgroundImagePositionAdjustment:];
```
