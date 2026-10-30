# `UIPreviewActionGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPreviewActionItem_Internal`, `NSCopying`, `UIPreviewActionItem`
- 6 instance variables, 10 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"NSString" _title;
@"UIImage" _image;
@"NSString" _identifier;
@"UIColor" _color;
q _style;
@"NSArray" _actions;
```

## Properties

```
@property (T@"NSArray",C,N,G_actions,S_setActions:,V_actions) actions;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Tq,N,V_style) style;
@property (T@"UIColor",&,N,G_color,S_setColor:,V_color) color;
@property (T@"UIImage",&,N,V_image) image;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPreviewActionGroup _actionGroupWithPreviewMenuItemWithSubactions:];
+[UIPreviewActionGroup _actionGroupWithTitle:style:color:actions:];
+[UIPreviewActionGroup actionGroupWithTitle:style:actions:];
```

## Instance methods

```
-[UIPreviewActionGroup _color];
-[UIPreviewActionGroup _setColor:];
-[UIPreviewActionGroup identifier];
-[UIPreviewActionGroup style];
-[UIPreviewActionGroup setStyle:];
-[UIPreviewActionGroup setIdentifier:];
-[UIPreviewActionGroup title];
-[UIPreviewActionGroup _actions];
-[UIPreviewActionGroup setTitle:];
-[UIPreviewActionGroup image];
-[UIPreviewActionGroup copyWithZone:];
-[UIPreviewActionGroup setImage:];
-[UIPreviewActionGroup _effectiveColor];
-[UIPreviewActionGroup _effectiveImage];
-[UIPreviewActionGroup _setActions:];
```
