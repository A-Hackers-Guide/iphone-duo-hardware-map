# `SAPExperienceProvider`

- Image: [`/System/Library/PrivateFrameworks/SetupAssistantPane.framework/SetupAssistantPane`](../userland/System__Library__PrivateFrameworks__SetupAssistantPane.framework__SetupAssistantPane.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
+[SAPExperienceProvider correspondingBundleIdentifierForBundleWithIdentifier:];
```

## Instance methods

```
-[SAPExperienceProvider init];
-[SAPExperienceProvider initWithServiceProvider:];
-[SAPExperienceProvider serviceProvider];
-[SAPExperienceProvider bundleLoader];
-[SAPExperienceProvider classForBundleWithIdentifier:];
-[SAPExperienceProvider initWithBundleLoader:serviceProvider:];
-[SAPExperienceProvider instanceForBundleWithIdentifier:];
```
