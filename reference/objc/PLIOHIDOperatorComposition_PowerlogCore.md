# `PLIOHIDOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} _eventSystemClient;
@"NSArray" _serviceClients;
@"NSString" _serviceName;
@? _operatorBlock;
@"PLOperator" _operator;
```

## Properties

```
@property (T@"PLOperator",&,V_operator) operator;
@property (T^{__IOHIDEventSystemClient=},V_eventSystemClient) eventSystemClient;
@property (T@"NSArray",&,V_serviceClients) serviceClients;
@property (T@"NSString",&,V_serviceName) serviceName;
@property (T@?,C,N,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[PLIOHIDOperatorComposition doubleForKey:];
-[PLIOHIDOperatorComposition dictionaryForKey:];
-[PLIOHIDOperatorComposition dealloc];
-[PLIOHIDOperatorComposition serviceName];
-[PLIOHIDOperatorComposition setServiceName:];
-[PLIOHIDOperatorComposition operator];
-[PLIOHIDOperatorComposition eventSystemClient];
-[PLIOHIDOperatorComposition setEventSystemClient:];
-[PLIOHIDOperatorComposition serviceClients];
-[PLIOHIDOperatorComposition setOperator:];
-[PLIOHIDOperatorComposition initWithOperator:forService:];
-[PLIOHIDOperatorComposition initWithOperator:forService:withBlock:];
-[PLIOHIDOperatorComposition operatorBlock];
-[PLIOHIDOperatorComposition setOperatorBlock:];
-[PLIOHIDOperatorComposition setServiceClients:];
```
