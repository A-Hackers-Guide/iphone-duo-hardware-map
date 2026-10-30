# `PHBusinessCallingListController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `CoreTelephonyClientDelegate`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"PHBrandedCallingController" _brandedCallingController;
@"PHBusinessConnectCallingController" _businessConnectCallingController;
@"CoreTelephonyClient" _ctClient;
```

## Properties

```
@property (T@"PHBrandedCallingController",&,N,V_brandedCallingController) brandedCallingController;
@property (T@"PHBusinessConnectCallingController",&,N,V_businessConnectCallingController) businessConnectCallingController;
@property (T@"CoreTelephonyClient",&,N,V_ctClient) ctClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHBusinessCallingListController activeSubscriptionsDidChange];
-[PHBusinessCallingListController willEnterForeground];
-[PHBusinessCallingListController ctClient];
-[PHBusinessCallingListController init];
-[PHBusinessCallingListController specifiers];
-[PHBusinessCallingListController setCtClient:];
-[PHBusinessCallingListController brandedCallingController];
-[PHBusinessCallingListController businessConnectCallingController];
-[PHBusinessCallingListController groupFooterTextFor:];
-[PHBusinessCallingListController setBrandedCallingController:];
-[PHBusinessCallingListController setBusinessConnectCallingController:];
```
