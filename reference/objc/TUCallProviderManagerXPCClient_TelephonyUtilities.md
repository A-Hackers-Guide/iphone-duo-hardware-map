# `TUCallProviderManagerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallProviderManagerXPCClient`, `TUCallProviderManagerDataSource`
- 9 instance variables, 16 properties, 36 instance methods, 7 class methods

## Instance variables

```
B _requestedInitialState;
B _hasEverRequestedInitialState;
i _token;
@"<TUCallProviderManagerDataSourceDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
@"NSDictionary" _providersByIdentifier;
@"NSDictionary" _localProvidersByIdentifier;
@"NSDictionary" _pairedHostDeviceProvidersByIdentifier;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (Ti,N,V_token) token;
@property (TB,N,V_requestedInitialState) requestedInitialState;
@property (TB,N,V_hasEverRequestedInitialState) hasEverRequestedInitialState;
@property (T@"NSDictionary",C,N,V_providersByIdentifier) providersByIdentifier;
@property (T@"NSDictionary",C,N,V_localProvidersByIdentifier) localProvidersByIdentifier;
@property (T@"NSDictionary",C,N,V_pairedHostDeviceProvidersByIdentifier) pairedHostDeviceProvidersByIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) currentProcessCanAccessInitialState;
@property (T@"TUCallProvider",R,N) defaultAppProvider;
@property (T@"NSArray",R,C,N) sortedProviders;
@property (T@"<TUCallProviderManagerDataSourceDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[TUCallProviderManagerXPCClient setAsynchronousServer:];
+[TUCallProviderManagerXPCClient asynchronousServer];
+[TUCallProviderManagerXPCClient setSynchronousServer:];
+[TUCallProviderManagerXPCClient synchronousServer];
+[TUCallProviderManagerXPCClient callProviderManagerAllowedClasses];
+[TUCallProviderManagerXPCClient callProviderManagerClientXPCInterface];
+[TUCallProviderManagerXPCClient callProviderManagerServerXPCInterface];
```

## Instance methods

```
-[TUCallProviderManagerXPCClient defaultAppProvider];
-[TUCallProviderManagerXPCClient setHasEverRequestedInitialState:];
-[TUCallProviderManagerXPCClient setLocalProvidersByIdentifier:];
-[TUCallProviderManagerXPCClient synchronousServerWithErrorHandler:];
-[TUCallProviderManagerXPCClient _updateProvidersByIdentifier:localProvidersByIdentifier:pairedHostDeviceProvidersByIdentifier:];
-[TUCallProviderManagerXPCClient server];
-[TUCallProviderManagerXPCClient init];
-[TUCallProviderManagerXPCClient setXpcConnection:];
-[TUCallProviderManagerXPCClient currentProcessCanAccessInitialState];
-[TUCallProviderManagerXPCClient dealloc];
-[TUCallProviderManagerXPCClient launchAppForDialRequest:completion:];
-[TUCallProviderManagerXPCClient setProvidersByIdentifier:];
-[TUCallProviderManagerXPCClient providersByIdentifier];
-[TUCallProviderManagerXPCClient queue];
-[TUCallProviderManagerXPCClient localProvidersByIdentifier];
-[TUCallProviderManagerXPCClient xpcConnection];
-[TUCallProviderManagerXPCClient invalidate];
-[TUCallProviderManagerXPCClient openURL:isSensitive:error:];
-[TUCallProviderManagerXPCClient sortedProviders];
-[TUCallProviderManagerXPCClient donateUserIntentForProviderWithIdentifier:];
-[TUCallProviderManagerXPCClient setDelegate:];
-[TUCallProviderManagerXPCClient setRequestedInitialState:];
-[TUCallProviderManagerXPCClient hasEverRequestedInitialState];
-[TUCallProviderManagerXPCClient openURL:shouldActivate:completionHandler:];
-[TUCallProviderManagerXPCClient delegate];
-[TUCallProviderManagerXPCClient donateBackgroundCallIntentForProviderWithIdentifier:];
-[TUCallProviderManagerXPCClient requestedInitialState];
-[TUCallProviderManagerXPCClient token];
-[TUCallProviderManagerXPCClient blockUntilInitialStateReceived];
-[TUCallProviderManagerXPCClient setToken:];
-[TUCallProviderManagerXPCClient setPairedHostDeviceProvidersByIdentifier:];
-[TUCallProviderManagerXPCClient serverWithErrorHandler:];
-[TUCallProviderManagerXPCClient pairedHostDeviceProvidersByIdentifier];
-[TUCallProviderManagerXPCClient _requestInitialState];
-[TUCallProviderManagerXPCClient updateProvidersByIdentifier:localProvidersByIdentifier:pairedHostDeviceProvidersByIdentifier:];
-[TUCallProviderManagerXPCClient setQueue:];
```
