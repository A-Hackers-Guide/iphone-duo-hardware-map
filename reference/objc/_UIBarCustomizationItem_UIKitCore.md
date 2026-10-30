# `_UIBarCustomizationItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _enabled;
B _collapsed;
B _removable;
B _collapsible;
B _reverseItemsForRTL;
@"NSString" _identifier;
@"NSString" _name;
@"UIImage" _icon;
@"UIView" _view;
@"UIColor" _tintColor;
@? _sourceViewProvider;
@"NSArray" _subitems;
@"_UIBarCustomizationChiclet" __chiclet;
```

## Properties

```
@property (TB,N,V_collapsible) collapsible;
@property (T@"_UIBarCustomizationChiclet",&,N,V__chiclet) _chiclet;
@property (TB,N,V_reverseItemsForRTL) reverseItemsForRTL;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_name) name;
@property (T@"UIImage",&,N,V_icon) icon;
@property (T@"UIView",&,N,V_view) view;
@property (T@"UIColor",C,N,V_tintColor) tintColor;
@property (TB,N,V_enabled) enabled;
@property (T@?,C,N,V_sourceViewProvider) sourceViewProvider;
@property (T@"NSArray",R,N,V_subitems) subitems;
@property (TB,N,V_collapsed) collapsed;
@property (TB,N,V_removable) removable;
```

## Class methods

```
+[_UIBarCustomizationItem groupWithWithIdentifier:icon:name:items:];
+[_UIBarCustomizationItem itemWithIdentifier:icon:name:view:];
```

## Instance methods

```
-[_UIBarCustomizationItem setCollapsed:];
-[_UIBarCustomizationItem enabled];
-[_UIBarCustomizationItem identifier];
-[_UIBarCustomizationItem init];
-[_UIBarCustomizationItem subitems];
-[_UIBarCustomizationItem setIcon:];
-[_UIBarCustomizationItem setView:];
-[_UIBarCustomizationItem view];
-[_UIBarCustomizationItem setSourceViewProvider:];
-[_UIBarCustomizationItem setTintColor:];
-[_UIBarCustomizationItem setEnabled:];
-[_UIBarCustomizationItem setCollapsible:];
-[_UIBarCustomizationItem description];
-[_UIBarCustomizationItem setName:];
-[_UIBarCustomizationItem tintColor];
-[_UIBarCustomizationItem name];
-[_UIBarCustomizationItem sourceViewProvider];
-[_UIBarCustomizationItem icon];
-[_UIBarCustomizationItem _chiclet];
-[_UIBarCustomizationItem _enumerateSubitemsWithBlock:];
-[_UIBarCustomizationItem _sourceFrameInContainer:];
-[_UIBarCustomizationItem collapsed];
-[_UIBarCustomizationItem collapsible];
-[_UIBarCustomizationItem removable];
-[_UIBarCustomizationItem reverseItemsForRTL];
-[_UIBarCustomizationItem setRemovable:];
-[_UIBarCustomizationItem setReverseItemsForRTL:];
-[_UIBarCustomizationItem set_chiclet:];
```
