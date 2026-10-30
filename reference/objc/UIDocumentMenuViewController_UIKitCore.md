# `UIDocumentMenuViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIDocumentPickerRemoteViewControllerContaining`, `UIActionSheetPresentationControllerDelegate`
- 10 instance variables, 15 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"<UIDocumentMenuDelegate>" _weak_delegate;
B _ignoreApplicationEntitlementForImport;
B _dismissDelegateCalled;
B _isContentManaged;
@"<UIDocumentMenuDelegate>" _delegate;
@"NSMutableArray" _auxiliaryOptions;
@"_UIResilientRemoteViewContainerViewController" _childViewController;
Q _documentPickerMode;
@"NSURL" _uploadURL;
@"NSArray" _allowedUTIs;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_auxiliaryOptions) auxiliaryOptions;
@property (T@"_UIResilientRemoteViewContainerViewController",&,N,G_childViewController,S_setChildViewController:,V_childViewController) childViewController;
@property (T@"_UIDocumentPickerRemoteViewController",R,&,N,G_remoteViewController) remoteViewController;
@property (TB,N,V_dismissDelegateCalled) dismissDelegateCalled;
@property (TQ,N,V_documentPickerMode) documentPickerMode;
@property (T@"NSURL",C,N,V_uploadURL) uploadURL;
@property (T@"NSArray",C,N,V_allowedUTIs) allowedUTIs;
@property (TB,N,G_ignoreApplicationEntitlementForImport,S_setIgnoreApplicationEntitlementForImport:,V_ignoreApplicationEntitlementForImport) _ignoreApplicationEntitlementForImport;
@property (TB,N,G_isContentManaged,S_setIsContentManaged:,V_isContentManaged) isContentManaged;
@property (TB,D,N,G_sourceIsManaged,S_setSourceIsManaged:) sourceIsManaged;
@property (T@"<UIDocumentMenuDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDocumentMenuViewController preferredContentSizeDidChangeForChildContentContainer:];
-[UIDocumentMenuViewController _sourceIsManaged];
-[UIDocumentMenuViewController initWithNibName:bundle:];
-[UIDocumentMenuViewController setDelegate:];
-[UIDocumentMenuViewController delegate];
-[UIDocumentMenuViewController setModalPresentationStyle:];
-[UIDocumentMenuViewController initWithCoder:];
-[UIDocumentMenuViewController setAllowedUTIs:];
-[UIDocumentMenuViewController _childViewController];
-[UIDocumentMenuViewController _commonInitWithCompletion:];
-[UIDocumentMenuViewController _didSelectPicker];
-[UIDocumentMenuViewController _didSelectURL:];
-[UIDocumentMenuViewController _dismissViewController];
-[UIDocumentMenuViewController _dismissWithOption:];
-[UIDocumentMenuViewController _displayLocationsMenuFromRect:];
-[UIDocumentMenuViewController _ignoreApplicationEntitlementForImport];
-[UIDocumentMenuViewController _initIgnoringApplicationEntitlementForImportOfTypes:];
-[UIDocumentMenuViewController _isContentManaged];
-[UIDocumentMenuViewController _remoteViewController];
-[UIDocumentMenuViewController _setChildViewController:];
-[UIDocumentMenuViewController _setIgnoreApplicationEntitlementForImport:];
-[UIDocumentMenuViewController _setIsContentManaged:];
-[UIDocumentMenuViewController _setSourceIsManaged:];
-[UIDocumentMenuViewController _stitchFileCreationAtURL:];
-[UIDocumentMenuViewController actionSheetPresentationControllerDidDismissActionSheet:];
-[UIDocumentMenuViewController addOptionWithTitle:image:order:handler:];
-[UIDocumentMenuViewController allowedUTIs];
-[UIDocumentMenuViewController auxiliaryOptions];
-[UIDocumentMenuViewController dismissDelegateCalled];
-[UIDocumentMenuViewController documentPickerMode];
-[UIDocumentMenuViewController initWithDocumentTypes:inMode:];
-[UIDocumentMenuViewController initWithURL:inMode:];
-[UIDocumentMenuViewController setAuxiliaryOptions:];
-[UIDocumentMenuViewController setDismissDelegateCalled:];
-[UIDocumentMenuViewController setDocumentPickerMode:];
-[UIDocumentMenuViewController setUploadURL:];
-[UIDocumentMenuViewController uploadURL];
```
