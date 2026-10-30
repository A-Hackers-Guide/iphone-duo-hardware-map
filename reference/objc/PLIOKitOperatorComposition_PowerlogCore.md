# `PLIOKitOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 32 instance methods, 9 class methods

## Instance variables

```
I _notificationRef;
I _service;
I _iterator;
I _conn;
^{IONotificationPort=} _ioNotifyPort;
@"NSString" _serviceName;
@"NSString" _serviceClassName;
@? _operatorBlock;
@? _matchBlock;
@"PLOperator" _operator;
```

## Properties

```
@property (T@"PLOperator",&,V_operator) operator;
@property (T^{IONotificationPort=},V_ioNotifyPort) ioNotifyPort;
@property (TI,V_notificationRef) notificationRef;
@property (TI,V_service) service;
@property (T@"NSString",&,V_serviceName) serviceName;
@property (T@"NSString",&,V_serviceClassName) serviceClassName;
@property (TI,V_iterator) iterator;
@property (TI,V_conn) conn;
@property (T@?,C,N,V_operatorBlock) operatorBlock;
@property (T@?,C,N,V_matchBlock) matchBlock;
```

## Class methods

```
+[PLIOKitOperatorComposition enrichSnapshot:withPackSnapshot:withBankSnapshot:withChargerSnapshot:];
+[PLIOKitOperatorComposition enrichedSmartBatterySnapshotFromIOEntry:];
+[PLIOKitOperatorComposition enrichedSnapshotFromChargerService:];
+[PLIOKitOperatorComposition enrichedSnapshotFromPackService:];
+[PLIOKitOperatorComposition firstMatchingServiceSnapshotForClass:matcher:];
+[PLIOKitOperatorComposition legacyRescuedSnapshot:];
+[PLIOKitOperatorComposition snapshotFromIOEntry:];
+[PLIOKitOperatorComposition snapshotFromIOEntry:forKey:];
+[PLIOKitOperatorComposition snapshotFromIOEntry:forKeys:];
```

## Instance methods

```
-[PLIOKitOperatorComposition notificationRef];
-[PLIOKitOperatorComposition properties];
-[PLIOKitOperatorComposition setService:];
-[PLIOKitOperatorComposition dealloc];
-[PLIOKitOperatorComposition setNotificationRef:];
-[PLIOKitOperatorComposition setConn:];
-[PLIOKitOperatorComposition iterator];
-[PLIOKitOperatorComposition conn];
-[PLIOKitOperatorComposition serviceName];
-[PLIOKitOperatorComposition setServiceName:];
-[PLIOKitOperatorComposition service];
-[PLIOKitOperatorComposition operator];
-[PLIOKitOperatorComposition setIterator:];
-[PLIOKitOperatorComposition setOperator:];
-[PLIOKitOperatorComposition matchBlock];
-[PLIOKitOperatorComposition propertiesForKeys:];
-[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:];
-[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:withMatchBlock:];
-[PLIOKitOperatorComposition initWithOperator:forService:];
-[PLIOKitOperatorComposition initWithOperator:forService:withBlock:];
-[PLIOKitOperatorComposition initWithOperator:forServiceClass:];
-[PLIOKitOperatorComposition initWithOperator:forServiceClass:withBlock:];
-[PLIOKitOperatorComposition ioNotifyPort];
-[PLIOKitOperatorComposition operatorBlock];
-[PLIOKitOperatorComposition propertiesForKey:];
-[PLIOKitOperatorComposition propertiesFromIOEntry:];
-[PLIOKitOperatorComposition propertiesFromIOEntry:forKey:];
-[PLIOKitOperatorComposition serviceClassName];
-[PLIOKitOperatorComposition setIoNotifyPort:];
-[PLIOKitOperatorComposition setMatchBlock:];
-[PLIOKitOperatorComposition setOperatorBlock:];
-[PLIOKitOperatorComposition setServiceClassName:];
```
