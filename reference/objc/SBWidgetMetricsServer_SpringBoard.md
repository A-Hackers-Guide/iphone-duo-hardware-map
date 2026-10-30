# `SBWidgetMetricsServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSWidgetMetricsServiceServerInterface`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _connections;
@"FBServiceClientAuthenticator" _authenticator;
@"BSServiceConnectionListener" _listener;
@"NSObject<OS_dispatch_queue>" _queue;
@"<SBSWidgetMetricsProviding>" _systemMetricsProvider;
@"<SBSWidgetMetricsProviding>" _lockScreenMetricsProvider;
@"<SBSWidgetMetricsProviding>" _ambientMetricsProvider;
```

## Properties

```
@property (T@"NSMutableArray",R,C,N,V_connections) connections;
@property (T@"FBServiceClientAuthenticator",R,N,V_authenticator) authenticator;
@property (T@"BSServiceConnectionListener",R,N,V_listener) listener;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<SBSWidgetMetricsProviding>",R,W,N,V_systemMetricsProvider) systemMetricsProvider;
@property (T@"<SBSWidgetMetricsProviding>",R,W,N,V_lockScreenMetricsProvider) lockScreenMetricsProvider;
@property (T@"<SBSWidgetMetricsProviding>",R,W,N,V_ambientMetricsProvider) ambientMetricsProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWidgetMetricsServer listener:didReceiveConnection:withContext:];
-[SBWidgetMetricsServer connections];
-[SBWidgetMetricsServer init];
-[SBWidgetMetricsServer dealloc];
-[SBWidgetMetricsServer queue];
-[SBWidgetMetricsServer listener];
-[SBWidgetMetricsServer authenticator];
-[SBWidgetMetricsServer previewMetricsSpecificationForBundleIdentifier:];
-[SBWidgetMetricsServer previewMetricsSpecificationForDeviceContext:displayContext:bundleIdentifier:];
-[SBWidgetMetricsServer previewMetricsSpecificationsForBundleIdentifier:];
-[SBWidgetMetricsServer previewMetricsSpecificationsForDeviceContext:displayContext:bundleIdentifier:];
-[SBWidgetMetricsServer systemMetricsForWidget:];
-[SBWidgetMetricsServer systemMetricsForWidget:inHostingEnvironment:];
-[SBWidgetMetricsServer _defaultMetricsProviderForWidget:];
-[SBWidgetMetricsServer _metricsProviderForHostingEnvironment:];
-[SBWidgetMetricsServer ambientMetricsProvider];
-[SBWidgetMetricsServer initWithSystemMetricsProvider:lockScreenMetricsProvider:ambientMetricsProvider:];
-[SBWidgetMetricsServer lockScreenMetricsProvider];
-[SBWidgetMetricsServer systemMetricsProvider];
```
