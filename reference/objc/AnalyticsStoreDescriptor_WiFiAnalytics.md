# `AnalyticsStoreDescriptor`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 7 class methods

## Instance variables

```
@"NSURL" _modelURL;
@"NSURL" _storeURL;
@"NSDictionary" _remoteStoreOptions;
@"NSPersistentStoreDescription" _storeDescription;
Q _analyticsStoreOptions;
@"NSString" _analyticsStoreOptionsDescription;
```

## Properties

```
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (T@"NSURL",&,N,V_storeURL) storeURL;
@property (T@"NSPersistentStoreDescription",&,N,V_storeDescription) storeDescription;
@property (TQ,N,V_analyticsStoreOptions) analyticsStoreOptions;
@property (T@"NSString",&,N,V_analyticsStoreOptionsDescription) analyticsStoreOptionsDescription;
@property (T@"NSDictionary",R,N,V_remoteStoreOptions) remoteStoreOptions;
```

## Class methods

```
+[AnalyticsStoreDescriptor defaultModelURL];
+[AnalyticsStoreDescriptor defaultModel];
+[AnalyticsStoreDescriptor storeDescriptor];
+[AnalyticsStoreDescriptor applicationSupportDirectoryPath];
+[AnalyticsStoreDescriptor defaultModelName];
+[AnalyticsStoreDescriptor defaultPersistentStoreURL];
+[AnalyticsStoreDescriptor optionDescription:];
```

## Instance methods

```
-[AnalyticsStoreDescriptor storeURL];
-[AnalyticsStoreDescriptor description];
-[AnalyticsStoreDescriptor setStoreURL:];
-[AnalyticsStoreDescriptor modelURL];
-[AnalyticsStoreDescriptor setModelURL:];
-[AnalyticsStoreDescriptor storeDescription];
-[AnalyticsStoreDescriptor setStoreDescription:];
-[AnalyticsStoreDescriptor analyticsStoreOptions];
-[AnalyticsStoreDescriptor analyticsStoreOptionsDescription];
-[AnalyticsStoreDescriptor initWithStoreURL:modelURL:];
-[AnalyticsStoreDescriptor remoteStoreOptions];
-[AnalyticsStoreDescriptor setAnalyticsStoreOptions:];
-[AnalyticsStoreDescriptor setAnalyticsStoreOptionsDescription:];
```
