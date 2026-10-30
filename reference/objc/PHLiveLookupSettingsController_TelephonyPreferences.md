# `PHLiveLookupSettingsController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CXCallDirectoryExtensionManagerDelegate`
- 5 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"LiveLookupManagerProxy" _extensionManager;
@"NSMutableArray" _extensions;
@"NSObject<OS_dispatch_queue>" _queue;
@"PSListController" _parent;
@"NSArray" _specifiers;
```

## Properties

```
@property (T@"LiveLookupManagerProxy",R,N,V_extensionManager) extensionManager;
@property (T@"NSMutableArray",&,N,V_extensions) extensions;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
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
-[PHLiveLookupSettingsController tableView:moveRowAtIndexPath:toIndexPath:];
-[PHLiveLookupSettingsController setExtensions:];
-[PHLiveLookupSettingsController dealloc];
-[PHLiveLookupSettingsController queue];
-[PHLiveLookupSettingsController parent];
-[PHLiveLookupSettingsController extensions];
-[PHLiveLookupSettingsController initWithParent:];
-[PHLiveLookupSettingsController readPreferenceValue:];
-[PHLiveLookupSettingsController setPreferenceValue:specifier:];
-[PHLiveLookupSettingsController specifiers];
-[PHLiveLookupSettingsController setSpecifiers:];
-[PHLiveLookupSettingsController extensionManager];
-[PHLiveLookupSettingsController createExtensionsGroupSpecifiers];
-[PHLiveLookupSettingsController _extensionFrom:];
-[PHLiveLookupSettingsController _isUniqueExtension:];
-[PHLiveLookupSettingsController _localizedExtensionTitleForExtension:unique:];
-[PHLiveLookupSettingsController _updateExtensions];
-[PHLiveLookupSettingsController canEditExtensions];
-[PHLiveLookupSettingsController extensionForSpecifier:];
-[PHLiveLookupSettingsController handleUIApplicationWillEnterForegroundNotification:];
-[PHLiveLookupSettingsController hasExtensions];
-[PHLiveLookupSettingsController presentError:fromSettingEnabled:forExtension:];
-[PHLiveLookupSettingsController refreshView];
```
