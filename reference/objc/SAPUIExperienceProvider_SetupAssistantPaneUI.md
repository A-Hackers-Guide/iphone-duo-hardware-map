# `SAPUIExperienceProvider`

- Image: [`/System/Library/PrivateFrameworks/SetupAssistantPaneUI.framework/SetupAssistantPaneUI`](../userland/System__Library__PrivateFrameworks__SetupAssistantPaneUI.framework__SetupAssistantPaneUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAPBundleProvider`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"<SAPBundleLoaderType>" bundleLoader;
@"<SAPServiceProvider>" serviceProvider;
```

## Properties

```
@property (T@"<SAPBundleLoaderType>",N,R,VbundleLoader) bundleLoader;
@property (T@"<SAPServiceProvider>",N,R,VserviceProvider) serviceProvider;
```

## Class methods

```
+[SAPUIExperienceProvider correspondingBundleIdentifierForBundleWithIdentifier:];
```

## Instance methods

```
-[SAPUIExperienceProvider init];
-[SAPUIExperienceProvider initWithServiceProvider:];
-[SAPUIExperienceProvider serviceProvider];
-[SAPUIExperienceProvider bundleLoader];
-[SAPUIExperienceProvider classForBundleWithIdentifier:];
-[SAPUIExperienceProvider initWithBundleLoader:serviceProvider:];
-[SAPUIExperienceProvider instanceForBundleWithIdentifier:];
```
