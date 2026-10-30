# `UIPreviewAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPreviewActionItem_Internal`, `NSCopying`, `UIPreviewActionItem`
- 6 instance variables, 10 properties, 15 instance methods, 6 class methods

## Instance variables

```
@"NSString" _title;
@"UIImage" _image;
@"NSString" _identifier;
@"UIColor" _color;
q _style;
@? _handler;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (Tq,N,V_style) style;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIColor",&,N,G_color,S_setColor:,V_color) color;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPreviewAction _checkmarkImage];
+[UIPreviewAction _actionWithPreviewMenuItem:];
+[UIPreviewAction _actionWithTitle:color:image:handler:];
+[UIPreviewAction _actionWithTitle:style:color:image:handler:];
+[UIPreviewAction _actionWithTitle:style:image:handler:];
+[UIPreviewAction actionWithTitle:style:handler:];
```

## Instance methods

```
-[UIPreviewAction _color];
-[UIPreviewAction _setColor:];
-[UIPreviewAction identifier];
-[UIPreviewAction setHandler:];
-[UIPreviewAction style];
-[UIPreviewAction setStyle:];
-[UIPreviewAction setIdentifier:];
-[UIPreviewAction title];
-[UIPreviewAction handler];
-[UIPreviewAction setTitle:];
-[UIPreviewAction image];
-[UIPreviewAction copyWithZone:];
-[UIPreviewAction setImage:];
-[UIPreviewAction _effectiveColor];
-[UIPreviewAction _effectiveImage];
```
