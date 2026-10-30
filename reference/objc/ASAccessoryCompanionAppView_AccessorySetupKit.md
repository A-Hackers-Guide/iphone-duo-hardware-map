# `ASAccessoryCompanionAppView`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `LSApplicationWorkspaceObserverProtocol`
- 12 instance variables, 16 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _hasUpdatedUI;
B _observingAppInstall;
@? _storeProductViewHandler;
@"UIImageView" _iconView;
@"UILabel" _nameLabel;
@"UILabel" _publisherLabel;
@"UILabel" _installedLabel;
@"UIButton" _viewButton;
@"NSString" _bundleID;
@"ASAccessoryCompanionAppInfo" _appInfo;
@"NSArray" _currentConstraints;
@"LSApplicationWorkspace" _workspace;
```

## Properties

```
@property (T@"UIImageView",&,N,V_iconView) iconView;
@property (T@"UILabel",&,N,V_nameLabel) nameLabel;
@property (T@"UILabel",&,N,V_publisherLabel) publisherLabel;
@property (T@"UILabel",&,N,V_installedLabel) installedLabel;
@property (T@"UIButton",&,N,V_viewButton) viewButton;
@property (T@"NSString",&,N,V_bundleID) bundleID;
@property (T@"ASAccessoryCompanionAppInfo",&,N,V_appInfo) appInfo;
@property (T@"NSArray",&,N,V_currentConstraints) currentConstraints;
@property (TB,N,V_hasUpdatedUI) hasUpdatedUI;
@property (T@"LSApplicationWorkspace",&,N,V_workspace) workspace;
@property (TB,N,V_observingAppInstall) observingAppInstall;
@property (T@?,C,N,V_storeProductViewHandler) storeProductViewHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ASAccessoryCompanionAppView applicationsDidUninstall:];
-[ASAccessoryCompanionAppView workspace];
-[ASAccessoryCompanionAppView applicationsDidInstall:];
-[ASAccessoryCompanionAppView initWithBundleID:];
-[ASAccessoryCompanionAppView iconView];
-[ASAccessoryCompanionAppView setBundleID:];
-[ASAccessoryCompanionAppView dealloc];
-[ASAccessoryCompanionAppView setIconView:];
-[ASAccessoryCompanionAppView setAppInfo:];
-[ASAccessoryCompanionAppView willMoveToWindow:];
-[ASAccessoryCompanionAppView nameLabel];
-[ASAccessoryCompanionAppView appInfo];
-[ASAccessoryCompanionAppView updateConstraints];
-[ASAccessoryCompanionAppView setWorkspace:];
-[ASAccessoryCompanionAppView bundleID];
-[ASAccessoryCompanionAppView setNameLabel:];
-[ASAccessoryCompanionAppView setViewButton:];
-[ASAccessoryCompanionAppView viewButton];
-[ASAccessoryCompanionAppView productViewControllerDidFinish:];
-[ASAccessoryCompanionAppView _topmostViewController];
-[ASAccessoryCompanionAppView currentConstraints];
-[ASAccessoryCompanionAppView setCurrentConstraints:];
-[ASAccessoryCompanionAppView _viewButtonTapped:];
-[ASAccessoryCompanionAppView installedLabel];
-[ASAccessoryCompanionAppView publisherLabel];
-[ASAccessoryCompanionAppView setInstalledLabel:];
-[ASAccessoryCompanionAppView setPublisherLabel:];
-[ASAccessoryCompanionAppView _refreshAppInfo];
-[ASAccessoryCompanionAppView _presentStoreProductViewController];
-[ASAccessoryCompanionAppView _updateUIWithAppInfo:];
-[ASAccessoryCompanionAppView hasUpdatedUI];
-[ASAccessoryCompanionAppView initWithBundleID:appInfo:];
-[ASAccessoryCompanionAppView observingAppInstall];
-[ASAccessoryCompanionAppView setHasUpdatedUI:];
-[ASAccessoryCompanionAppView setObservingAppInstall:];
-[ASAccessoryCompanionAppView setStoreProductViewHandler:];
-[ASAccessoryCompanionAppView storeProductViewHandler];
```
