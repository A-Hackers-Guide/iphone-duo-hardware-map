# `PLBatteryUINotificationService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- Protocols: `UNUserNotificationCenterDelegate`
- 12 instance variables, 16 properties, 36 instance methods, 1 class methods

## Instance variables

```
B _tlcNotificationDelivered;
B _isOBCEngaged;
@"PLBatteryUINotificationService" _notificationService;
@"UNUserNotificationCenter" _userNotificationCenter;
@"UNUserNotificationCenter" _ursaNotificationCenter;
@"NSMutableDictionary" _queryPayload;
@"NSDictionary" _queryResponderService;
@"NSString" _tlcNotificationIdentifier;
@"PLXPCResponderOperatorComposition" _queryResponder;
@"PLXPCResponderOperatorComposition" _ursaQueryResponder;
@"NSDictionary" _hpdConfig;
@"PowerUISmartChargeClient" _smartChargingClient;
```

## Properties

```
@property (T@"UNUserNotificationCenter",&,V_userNotificationCenter) userNotificationCenter;
@property (T@"UNUserNotificationCenter",&,V_ursaNotificationCenter) ursaNotificationCenter;
@property (T@"NSMutableDictionary",&,V_queryPayload) queryPayload;
@property (T@"NSDictionary",&,N,V_queryResponderService) queryResponderService;
@property (T@"NSString",&,V_tlcNotificationIdentifier) tlcNotificationIdentifier;
@property (TB,V_tlcNotificationDelivered) tlcNotificationDelivered;
@property (T@"PLXPCResponderOperatorComposition",&,V_queryResponder) queryResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_ursaQueryResponder) ursaQueryResponder;
@property (T@"NSDictionary",&,V_hpdConfig) hpdConfig;
@property (T@"PowerUISmartChargeClient",&,V_smartChargingClient) smartChargingClient;
@property (TB,V_isOBCEngaged) isOBCEngaged;
@property (T@"PLBatteryUINotificationService",&,V_notificationService) notificationService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLBatteryUINotificationService load];
```

## Instance methods

```
-[PLBatteryUINotificationService userNotificationCenter];
-[PLBatteryUINotificationService setUserNotificationCenter:];
-[PLBatteryUINotificationService initOperatorDependancies];
-[PLBatteryUINotificationService notificationService];
-[PLBatteryUINotificationService setNotificationService:];
-[PLBatteryUINotificationService ursaTTRContent:];
-[PLBatteryUINotificationService ursaBaseContent];
-[PLBatteryUINotificationService handleUrsaNotificationRequest:];
-[PLBatteryUINotificationService hpdConfig];
-[PLBatteryUINotificationService initializeUrsaNotifications];
-[PLBatteryUINotificationService isOBCEngaged];
-[PLBatteryUINotificationService queryPayload];
-[PLBatteryUINotificationService queryResponder];
-[PLBatteryUINotificationService queryResponderService];
-[PLBatteryUINotificationService removeTLCNotification];
-[PLBatteryUINotificationService removeUrsaNotifications];
-[PLBatteryUINotificationService setHpdConfig:];
-[PLBatteryUINotificationService setIsOBCEngaged:];
-[PLBatteryUINotificationService setQueryPayload:];
-[PLBatteryUINotificationService setQueryResponder:];
-[PLBatteryUINotificationService setQueryResponderService:];
-[PLBatteryUINotificationService setSmartChargingClient:];
-[PLBatteryUINotificationService setTlcNotificationDelivered:];
-[PLBatteryUINotificationService setTlcNotificationIdentifier:];
-[PLBatteryUINotificationService setUrsaNotificationCenter:];
-[PLBatteryUINotificationService setUrsaQueryResponder:];
-[PLBatteryUINotificationService smartChargingClient];
-[PLBatteryUINotificationService surfaceNotification];
-[PLBatteryUINotificationService thermallyLimitedChargingEngagedContent];
-[PLBatteryUINotificationService thermallyLimitedChargingEngagedRequest];
-[PLBatteryUINotificationService tlcNotificationDelivered];
-[PLBatteryUINotificationService tlcNotificationIdentifier];
-[PLBatteryUINotificationService ursaBootargContent:];
-[PLBatteryUINotificationService ursaNotificationCenter];
-[PLBatteryUINotificationService ursaQueryResponder];
-[PLBatteryUINotificationService ursaRadarContent:];
```
