# `IOAccessorySystemStateEndpoint`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _service;
I _connection;
```

## Properties

```
@property (TI,R,N,V_service) service;
@property (TI,R,N,V_connection) connection;
```

## Instance methods

```
-[IOAccessorySystemStateEndpoint dealloc];
-[IOAccessorySystemStateEndpoint service];
-[IOAccessorySystemStateEndpoint connection];
-[IOAccessorySystemStateEndpoint initWithService:];
-[IOAccessorySystemStateEndpoint notifyBootComplete];
-[IOAccessorySystemStateEndpoint notifyUserActive:];
-[IOAccessorySystemStateEndpoint notifyUserPresent:];
```
