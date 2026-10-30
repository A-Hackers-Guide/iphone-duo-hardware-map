# `UIDocumentPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIDocumentBrowserViewControllerPrivateDelegate`, `_UIRemoteViewControllerContaining`, `UIAdaptivePresentationControllerDelegate`
- 13 instance variables, 27 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"<UIDocumentPickerDelegate>" _weak_delegate;
@"NSMutableArray" _securityScopedURLs;
B _ignoreApplicationEntitlementForImport;
B _allowsMultipleSelection;
B _isContentManaged;
B _automaticallyDismissesAfterCompletion;
@"<UIDocumentPickerDelegate>" _delegate;
Q _documentPickerMode;
@"NSURL" _directoryURL;
@"NSArray" _documentTypes;
@"UIViewController" _childViewController;
@"NSArray" _uploadURLs;
@"DOCConfiguration" _configuration;
```

## Properties

```
@property (TQ,N,V_documentPickerMode) documentPickerMode;
@property (T@"NSArray",C,N,V_documentTypes) documentTypes;
@property (T@"UIViewController",&,N,G_childViewController,S_setChildViewController:,V_childViewController) childViewController;
@property (T@"NSArray",C,N,V_uploadURLs) uploadURLs;
@property (T@"NSMutableArray",&,N,V_securityScopedURLs) _securityScopedURLs;
@property (T@"DOCConfiguration",&,N,V_configuration) configuration;
@property (TB,N,G_ignoreApplicationEntitlementForImport,S_setIgnoreApplicationEntitlementForImport:,V_ignoreApplicationEntitlementForImport) _ignoreApplicationEntitlementForImport;
@property (TB,N,G_isContentManaged,S_setIsContentManaged:,V_isContentManaged) isContentManaged;
@property (TB,D,N,G_sourceIsManaged,S_setSourceIsManaged:) sourceIsManaged;
@property (TB,N,G_automaticallyDismissesAfterCompletion,S_setAutomaticallyDismissesAfterCompletion:,V_automaticallyDismissesAfterCompletion) automaticallyDismissesAfterCompletion;
@property (TQ,N) pickerUserInterfaceStyle;
@property (TB,N,G_forPickingDownloadsFolder,S_setForPickingDownloadsFolder:) forPickingDownloadsFolder;
@property (TB,N,G_ignoreApplicationEntitlementForImport,S_setIgnoreApplicationEntitlementForImport:) _ignoreApplicationEntitlementForImport;
@property (TB,N,G_isContentManaged,S_setIsContentManaged:) isContentManaged;
@property (TB,N,G_sourceIsManaged,S_setSourceIsManaged:) sourceIsManaged;
@property (TB,N,G_automaticallyDismissesAfterCompletion,S_setAutomaticallyDismissesAfterCompletion:) automaticallyDismissesAfterCompletion;
@property (TQ,N) pickerUserInterfaceStyle;
@property (TB,N,G_forPickingDownloadsFolder,S_setForPickingDownloadsFolder:) forPickingDownloadsFolder;
@property (T@"<UIDocumentPickerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_allowsMultipleSelection) allowsMultipleSelection;
@property (TB,N) shouldShowFileExtensions;
@property (T@"NSURL",C,N,V_directoryURL) directoryURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIRemoteViewController",R,N) _containedRemoteViewController;
```

## Instance methods

```
-[UIDocumentPickerViewController presentationControllerDidDismiss:];
-[UIDocumentPickerViewController preferredContentSizeDidChangeForChildContentContainer:];
-[UIDocumentPickerViewController setAllowsMultipleSelection:];
-[UIDocumentPickerViewController _containedRemoteViewController];
-[UIDocumentPickerViewController dealloc];
-[UIDocumentPickerViewController setConfiguration:];
-[UIDocumentPickerViewController viewDidLoad];
-[UIDocumentPickerViewController _sourceIsManaged];
-[UIDocumentPickerViewController initWithNibName:bundle:];
-[UIDocumentPickerViewController viewWillAppear:];
-[UIDocumentPickerViewController setDelegate:];
-[UIDocumentPickerViewController configuration];
-[UIDocumentPickerViewController delegate];
-[UIDocumentPickerViewController initWithCoder:];
-[UIDocumentPickerViewController modalPresentationStyle];
-[UIDocumentPickerViewController _consumeSandboxExtensionForURL:];
-[UIDocumentPickerViewController _automaticallyDismissesAfterCompletion];
-[UIDocumentPickerViewController _callDelegateWithSelectedURLsAndDismiss:];
-[UIDocumentPickerViewController _childViewController];
-[UIDocumentPickerViewController _didTapCancel];
-[UIDocumentPickerViewController _forPickingDownloadsFolder];
-[UIDocumentPickerViewController _ignoreApplicationEntitlementForImport];
-[UIDocumentPickerViewController _initForImportingDocumentsWithConversionRules:];
-[UIDocumentPickerViewController _initIgnoringApplicationEntitlementForImportOfTypes:];
-[UIDocumentPickerViewController _isContentManaged];
-[UIDocumentPickerViewController _securityScopedURLs];
-[UIDocumentPickerViewController _setAutomaticallyDismissesAfterCompletion:];
-[UIDocumentPickerViewController _setChildViewController:];
-[UIDocumentPickerViewController _setForPickingDownloadsFolder:];
-[UIDocumentPickerViewController _setIgnoreApplicationEntitlementForImport:];
-[UIDocumentPickerViewController _setIsContentManaged:];
-[UIDocumentPickerViewController _setSourceIsManaged:];
-[UIDocumentPickerViewController _tellDelegateDocumentPickerWasCancelled];
-[UIDocumentPickerViewController _viewControllerPresentationDidInitiate];
-[UIDocumentPickerViewController allowsMultipleSelection];
-[UIDocumentPickerViewController directoryURL];
-[UIDocumentPickerViewController documentBrowser:didPickDocumentURLs:];
-[UIDocumentPickerViewController documentManagerWasCancelled:];
-[UIDocumentPickerViewController documentPickerMode];
-[UIDocumentPickerViewController documentTypes];
-[UIDocumentPickerViewController initForExportingURLs:];
-[UIDocumentPickerViewController initForExportingURLs:asCopy:];
-[UIDocumentPickerViewController initForOpeningContentTypes:];
-[UIDocumentPickerViewController initForOpeningContentTypes:asCopy:];
-[UIDocumentPickerViewController initWithDocumentTypes:inMode:];
-[UIDocumentPickerViewController initWithURL:inMode:];
-[UIDocumentPickerViewController initWithURLs:inMode:];
-[UIDocumentPickerViewController pickerUserInterfaceStyle];
-[UIDocumentPickerViewController setDirectoryURL:];
-[UIDocumentPickerViewController setDocumentPickerMode:];
-[UIDocumentPickerViewController setDocumentTypes:];
-[UIDocumentPickerViewController setPickerUserInterfaceStyle:];
-[UIDocumentPickerViewController setShouldShowFileExtensions:];
-[UIDocumentPickerViewController setUploadURLs:];
-[UIDocumentPickerViewController set_securityScopedURLs:];
-[UIDocumentPickerViewController shouldShowFileExtensions];
-[UIDocumentPickerViewController uploadURLs];
```
