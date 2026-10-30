# `TUCallProviderManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallProviderManagerDataSourceDelegate`
- 5 instance variables, 20 properties, 40 instance methods, 3 class methods

## Instance variables

```
Q _type;
@"NSObject<OS_dispatch_queue>" _queue;
@"<TUCallProviderManagerDataSource>" _dataSource;
@"NSMapTable" _delegateToQueue;
@"<TUFeatureFlags>" _featureFlags;
```

## Properties

```
@property (TQ,R,N,V_type) type;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<TUCallProviderManagerDataSource>",R,N,V_dataSource) dataSource;
@property (T@"NSDictionary",R,C,N) providersByIdentifier;
@property (T@"NSMapTable",&,N,V_delegateToQueue) delegateToQueue;
@property (T@"<TUFeatureFlags>",R,N,V_featureFlags) featureFlags;
@property (T@"TUCallProvider",R,N) superboxProvider;
@property (T@"TUCallProvider",R,N) tinCanProvider;
@property (T@"TUCallProvider",R,N) defaultProvider;
@property (T@"TUCallProvider",R,N) emergencyProvider;
@property (T@"TUCallProvider",R,N) voicemailProvider;
@property (T@"TUCallProvider",R,N) telephonyProvider;
@property (T@"TUCallProvider",R,N) faceTimeProvider;
@property (T@"NSArray",R,C,N) providers;
@property (T@"TUCallProvider",R,N) defaultAppProvider;
@property (T@"NSArray",R,C,N) sortedProviders;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallProviderManager serviceForProvider:video:];
+[TUCallProviderManager invitationPreferencesForRecentCall];
+[TUCallProviderManager defaultProviders];
```

## Instance methods

```
-[TUCallProviderManager providers];
-[TUCallProviderManager removeDelegate:];
-[TUCallProviderManager defaultAppProvider];
-[TUCallProviderManager providerForFavoritesEntryActionBundleIdentifier:];
-[TUCallProviderManager addDelegate:queue:];
-[TUCallProviderManager providersChangedForDataSource:];
-[TUCallProviderManager delegateToQueue];
-[TUCallProviderManager debugDescription];
-[TUCallProviderManager emergencyProvider];
-[TUCallProviderManager providerForRecentCall:];
-[TUCallProviderManager init];
-[TUCallProviderManager initWithType:];
-[TUCallProviderManager dealloc];
-[TUCallProviderManager launchAppForDialRequest:completion:];
-[TUCallProviderManager defaultProvider];
-[TUCallProviderManager providersByIdentifier];
-[TUCallProviderManager tinCanProvider];
-[TUCallProviderManager queue];
-[TUCallProviderManager dialRequestForRecentCall:];
-[TUCallProviderManager sortedProviders];
-[TUCallProviderManager donateUserIntentForProviderWithIdentifier:];
-[TUCallProviderManager initWithDataSource:type:queue:];
-[TUCallProviderManager initWithLocalProviders];
-[TUCallProviderManager dataSource];
-[TUCallProviderManager providerWithService:video:];
-[TUCallProviderManager voicemailProvider];
-[TUCallProviderManager type];
-[TUCallProviderManager initWithPairedHostDeviceProviders];
-[TUCallProviderManager joinConversationRequestForRecentCall:];
-[TUCallProviderManager providerForFavoritesEntry:];
-[TUCallProviderManager donateBackgroundCallIntentForProviderWithIdentifier:];
-[TUCallProviderManager providersPassingTest:];
-[TUCallProviderManager sortedProvidersPassingTest:];
-[TUCallProviderManager telephonyProvider];
-[TUCallProviderManager faceTimeProvider];
-[TUCallProviderManager superboxProvider];
-[TUCallProviderManager setDelegateToQueue:];
-[TUCallProviderManager initWithDataSource:type:queue:featureFlags:];
-[TUCallProviderManager providerWithIdentifier:];
-[TUCallProviderManager featureFlags];
```
