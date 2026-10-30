# `PHCallDirectorySettingsController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CXCallDirectoryExtensionManagerDelegate`
- 4 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"CXCallDirectoryExtensionManager" _extensionManager;
@"NSMutableArray" _extensions;
@"PSListController" _parent;
@"NSArray" _specifiers;
```

## Properties

```
@property (T@"CXCallDirectoryExtensionManager",R,N,V_extensionManager) extensionManager;
@property (T@"NSMutableArray",&,N,V_extensions) extensions;
@property (T@"PSListController",R,N,V_parent) parent;
@property (T@"NSArray",&,N,V_specifiers) specifiers;
@property (TB,R,N) hasExtensions;
@property (TB,R,N) canEditExtensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHCallDirectorySettingsController tableView:moveRowAtIndexPath:toIndexPath:];
-[PHCallDirectorySettingsController setExtensions:];
-[PHCallDirectorySettingsController parent];
-[PHCallDirectorySettingsController extensions];
-[PHCallDirectorySettingsController initWithParent:];
-[PHCallDirectorySettingsController readPreferenceValue:];
-[PHCallDirectorySettingsController setPreferenceValue:specifier:];
-[PHCallDirectorySettingsController specifiers];
-[PHCallDirectorySettingsController setSpecifiers:];
-[PHCallDirectorySettingsController extensionsChangedForCallDirectoryExtensionManager:];
-[PHCallDirectorySettingsController extensionManager];
-[PHCallDirectorySettingsController createExtensionsGroupSpecifiers];
-[PHCallDirectorySettingsController _localizedExtensionTitleForExtension:];
-[PHCallDirectorySettingsController _updateExtensions];
-[PHCallDirectorySettingsController callDirectoryExtensionForSpecifier:];
-[PHCallDirectorySettingsController canEditExtensions];
-[PHCallDirectorySettingsController handleWillFinishEditing];
-[PHCallDirectorySettingsController hasExtensions];
-[PHCallDirectorySettingsController presentError:fromSettingEnabled:forExtension:];
-[PHCallDirectorySettingsController refreshView];
```
