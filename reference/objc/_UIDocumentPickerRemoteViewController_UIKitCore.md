# `_UIDocumentPickerRemoteViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- Protocols: `_UIDocumentPickerViewControllerHost`, `_UIDocumentPickerServiceInvalidating`
- 2 instance variables, 6 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"UIViewController<_UIDocumentPickerRemoteViewControllerContaining>" _publicController;
@"NSString" _identifier;
```

## Properties

```
@property (T@"UIViewController<_UIDocumentPickerRemoteViewControllerContaining>",W,N,V_publicController) publicController;
@property (T@"NSString",&,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDocumentPickerRemoteViewController exportedInterface];
+[_UIDocumentPickerRemoteViewController serviceViewControllerInterface];
```

## Instance methods

```
-[_UIDocumentPickerRemoteViewController setPreferredContentSize:];
-[_UIDocumentPickerRemoteViewController identifier];
-[_UIDocumentPickerRemoteViewController viewServiceDidTerminateWithError:];
-[_UIDocumentPickerRemoteViewController viewDidLoad];
-[_UIDocumentPickerRemoteViewController invalidate];
-[_UIDocumentPickerRemoteViewController setIdentifier:];
-[_UIDocumentPickerRemoteViewController _didSelectPicker];
-[_UIDocumentPickerRemoteViewController _didSelectURLBookmark:];
-[_UIDocumentPickerRemoteViewController _didSelectURLWrapper:];
-[_UIDocumentPickerRemoteViewController _dismissViewController];
-[_UIDocumentPickerRemoteViewController _dismissWithOption:];
-[_UIDocumentPickerRemoteViewController _stitchFileCreationAtURL:];
-[_UIDocumentPickerRemoteViewController _tintColorDidChangeToColor:];
-[_UIDocumentPickerRemoteViewController publicController];
-[_UIDocumentPickerRemoteViewController setPublicController:];
```
