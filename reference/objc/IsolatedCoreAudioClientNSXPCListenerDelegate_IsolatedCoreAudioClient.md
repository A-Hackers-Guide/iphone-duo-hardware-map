# `IsolatedCoreAudioClientNSXPCListenerDelegate`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 4 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSXPCInterface" _mInterface;
@"NSString" _mEntitlementString;
@"NSMutableDictionary" _mConnections;
{function<void (int)>="__f_"{__value_func<void (int)>="__buf_"(type="__data"[24C])"__f_"^v}} _mClientReaper;
```

## Properties

```
@property (T@"NSXPCInterface",&,N,V_mInterface) mInterface;
@property (T@"NSString",C,N,V_mEntitlementString) mEntitlementString;
@property (T@"NSMutableDictionary",&,N,V_mConnections) mConnections;
@property (T{function<void (int)>={__value_func<void (int)>=(type=[24C])^v}},N,V_mClientReaper) mClientReaper;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[IsolatedCoreAudioClientNSXPCListenerDelegate listener:shouldAcceptNewConnection:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate dealloc];
-[IsolatedCoreAudioClientNSXPCListenerDelegate getUseCaseIDForPID:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate lookupConnectionForPID:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate mClientReaper];
-[IsolatedCoreAudioClientNSXPCListenerDelegate mConnections];
-[IsolatedCoreAudioClientNSXPCListenerDelegate mEntitlementString];
-[IsolatedCoreAudioClientNSXPCListenerDelegate mInterface];
-[IsolatedCoreAudioClientNSXPCListenerDelegate setClientReaper:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate setMClientReaper:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate setMConnections:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate setMEntitlementString:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate setMInterface:];
-[IsolatedCoreAudioClientNSXPCListenerDelegate setUseCaseIDForCurrentConnection:];
```
