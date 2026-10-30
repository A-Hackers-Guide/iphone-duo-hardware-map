# `UISearchToken`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 2 class methods

## Instance variables

```
@ _representedObject;
@"NSString" _text;
@"UIImage" _image;
```

## Properties

```
@property (T@"NSString",C,N,V_text) text;
@property (T@"UIImage",&,N,V_image) image;
@property (T@,&,N,V_representedObject) representedObject;
```

## Class methods

```
+[UISearchToken tokenWithImage:];
+[UISearchToken tokenWithIcon:text:];
```

## Instance methods

```
-[UISearchToken text];
-[UISearchToken setText:];
-[UISearchToken image];
-[UISearchToken setImage:];
-[UISearchToken _initToken];
-[UISearchToken representedObject];
-[UISearchToken setRepresentedObject:];
```
