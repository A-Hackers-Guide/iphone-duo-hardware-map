# `TUBusinessServicesMetadataDataProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"<TUBusinessServiceProviderProtocol>" _businessQueryService;
@"NSObject<OS_dispatch_queue>" _queue;
@? _metadataQueryHandler;
```

## Properties

```
@property (T@"<TUBusinessServiceProviderProtocol>",R,N,V_businessQueryService) businessQueryService;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@?,C,N,V_metadataQueryHandler) metadataQueryHandler;
```

## Class methods

```
+[TUBusinessServicesMetadataDataProvider sharedInstance];
```

## Instance methods

```
-[TUBusinessServicesMetadataDataProvider init];
-[TUBusinessServicesMetadataDataProvider queue];
-[TUBusinessServicesMetadataDataProvider businessQueryService];
-[TUBusinessServicesMetadataDataProvider fetchBusinessServiceInformationForHandleValue:completion:];
-[TUBusinessServicesMetadataDataProvider initWithBusinessService:];
-[TUBusinessServicesMetadataDataProvider isValidBusinessItem:];
-[TUBusinessServicesMetadataDataProvider metadataQueryHandler];
-[TUBusinessServicesMetadataDataProvider setMetadataQueryHandler:];
```
