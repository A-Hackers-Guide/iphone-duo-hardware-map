# `DefaultSpamFilterListController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 5 instance variables, 5 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<DefaultSpamFilterListControllerDelegate>" _delegate;
@"PHCallDirectorySettingsController" _callDirectorySettingsController;
@"PHLiveLookupSettingsController" _liveLookupSettingsController;
@"CXCallDirectoryNSExtensionManager" _nsExtensionManager;
@"NSMutableSet" _appsWithExtensions;
```

## Properties

```
@property (T@"PHCallDirectorySettingsController",R,N,V_callDirectorySettingsController) callDirectorySettingsController;
@property (T@"PHLiveLookupSettingsController",R,N,V_liveLookupSettingsController) liveLookupSettingsController;
@property (T@"CXCallDirectoryNSExtensionManager",R,N,V_nsExtensionManager) nsExtensionManager;
@property (T@"NSMutableSet",&,N,V_appsWithExtensions) appsWithExtensions;
@property (T@"<DefaultSpamFilterListControllerDelegate>",&,N,V_delegate) delegate;
```

## Instance methods

```
-[DefaultSpamFilterListController tableView:canMoveRowAtIndexPath:];
-[DefaultSpamFilterListController tableView:shouldIndentWhileEditingRowAtIndexPath:];
-[DefaultSpamFilterListController tableView:editingStyleForRowAtIndexPath:];
-[DefaultSpamFilterListController tableView:moveRowAtIndexPath:toIndexPath:];
-[DefaultSpamFilterListController tableView:cellForRowAtIndexPath:];
-[DefaultSpamFilterListController setEditing:animated:];
-[DefaultSpamFilterListController initWithNibName:bundle:];
-[DefaultSpamFilterListController tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:];
-[DefaultSpamFilterListController viewWillAppear:];
-[DefaultSpamFilterListController setDelegate:];
-[DefaultSpamFilterListController delegate];
-[DefaultSpamFilterListController configureCell:];
-[DefaultSpamFilterListController reloadSpecifiers];
-[DefaultSpamFilterListController specifiers];
-[DefaultSpamFilterListController extensionCount];
-[DefaultSpamFilterListController setSwitchOn:];
-[DefaultSpamFilterListController callDirectorySettingsController];
-[DefaultSpamFilterListController _updateExtensions];
-[DefaultSpamFilterListController addCallDirectorySpecifierIfNecessary:];
-[DefaultSpamFilterListController addLiveLookupSpecifierIfNecessary:];
-[DefaultSpamFilterListController appsWithExtensions];
-[DefaultSpamFilterListController callDirectoryIdentificationIndex];
-[DefaultSpamFilterListController canEditExtensions];
-[DefaultSpamFilterListController configureCell:forSpecifier:];
-[DefaultSpamFilterListController liveLookupIdentificationIndex];
-[DefaultSpamFilterListController liveLookupSettingsController];
-[DefaultSpamFilterListController nsExtensionManager];
-[DefaultSpamFilterListController refreshView];
-[DefaultSpamFilterListController setAppsWithExtensions:];
-[DefaultSpamFilterListController setNavigationItemsForEditing:animated:];
```
