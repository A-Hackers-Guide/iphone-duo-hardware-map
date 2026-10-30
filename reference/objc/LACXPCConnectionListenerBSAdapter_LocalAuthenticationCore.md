# `LACXPCConnectionListenerBSAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `LACXPCConnectionListener`
- 2 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _listener;
@"<LACXPCConnectionListenerDelegate>" delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACXPCConnectionListenerDelegate>",W,N,Vdelegate) delegate;
```

## Instance methods

```
-[LACXPCConnectionListenerBSAdapter listener:didReceiveConnection:withContext:];
-[LACXPCConnectionListenerBSAdapter setDelegate:];
-[LACXPCConnectionListenerBSAdapter activate];
-[LACXPCConnectionListenerBSAdapter delegate];
-[LACXPCConnectionListenerBSAdapter initWithDomainName:protocolServiceName:];
```
