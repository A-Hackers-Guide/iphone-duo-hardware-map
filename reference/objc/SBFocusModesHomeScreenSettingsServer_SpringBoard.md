# `SBFocusModesHomeScreenSettingsServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSFocusModesHomeScreenSettingsClientToServerInterface`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<SBFocusModesHomeScreenSettingsServerDelegate>" _delegate;
@"FBServiceClientAuthenticator" _authenticator;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _connections;
@"BSServiceConnectionListener" _listener;
```

## Properties

```
@property (T@"FBServiceClientAuthenticator",R,N,V_authenticator) authenticator;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSMutableArray",R,C,N,V_connections) connections;
@property (T@"BSServiceConnectionListener",R,N,V_listener) listener;
@property (T@"<SBFocusModesHomeScreenSettingsServerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFocusModesHomeScreenSettingsServer listener:didReceiveConnection:withContext:];
-[SBFocusModesHomeScreenSettingsServer connections];
-[SBFocusModesHomeScreenSettingsServer init];
-[SBFocusModesHomeScreenSettingsServer queue];
-[SBFocusModesHomeScreenSettingsServer listener];
-[SBFocusModesHomeScreenSettingsServer setDelegate:];
-[SBFocusModesHomeScreenSettingsServer activate];
-[SBFocusModesHomeScreenSettingsServer delegate];
-[SBFocusModesHomeScreenSettingsServer authenticator];
-[SBFocusModesHomeScreenSettingsServer addSuggestedHomeScreenPageWithRequest:];
-[SBFocusModesHomeScreenSettingsServer homeScreenSnapshotsForSuggestedPagesWithRequest:completion:];
-[SBFocusModesHomeScreenSettingsServer homeScreenSnapshotsWithRequest:completion:];
-[SBFocusModesHomeScreenSettingsServer updateFocusModeHomeScreenSettingsWithRequest:];
```
