# `PHCallBlockingAndIdentificationSettingsBundleController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSBundleController`
- Protocols: `CXCallDirectoryExtensionManagerDelegate`, `PHCallBlockingServiceProviderControllerDelegate`
- 6 instance variables, 12 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"PSSpecifier" _callDirectorySpecifier;
@"NSMutableArray" _extensions;
@"NSMutableArray" _llextensions;
@"CXCallDirectoryExtensionManager" _extensionManager;
@"PHCallBlockingServiceProviderController" _serviceProviderController;
@"PHBusinessCallingController" _businessCallingController;
```

## Properties

```
@property (T@"PSSpecifier",&,N,V_callDirectorySpecifier) callDirectorySpecifier;
@property (T@"NSMutableArray",&,N,V_extensions) extensions;
@property (T@"NSMutableArray",&,N,V_llextensions) llextensions;
@property (T@"CXCallDirectoryExtensionManager",R,N,V_extensionManager) extensionManager;
@property (T@"PHCallBlockingServiceProviderController",R,N,V_serviceProviderController) serviceProviderController;
@property (T@"PHBusinessCallingController",R,N,V_businessCallingController) businessCallingController;
@property (T@"PSListController",R,W,N) parentListController;
@property (TB,R,N,GisHidden) hidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHCallBlockingAndIdentificationSettingsBundleController setExtensions:];
-[PHCallBlockingAndIdentificationSettingsBundleController isHidden];
-[PHCallBlockingAndIdentificationSettingsBundleController extensions];
-[PHCallBlockingAndIdentificationSettingsBundleController initWithParentListController:];
-[PHCallBlockingAndIdentificationSettingsBundleController specifiersWithSpecifier:];
-[PHCallBlockingAndIdentificationSettingsBundleController extensionsChangedForCallDirectoryExtensionManager:];
-[PHCallBlockingAndIdentificationSettingsBundleController extensionManager];
-[PHCallBlockingAndIdentificationSettingsBundleController parentListController];
-[PHCallBlockingAndIdentificationSettingsBundleController _updateExtensions];
-[PHCallBlockingAndIdentificationSettingsBundleController businessCallingController];
-[PHCallBlockingAndIdentificationSettingsBundleController callDirectorySpecifier];
-[PHCallBlockingAndIdentificationSettingsBundleController didChangeServiceProvidersForCallBlockingServiceProviderController:];
-[PHCallBlockingAndIdentificationSettingsBundleController llextensions];
-[PHCallBlockingAndIdentificationSettingsBundleController serviceProviderController];
-[PHCallBlockingAndIdentificationSettingsBundleController setCallDirectorySpecifier:];
-[PHCallBlockingAndIdentificationSettingsBundleController setLlextensions:];
-[PHCallBlockingAndIdentificationSettingsBundleController shouldInsert];
-[PHCallBlockingAndIdentificationSettingsBundleController updateParentListController];
```
