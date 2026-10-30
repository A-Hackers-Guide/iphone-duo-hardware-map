# `CWFTrialFactorProvider`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _consumerKey;
@"NSObject<OS_dispatch_queue>" _providerQueue;
@"TRIClient" _triClient;
@"<TRINotificationToken>" _updateToken;
@? _updateHandler;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
B _isMonitoring;
@"NSDictionary" _currentParameters;
```

## Properties

```
@property (T@"NSString",R,C,N,V_consumerKey) consumerKey;
@property (T@"NSDictionary",R,N) currentParameters;
```

## Instance methods

```
-[CWFTrialFactorProvider startMonitoring];
-[CWFTrialFactorProvider dealloc];
-[CWFTrialFactorProvider forceRefresh];
-[CWFTrialFactorProvider stopMonitoring];
-[CWFTrialFactorProvider consumerKey];
-[CWFTrialFactorProvider _downloadAndParseFactor];
-[CWFTrialFactorProvider _parseFactorAndNotify];
-[CWFTrialFactorProvider _updateParametersAndNotify:];
-[CWFTrialFactorProvider currentParameters];
-[CWFTrialFactorProvider initWithConsumerKey:];
-[CWFTrialFactorProvider setUpdateHandler:queue:];
```
