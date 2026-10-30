# `SBFApplication`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBSApplicationShortcutService" _applicationShortcutService;
@"SBSApplicationShortcutServiceFetchResult" _applicationShortcutServiceFetchResult;
d _applicationShortcutServiceFetchResultExpirationReferenceTime;
B _systemOrInternalApplication;
@"NSString" _applicationBundleIdentifier;
@"NSString" _displayName;
@"NSURL" _bundleURL;
@"NSNumber" _appStoreItemID;
@"NSString" _applicationShortcutWidgetBundleIdentifier;
```

## Properties

```
@property (T@"NSString",R,N,V_applicationBundleIdentifier) applicationBundleIdentifier;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (T@"NSURL",R,N,V_bundleURL) bundleURL;
@property (TB,R,N,GisSystemOrInternalApplication,V_systemOrInternalApplication) systemOrInternalApplication;
@property (T@"NSNumber",R,N,V_appStoreItemID) appStoreItemID;
@property (T@"NSString",R,N,V_applicationShortcutWidgetBundleIdentifier) applicationShortcutWidgetBundleIdentifier;
@property (T@"NSArray",R,N) staticApplicationShortcutItems;
@property (T@"NSArray",R,N) dynamicApplicationShortcutItems;
```

## Instance methods

```
-[SBFApplication bundleURL];
-[SBFApplication dynamicApplicationShortcutItems];
-[SBFApplication initWithApplicationBundleIdentifier:];
-[SBFApplication init];
-[SBFApplication displayName];
-[SBFApplication dealloc];
-[SBFApplication applicationBundleIdentifier];
-[SBFApplication applicationShortcutWidgetBundleIdentifier];
-[SBFApplication staticApplicationShortcutItems];
-[SBFApplication _updateApplicationShortcutServiceFetchResult];
-[SBFApplication appStoreItemID];
-[SBFApplication isSystemOrInternalApplication];
```
