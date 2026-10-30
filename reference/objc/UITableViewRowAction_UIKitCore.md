# `UITableViewRowAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _style;
@"NSString" _title;
@"UIColor" _backgroundColor;
@? _handler;
@"UIVisualEffect" _backgroundEffect;
```

## Properties

```
@property (T@?,R,N,G_handler,V_handler) handler;
@property (Tq,R,N,V_style) style;
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
@property (T@"UIVisualEffect",C,N,V_backgroundEffect) backgroundEffect;
```

## Class methods

```
+[UITableViewRowAction rowActionWithStyle:title:handler:];
```

## Instance methods

```
-[UITableViewRowAction setBackgroundEffect:];
-[UITableViewRowAction _button];
-[UITableViewRowAction style];
-[UITableViewRowAction backgroundEffect];
-[UITableViewRowAction setBackgroundColor:];
-[UITableViewRowAction title];
-[UITableViewRowAction backgroundColor];
-[UITableViewRowAction setTitle:];
-[UITableViewRowAction _handler];
-[UITableViewRowAction copyWithZone:];
-[UITableViewRowAction _initWithStyle:title:handler:];
-[UITableViewRowAction _setButton:];
```
