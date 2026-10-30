# `TUCallProviderManagerDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 15 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) currentProcessCanAccessInitialState;
@property (T@"NSDictionary",R,C,N) providersByIdentifier;
@property (T@"NSDictionary",R,C,N) localProvidersByIdentifier;
@property (T@"NSDictionary",R,C,N) pairedHostDeviceProvidersByIdentifier;
@property (T@"TUCallProvider",R,N) defaultAppProvider;
@property (T@"NSArray",R,C,N) sortedProviders;
@property (T@"<TUCallProviderManagerDataSourceDelegate>",W,N) delegate;
```

## Instance methods

```
-[TUCallProviderManagerDataSource defaultAppProvider];
-[TUCallProviderManagerDataSource currentProcessCanAccessInitialState];
-[TUCallProviderManagerDataSource launchAppForDialRequest:completion:];
-[TUCallProviderManagerDataSource providersByIdentifier];
-[TUCallProviderManagerDataSource localProvidersByIdentifier];
-[TUCallProviderManagerDataSource invalidate];
-[TUCallProviderManagerDataSource openURL:isSensitive:error:];
-[TUCallProviderManagerDataSource sortedProviders];
-[TUCallProviderManagerDataSource donateUserIntentForProviderWithIdentifier:];
-[TUCallProviderManagerDataSource setDelegate:];
-[TUCallProviderManagerDataSource openURL:shouldActivate:completionHandler:];
-[TUCallProviderManagerDataSource delegate];
-[TUCallProviderManagerDataSource donateBackgroundCallIntentForProviderWithIdentifier:];
-[TUCallProviderManagerDataSource blockUntilInitialStateReceived];
-[TUCallProviderManagerDataSource pairedHostDeviceProvidersByIdentifier];
```
