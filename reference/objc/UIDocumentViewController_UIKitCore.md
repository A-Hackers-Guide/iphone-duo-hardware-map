# `UIDocumentViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 9 instance variables, 3 properties, 38 instance methods, 0 class methods

## Instance variables

```
{?="isPresentedFromDocumentBrowser"b1"hasReceivedDocumentDidOpen"b1"needsDocumentUnavailableConfigurationUpdate"b1} _flags;
@"UIDocumentViewControllerLaunchOptions" _launchOptions;
@"UIBarButtonItemGroup" _undoRedoItemGroup;
@"NSObject<OS_dispatch_queue>" _documentBackgroundQueue;
@"_UIDocumentLaunchViewController" _launchViewController;
@"UIDocument" _document;
Q _lastKnownState;
@"_UIBarButtonItemActionBinding" _undoManagerBinding;
@"_UIDocumentMovedPopoverViewController" _documentMovedPopover;
```

## Properties

```
@property (T@"UIDocument",&,N,V_document) document;
@property (T@"UIDocumentViewControllerLaunchOptions",&,N,V_launchOptions) launchOptions;
@property (T@"UIBarButtonItemGroup",R,N,V_undoRedoItemGroup) undoRedoItemGroup;
```

## Instance methods

```
-[UIDocumentViewController undo:];
-[UIDocumentViewController observeValueForKeyPath:ofObject:change:context:];
-[UIDocumentViewController document];
-[UIDocumentViewController open:];
-[UIDocumentViewController viewIsAppearing:];
-[UIDocumentViewController undoManager];
-[UIDocumentViewController _intelligenceCollectContentIn:collector:];
-[UIDocumentViewController initWithDocument:];
-[UIDocumentViewController dealloc];
-[UIDocumentViewController setView:];
-[UIDocumentViewController setDocument:];
-[UIDocumentViewController loadView];
-[UIDocumentViewController redo:];
-[UIDocumentViewController viewWillLayoutSubviews];
-[UIDocumentViewController _edgeInsetsForChildViewController:insetsAreAbsolute:];
-[UIDocumentViewController didMoveToParentViewController:];
-[UIDocumentViewController canPerformAction:withSender:];
-[UIDocumentViewController documentDidOpen];
-[UIDocumentViewController _closeDocumentIfNecessary:completionHandler:];
-[UIDocumentViewController _documentDidMoveToWritableLocation:];
-[UIDocumentViewController _documentDidOpen];
-[UIDocumentViewController _documentStateChanged:];
-[UIDocumentViewController _localizedNameChanged:];
-[UIDocumentViewController _performDocumentUnavailableConfigurationUpdate];
-[UIDocumentViewController _performOpenByClosingExistingDocument];
-[UIDocumentViewController _registerDocumentAssociation];
-[UIDocumentViewController _registerDocumentObservers];
-[UIDocumentViewController _unregisterDocumentAssociation];
-[UIDocumentViewController _unregisterDocumentObservers];
-[UIDocumentViewController _updateIsPresentedFromDocumentBrowser];
-[UIDocumentViewController _updateNavigationItem];
-[UIDocumentViewController _updateUndoManagerBinding];
-[UIDocumentViewController launchOptions];
-[UIDocumentViewController navigationItemDidUpdate];
-[UIDocumentViewController openDocumentWithCompletionHandler:];
-[UIDocumentViewController setLaunchOptions:];
-[UIDocumentViewController undoRedoItemGroup];
-[UIDocumentViewController updateContentUnavailableConfigurationUsingState:];
```
