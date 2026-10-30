# `SAPUIExpressSettingViewModelType` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SetupAssistantPaneUI.framework/SetupAssistantPaneUI`](../userland/System__Library__PrivateFrameworks__SetupAssistantPaneUI.framework__SetupAssistantPaneUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 6 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) title;
@property (T@"NSString",R,N) subtitle;
@property (T@"NSString",R,N) stateText;
@property (T@"<SAPUIExpressSettingIconNameProvider>",R,N) iconProvider;
@property (TQ,R,N) featureType;
@property (T@"NSArray",R,N) privacyIdentifiers;
```

## Instance methods

```
-[SAPUIExpressSettingViewModelType subtitle];
-[SAPUIExpressSettingViewModelType title];
-[SAPUIExpressSettingViewModelType iconProvider];
-[SAPUIExpressSettingViewModelType privacyIdentifiers];
-[SAPUIExpressSettingViewModelType featureType];
-[SAPUIExpressSettingViewModelType addingPrivacyIdentifiers:];
-[SAPUIExpressSettingViewModelType initWithTitle:subtitle:stateText:iconServicesIconNamed:featureType:];
-[SAPUIExpressSettingViewModelType initWithTitle:subtitle:stateText:symbolName:featureType:];
-[SAPUIExpressSettingViewModelType stateText];
-[SAPUIExpressSettingViewModelType withPrivacyIdentifiers:];
```
