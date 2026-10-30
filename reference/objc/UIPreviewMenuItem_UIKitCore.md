# `UIPreviewMenuItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"NSString" identifier;
@"NSString" _title;
@? _handler;
q _style;
@"NSArray" __subitems;
@"UIImage" _image;
@"UIColor" _color;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (T@"NSString",C,N,V_title) title;
@property (Tq,N,V_style) style;
@property (T@"NSArray",C,N,G_subitems,S_setSubitems:,V__subitems) _subitems;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIColor",&,N,G_color,S_setColor:,V_color) color;
@property (T@"NSString",C,N,Videntifier) identifier;
```

## Class methods

```
+[UIPreviewMenuItem _itemWithTitle:color:image:handler:];
+[UIPreviewMenuItem _itemWithTitle:style:image:handler:];
+[UIPreviewMenuItem itemWithTitle:style:handler:];
+[UIPreviewMenuItem itemWithTitle:style:items:];
+[UIPreviewMenuItem itemWithViewControllerPreviewAction:];
```

## Instance methods

```
-[UIPreviewMenuItem _color];
-[UIPreviewMenuItem _setColor:];
-[UIPreviewMenuItem identifier];
-[UIPreviewMenuItem setHandler:];
-[UIPreviewMenuItem style];
-[UIPreviewMenuItem setStyle:];
-[UIPreviewMenuItem setIdentifier:];
-[UIPreviewMenuItem title];
-[UIPreviewMenuItem handler];
-[UIPreviewMenuItem setTitle:];
-[UIPreviewMenuItem image];
-[UIPreviewMenuItem copyWithZone:];
-[UIPreviewMenuItem setImage:];
-[UIPreviewMenuItem _setSubitems:];
-[UIPreviewMenuItem _subitems];
```
