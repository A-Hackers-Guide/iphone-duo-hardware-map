# `SAPBundleLoader`

- Image: [`/System/Library/PrivateFrameworks/SetupAssistantPane.framework/SetupAssistantPane`](../userland/System__Library__PrivateFrameworks__SetupAssistantPane.framework__SetupAssistantPane.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAPBundleLoaderType`
- 4 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
? indexedBundlesPaths;
fileManager;
internalBuildProvider;
featureFlagProvider;
```

## Properties

```
@property (T@"NSDictionary",N,C) indexedBundlesPaths;
```

## Class methods

```
+[SAPBundleLoader sharedInstance];
```

## Instance methods

```
-[SAPBundleLoader init];
-[SAPBundleLoader allAvailableBundleIdentifiersFilteredBy:];
-[SAPBundleLoader allAvailableBundlePathsByIdentifier];
-[SAPBundleLoader indexedBundlesPaths];
-[SAPBundleLoader loadBundleWithIdentifier:];
-[SAPBundleLoader setIndexedBundlesPaths:];
```
