# `PHCallBlockingAndIdentificationSettingsListController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `CoreTelephonyClientDelegate`, `TUConfigurationProviderDelegate`
- 8 instance variables, 12 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"PHBusinessCallingController" _businessCallingController;
@"PHCallDirectorySettingsController" _callDirectorySettingsController;
@"PHLiveLookupSettingsController" _liveLookupSettingsController;
@"CoreTelephonyClient" _ctClient;
@"NSObject<OS_dispatch_queue>" _queue;
@"TUFeatureFlags" _featureFlags;
@"TUConfigurationProvider" _configurationProvider;
Q _businessCallingSpecifierCount;
```

## Properties

```
@property (T@"PHBusinessCallingController",R,N,V_businessCallingController) businessCallingController;
@property (T@"PHCallDirectorySettingsController",R,N,V_callDirectorySettingsController) callDirectorySettingsController;
@property (T@"PHLiveLookupSettingsController",R,N,V_liveLookupSettingsController) liveLookupSettingsController;
@property (T@"CoreTelephonyClient",R,N,V_ctClient) ctClient;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"TUConfigurationProvider",R,N,V_configurationProvider) configurationProvider;
@property (TQ,N,V_businessCallingSpecifierCount) businessCallingSpecifierCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHCallBlockingAndIdentificationSettingsListController tableView:canMoveRowAtIndexPath:];
-[PHCallBlockingAndIdentificationSettingsListController tableView:shouldIndentWhileEditingRowAtIndexPath:];
-[PHCallBlockingAndIdentificationSettingsListController tableView:editingStyleForRowAtIndexPath:];
-[PHCallBlockingAndIdentificationSettingsListController tableView:moveRowAtIndexPath:toIndexPath:];
-[PHCallBlockingAndIdentificationSettingsListController tableView:cellForRowAtIndexPath:];
-[PHCallBlockingAndIdentificationSettingsListController activeSubscriptionsDidChange];
-[PHCallBlockingAndIdentificationSettingsListController ctClient];
-[PHCallBlockingAndIdentificationSettingsListController setEditing:animated:];
-[PHCallBlockingAndIdentificationSettingsListController queue];
-[PHCallBlockingAndIdentificationSettingsListController initWithNibName:bundle:];
-[PHCallBlockingAndIdentificationSettingsListController tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:];
-[PHCallBlockingAndIdentificationSettingsListController viewWillAppear:];
-[PHCallBlockingAndIdentificationSettingsListController configurationProvider];
-[PHCallBlockingAndIdentificationSettingsListController featureFlags];
-[PHCallBlockingAndIdentificationSettingsListController configureCell:];
-[PHCallBlockingAndIdentificationSettingsListController reloadSpecifiers];
-[PHCallBlockingAndIdentificationSettingsListController specifiers];
-[PHCallBlockingAndIdentificationSettingsListController configurationChanged];
-[PHCallBlockingAndIdentificationSettingsListController setSwitchOn:];
-[PHCallBlockingAndIdentificationSettingsListController emitNavigationEvent];
-[PHCallBlockingAndIdentificationSettingsListController businessCallIdentificationIndex];
-[PHCallBlockingAndIdentificationSettingsListController callDirectorySettingsController];
-[PHCallBlockingAndIdentificationSettingsListController addBusinessCallingSpecifierIfNecessary:];
-[PHCallBlockingAndIdentificationSettingsListController addCallDirectorySpecifierIfNecessary:];
-[PHCallBlockingAndIdentificationSettingsListController addLiveLookupSpecifierIfNecessary:];
-[PHCallBlockingAndIdentificationSettingsListController businessCallingController];
-[PHCallBlockingAndIdentificationSettingsListController businessCallingSpecifierCount];
-[PHCallBlockingAndIdentificationSettingsListController callDirectoryIdentificationIndex];
-[PHCallBlockingAndIdentificationSettingsListController canEditExtensions];
-[PHCallBlockingAndIdentificationSettingsListController configureCell:forSpecifier:];
-[PHCallBlockingAndIdentificationSettingsListController liveLookupIdentificationIndex];
-[PHCallBlockingAndIdentificationSettingsListController liveLookupSettingsController];
-[PHCallBlockingAndIdentificationSettingsListController refreshView];
-[PHCallBlockingAndIdentificationSettingsListController setBusinessCallingSpecifierCount:];
-[PHCallBlockingAndIdentificationSettingsListController setNavigationItemsForEditing:animated:];
```
