# `SAPUIExpressSettingViewModel`

- Image: [`/System/Library/PrivateFrameworks/SetupAssistantPaneUI.framework/SetupAssistantPaneUI`](../userland/System__Library__PrivateFrameworks__SetupAssistantPaneUI.framework__SetupAssistantPaneUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAPUIExpressSettingViewModelType`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
? title;
? subtitle;
? stateText;
@"<SAPUIExpressSettingIconNameProvider>" iconProvider;
Q featureType;
? privacyIdentifiers;
```

## Properties

```
@property (T@"NSString",N,R) title;
@property (T@"NSString",N,R) subtitle;
@property (T@"NSString",N,R) stateText;
@property (T@"<SAPUIExpressSettingIconNameProvider>",N,R,ViconProvider) iconProvider;
@property (TQ,N,R,VfeatureType) featureType;
@property (T@"NSArray",N,R) privacyIdentifiers;
```

## Instance methods

```
-[SAPUIExpressSettingViewModel subtitle];
-[SAPUIExpressSettingViewModel init];
-[SAPUIExpressSettingViewModel title];
-[SAPUIExpressSettingViewModel iconProvider];
-[SAPUIExpressSettingViewModel privacyIdentifiers];
-[SAPUIExpressSettingViewModel featureType];
-[SAPUIExpressSettingViewModel addingPrivacyIdentifiers:];
-[SAPUIExpressSettingViewModel initWithTitle:subtitle:stateText:iconProvider:featureType:privacyIdentifiers:];
-[SAPUIExpressSettingViewModel initWithTitle:subtitle:stateText:iconServicesIconNamed:featureType:];
-[SAPUIExpressSettingViewModel initWithTitle:subtitle:stateText:symbolName:featureType:];
-[SAPUIExpressSettingViewModel stateText];
-[SAPUIExpressSettingViewModel withPrivacyIdentifiers:];
```
