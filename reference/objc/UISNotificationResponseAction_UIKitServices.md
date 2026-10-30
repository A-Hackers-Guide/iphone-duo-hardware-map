# `UISNotificationResponseAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 1 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UNNotificationResponse" _response;
```

## Properties

```
@property (T@"UNNotificationResponse",R,&,N,V_response) response;
@property (TB,R,N) isLocal;
@property (TB,R,N) isRemote;
@property (TB,R,N) isDefaultAction;
```

## Instance methods

```
-[UISNotificationResponseAction UIActionType];
-[UISNotificationResponseAction abortForUsageViolation:];
-[UISNotificationResponseAction initWithXPCDictionary:];
-[UISNotificationResponseAction isRemote];
-[UISNotificationResponseAction valueDescriptionForFlag:object:ofSetting:];
-[UISNotificationResponseAction keyDescriptionForSetting:];
-[UISNotificationResponseAction isLocal];
-[UISNotificationResponseAction _trigger];
-[UISNotificationResponseAction isKindOfClass:];
-[UISNotificationResponseAction response];
-[UISNotificationResponseAction isDefaultAction];
-[UISNotificationResponseAction initWithResponse:withHandler:];
```
