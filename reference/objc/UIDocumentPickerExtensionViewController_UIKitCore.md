# `UIDocumentPickerExtensionViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIDocumentPickerExtensionViewController`
- 5 instance variables, 9 properties, 17 instance methods, 2 class methods

## Instance variables

```
Q _documentPickerMode;
@"NSURL" _originalURL;
@"NSArray" _validTypes;
@"NSString" _providerIdentifier;
@"NSURL" _documentStorageURL;
```

## Properties

```
@property (T@"NSURL",C,N,S_setUploadURL:,V_originalURL) originalURL;
@property (T@"NSArray",C,N,S_setPickableTypes:,V_validTypes) validTypes;
@property (T@"NSString",C,N,S_setProviderIdentifier:,V_providerIdentifier) providerIdentifier;
@property (T@"NSURL",C,N,S_setDocumentStorageURL:,V_documentStorageURL) documentStorageURL;
@property (TQ,N,S_setPickerMode:,V_documentPickerMode) documentPickerMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDocumentPickerExtensionViewController _exportedInterface];
+[UIDocumentPickerExtensionViewController _remoteViewControllerInterface];
```

## Instance methods

```
-[UIDocumentPickerExtensionViewController originalURL];
-[UIDocumentPickerExtensionViewController _setTintColor:];
-[UIDocumentPickerExtensionViewController providerIdentifier];
-[UIDocumentPickerExtensionViewController _setPickerMode:];
-[UIDocumentPickerExtensionViewController _documentPickerDidDismiss];
-[UIDocumentPickerExtensionViewController _prepareWithExtensionInfo:completionHandler:];
-[UIDocumentPickerExtensionViewController _setDocumentStorageURL:];
-[UIDocumentPickerExtensionViewController _setPickableTypes:];
-[UIDocumentPickerExtensionViewController _setProviderIdentifier:];
-[UIDocumentPickerExtensionViewController _setUploadURL:];
-[UIDocumentPickerExtensionViewController _setUploadURLWrapper:];
-[UIDocumentPickerExtensionViewController dismissGrantingAccessToURL:];
-[UIDocumentPickerExtensionViewController documentPickerMode];
-[UIDocumentPickerExtensionViewController documentStorageURL];
-[UIDocumentPickerExtensionViewController prepareForDocumentSelectionInMode:];
-[UIDocumentPickerExtensionViewController prepareForPresentationInMode:];
-[UIDocumentPickerExtensionViewController validTypes];
```
