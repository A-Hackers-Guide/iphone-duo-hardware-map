# `UIDocumentViewControllerLaunchOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDocumentLandingPresenter`, `_UIDocumentLandingPresenterDefaultDocumentCreating`
- 19 instance variables, 21 properties, 38 instance methods, 2 class methods

## Instance variables

```
{?="hasHiddenMacProxyWindow"b1"hasUpdatedDocumentTargetView"b1"isCreatingDocument"b1} _flags;
@"UIView" _documentTargetView;
@"UIColor" _tintColor;
@"UIMenu" _primaryMenu;
@"UIMenu" _secondaryMenu;
@"NSArray" _overridePasteActionUTTypes;
@"UIDocumentBrowserViewController" _browserViewController;
@"NSString" _title;
@"NSString" _subtitle;
@"UIAction" _primaryAction;
@"UIAction" _secondaryAction;
@"UIView" _foregroundAccessoryView;
@"UIView" _backgroundAccessoryView;
@"UIBackgroundConfiguration" _background;
@"UIDocumentBrowserViewController" _defaultBrowserViewController;
@"NSURL" _documentURL;
@"NSURL" _createdDocumentURL;
@"NSString" _documentCreationIntent;
@"UIDocumentViewController" __documentViewController;
```

## Properties

```
@property (T@"UIColor",&,N,S_setTintColor:,V_tintColor) _tintColor;
@property (T@"UIMenu",C,N,S_setPrimaryMenu:,V_primaryMenu) _primaryMenu;
@property (T@"UIMenu",C,N,S_setSecondaryMenu:,V_secondaryMenu) _secondaryMenu;
@property (T@"NSArray",C,N,S_setOverridePasteActionUTTypes:,V_overridePasteActionUTTypes) _overridePasteActionUTTypes;
@property (T@"UIColor",&,N,S_setTintColor:) _tintColor;
@property (T@"UIMenu",C,N,S_setPrimaryMenu:) _primaryMenu;
@property (T@"UIMenu",C,N,S_setSecondaryMenu:) _secondaryMenu;
@property (T@"NSArray",C,N,S_setOverridePasteActionUTTypes:) _overridePasteActionUTTypes;
@property (T@"UIDocumentBrowserViewController",&,N,V_browserViewController) browserViewController;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_subtitle) subtitle;
@property (T@"UIAction",C,N,V_primaryAction) primaryAction;
@property (T@"UIAction",C,N,V_secondaryAction) secondaryAction;
@property (T@"UIView",&,N) documentTargetView;
@property (T@"UIView",&,N,V_foregroundAccessoryView) foregroundAccessoryView;
@property (T@"UIView",&,N,V_backgroundAccessoryView) backgroundAccessoryView;
@property (T@"UIBackgroundConfiguration",&,N,V_background) background;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDocumentViewControllerLaunchOptions createDocumentActionWithIntent:];
+[UIDocumentViewControllerLaunchOptions _backgroundColorBlendedWithColor:];
```

## Instance methods

```
-[UIDocumentViewControllerLaunchOptions _tintColor];
-[UIDocumentViewControllerLaunchOptions primaryAction];
-[UIDocumentViewControllerLaunchOptions _setTintColor:];
-[UIDocumentViewControllerLaunchOptions subtitle];
-[UIDocumentViewControllerLaunchOptions setBackground:];
-[UIDocumentViewControllerLaunchOptions init];
-[UIDocumentViewControllerLaunchOptions setSubtitle:];
-[UIDocumentViewControllerLaunchOptions background];
-[UIDocumentViewControllerLaunchOptions title];
-[UIDocumentViewControllerLaunchOptions setPrimaryAction:];
-[UIDocumentViewControllerLaunchOptions setTitle:];
-[UIDocumentViewControllerLaunchOptions _setOverridePasteActionUTTypes:];
-[UIDocumentViewControllerLaunchOptions documentLandingBrowser:didImportDocumentAtURL:toDestinationURL:];
-[UIDocumentViewControllerLaunchOptions secondaryAction];
-[UIDocumentViewControllerLaunchOptions _dismissBrowserViewController];
-[UIDocumentViewControllerLaunchOptions _overridePasteActionUTTypes];
-[UIDocumentViewControllerLaunchOptions _prepareBrowserViewController:];
-[UIDocumentViewControllerLaunchOptions _presentAlertForDocumentAtURL:error:isImport:];
-[UIDocumentViewControllerLaunchOptions _primaryMenu];
-[UIDocumentViewControllerLaunchOptions _replaceDocumentWithDocumentAtURL:isImport:];
-[UIDocumentViewControllerLaunchOptions _secondaryMenu];
-[UIDocumentViewControllerLaunchOptions _setNeedsUpdateDocumentUnavailableConfiguration];
-[UIDocumentViewControllerLaunchOptions _setPrimaryMenu:];
-[UIDocumentViewControllerLaunchOptions _setSecondaryMenu:];
-[UIDocumentViewControllerLaunchOptions backgroundAccessoryView];
-[UIDocumentViewControllerLaunchOptions browserViewController];
-[UIDocumentViewControllerLaunchOptions documentLandingBrowser:didPickDocumentsAtURLs:];
-[UIDocumentViewControllerLaunchOptions documentLandingBrowser:didRequestDocumentCreationWithHandler:];
-[UIDocumentViewControllerLaunchOptions documentLandingBrowser:failedToImportDocumentAtURL:error:];
-[UIDocumentViewControllerLaunchOptions documentLandingBrowserDidEndDocumentCreation:importedURL:canceled:error:];
-[UIDocumentViewControllerLaunchOptions documentLandingBrowserWillStartDocumentCreation:];
-[UIDocumentViewControllerLaunchOptions documentTargetView];
-[UIDocumentViewControllerLaunchOptions foregroundAccessoryView];
-[UIDocumentViewControllerLaunchOptions setBackgroundAccessoryView:];
-[UIDocumentViewControllerLaunchOptions setBrowserViewController:];
-[UIDocumentViewControllerLaunchOptions setDocumentTargetView:];
-[UIDocumentViewControllerLaunchOptions setForegroundAccessoryView:];
-[UIDocumentViewControllerLaunchOptions setSecondaryAction:];
```
