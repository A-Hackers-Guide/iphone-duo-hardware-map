# `_UIDocumentPickerAuxiliaryOption`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _newlyAdded;
@"NSString" _title;
@"UIImage" _image;
@"NSString" _identifier;
@? _handler;
Q _order;
```

## Properties

```
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@?,C,N,V_handler) handler;
@property (TQ,N,V_order) order;
@property (TB,N,GisNewlyAdded,V_newlyAdded) newlyAdded;
```

## Class methods

```
+[_UIDocumentPickerAuxiliaryOption supportsSecureCoding];
```

## Instance methods

```
-[_UIDocumentPickerAuxiliaryOption identifier];
-[_UIDocumentPickerAuxiliaryOption init];
-[_UIDocumentPickerAuxiliaryOption setOrder:];
-[_UIDocumentPickerAuxiliaryOption setHandler:];
-[_UIDocumentPickerAuxiliaryOption order];
-[_UIDocumentPickerAuxiliaryOption setIdentifier:];
-[_UIDocumentPickerAuxiliaryOption title];
-[_UIDocumentPickerAuxiliaryOption handler];
-[_UIDocumentPickerAuxiliaryOption encodeWithCoder:];
-[_UIDocumentPickerAuxiliaryOption initWithCoder:];
-[_UIDocumentPickerAuxiliaryOption setTitle:];
-[_UIDocumentPickerAuxiliaryOption image];
-[_UIDocumentPickerAuxiliaryOption setImage:];
-[_UIDocumentPickerAuxiliaryOption isNewlyAdded];
-[_UIDocumentPickerAuxiliaryOption setNewlyAdded:];
```
