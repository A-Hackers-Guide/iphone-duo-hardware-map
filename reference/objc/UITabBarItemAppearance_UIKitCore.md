# `UITabBarItemAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 7 properties, 26 instance methods, 1 class methods

## Instance variables

```
[5@"UITabBarItemStateAppearance"] _states;
@"_UITabBarItemData" _data;
@"UITabBarAppearance" _owningAppearance;
```

## Properties

```
@property (T@"_UITabBarItemData",&,N,S_setData:,V_data) _data;
@property (T@"UITabBarAppearance",W,N,S_setOwningAppearance:,V_owningAppearance) _owningAppearance;
@property (T@"UITabBarItemStateAppearance",R,N) highlighted;
@property (T@"UITabBarItemStateAppearance",R,N) normal;
@property (T@"UITabBarItemStateAppearance",R,N) selected;
@property (T@"UITabBarItemStateAppearance",R,N) disabled;
@property (T@"UITabBarItemStateAppearance",R,N) focused;
```

## Class methods

```
+[UITabBarItemAppearance supportsSecureCoding];
```

## Instance methods

```
-[UITabBarItemAppearance disabled];
-[UITabBarItemAppearance normal];
-[UITabBarItemAppearance focused];
-[UITabBarItemAppearance init];
-[UITabBarItemAppearance copy];
-[UITabBarItemAppearance dealloc];
-[UITabBarItemAppearance configureWithDefaultForStyle:];
-[UITabBarItemAppearance highlighted];
-[UITabBarItemAppearance initWithStyle:];
-[UITabBarItemAppearance _describeInto:];
-[UITabBarItemAppearance _setData:];
-[UITabBarItemAppearance _data];
-[UITabBarItemAppearance encodeWithCoder:];
-[UITabBarItemAppearance _proxyForState:];
-[UITabBarItemAppearance hash];
-[UITabBarItemAppearance description];
-[UITabBarItemAppearance initWithCoder:];
-[UITabBarItemAppearance copyWithZone:];
-[UITabBarItemAppearance isEqual:];
-[UITabBarItemAppearance selected];
-[UITabBarItemAppearance _writeToStorage:];
-[UITabBarItemAppearance _initWithTabBarItemData:];
-[UITabBarItemAppearance _owningAppearance];
-[UITabBarItemAppearance _setOwningAppearance:];
-[UITabBarItemAppearance _updateDataTo:];
-[UITabBarItemAppearance initWithTabBarItemAppearance:];
```
