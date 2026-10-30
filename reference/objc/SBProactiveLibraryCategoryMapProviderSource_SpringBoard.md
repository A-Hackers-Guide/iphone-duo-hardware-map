# `SBProactiveLibraryCategoryMapProviderSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHLibraryCategoryMapProviderSource`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"ATXAppDirectoryClient" _appDirectoryClient;
@"<SBHLibraryCategoryMapProviderSourceDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBHLibraryCategoryMapProviderSourceDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",R,N) sourceName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProactiveLibraryCategoryMapProviderSource init];
-[SBProactiveLibraryCategoryMapProviderSource sourceName];
-[SBProactiveLibraryCategoryMapProviderSource setDelegate:];
-[SBProactiveLibraryCategoryMapProviderSource delegate];
-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:];
-[SBProactiveLibraryCategoryMapProviderSource _nonHiddenBundleIdentifiersForBundleIdentifiers:];
-[SBProactiveLibraryCategoryMapProviderSource _shouldRemoveRecentsPodWithLastKnownRecentApps:];
-[SBProactiveLibraryCategoryMapProviderSource handleUpdateCategoriesNotification:];
```
