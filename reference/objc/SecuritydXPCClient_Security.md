# `SecuritydXPCClient`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SecuritydXPCClientInterface`
- 1 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SecuritydXPCClient configureSecuritydXPCProtocol:];
```

## Instance methods

```
-[SecuritydXPCClient init];
-[SecuritydXPCClient dealloc];
-[SecuritydXPCClient connection];
-[SecuritydXPCClient setConnection:];
-[SecuritydXPCClient initTargetingSession:];
-[SecuritydXPCClient protocolWithSync:errorHandler:];
```
