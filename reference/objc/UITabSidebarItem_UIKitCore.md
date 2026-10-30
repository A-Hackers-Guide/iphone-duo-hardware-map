# `UITabSidebarItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"UIListContentConfiguration" _defaultContentConfiguration;
@"UIBackgroundConfiguration" _defaultBackgroundConfiguration;
Q _attributes;
@"<UIContentConfiguration>" _contentConfiguration;
@"UIBackgroundConfiguration" _backgroundConfiguration;
@"NSArray" _accessories;
@"UITab" _tab;
@"UIAction" _action;
@"UICellConfigurationState" _configurationState;
```

## Properties

```
@property (T@"UITab",R,N,V_tab) tab;
@property (T@"UIAction",R,N,V_action) action;
@property (T@"UICellConfigurationState",R,N,V_configurationState) configurationState;
@property (T@"<UIContentConfiguration>",C,N,V_contentConfiguration) contentConfiguration;
@property (T@"UIBackgroundConfiguration",C,N,V_backgroundConfiguration) backgroundConfiguration;
@property (T@"NSArray",C,N,V_accessories) accessories;
```

## Class methods

```
+[UITabSidebarItem itemFromRequest:];
```

## Instance methods

```
-[UITabSidebarItem accessories];
-[UITabSidebarItem action];
-[UITabSidebarItem setAccessories:];
-[UITabSidebarItem setBackgroundConfiguration:];
-[UITabSidebarItem backgroundConfiguration];
-[UITabSidebarItem copyWithZone:];
-[UITabSidebarItem isEqual:];
-[UITabSidebarItem tab];
-[UITabSidebarItem _initWithItem:];
-[UITabSidebarItem _initWithRequest:];
-[UITabSidebarItem _resolvedAccessories];
-[UITabSidebarItem _resolvedImageForState:];
-[UITabSidebarItem _shouldUpdateImageForSelectedStateChange];
-[UITabSidebarItem _updatedItemUsingState:];
-[UITabSidebarItem configurationState];
-[UITabSidebarItem contentConfiguration];
-[UITabSidebarItem defaultBackgroundConfiguration];
-[UITabSidebarItem defaultContentConfiguration];
-[UITabSidebarItem setContentConfiguration:];
```
