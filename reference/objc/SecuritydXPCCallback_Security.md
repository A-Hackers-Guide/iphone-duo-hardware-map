# `SecuritydXPCCallback`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SecuritydXPCCallbackProtocol`
- 1 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@? _callback;
```

## Properties

```
@property (T@?,C,V_callback) callback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SecuritydXPCCallback callback];
-[SecuritydXPCCallback setCallback:];
-[SecuritydXPCCallback initWithCallback:];
-[SecuritydXPCCallback callCallback:error:];
```
