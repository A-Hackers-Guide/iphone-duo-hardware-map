# `LAStorage`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 40 instance methods, 2 class methods

## Instance variables

```
I _instanceId;
q _domain;
@"LAContext" _authenticationContext;
@"NSXPCConnection" _connection;
@"<LACSecureStorageService>" _remoteObjectProxy;
```

## Properties

```
@property (T@"NSXPCConnection",R,N,V_connection) connection;
@property (T@"<LACSecureStorageService>",R,N,V_remoteObjectProxy) remoteObjectProxy;
@property (TI,R,N,V_instanceId) instanceId;
@property (Tq,R,N,V_domain) domain;
@property (T@"LAContext",R,N,V_authenticationContext) authenticationContext;
```

## Class methods

```
+[LAStorage newInstanceId];
+[LAStorage secureDomainStorage];
```

## Instance methods

```
-[LAStorage dictionaryForKey:];
-[LAStorage domain];
-[LAStorage boolForKey:];
-[LAStorage exchangeData:forKey:error:];
-[LAStorage exchangeData:forKey:completionHandler:];
-[LAStorage numberForKey:completionHandler:];
-[LAStorage setBool:forKey:completionHandler:];
-[LAStorage boolForKey:completionHandler:];
-[LAStorage processError:completionHandler:];
-[LAStorage removeObjectForKey:completionHandler:];
-[LAStorage setBool:forKey:error:];
-[LAStorage dealloc];
-[LAStorage _bootstrapServiceType:completionHandler:];
-[LAStorage setDictionary:forKey:completionHandler:];
-[LAStorage setObject:forKey:withOptions:completionHandler:];
-[LAStorage boolForKey:error:];
-[LAStorage authenticationContext];
-[LAStorage setDictionary:forKey:error:];
-[LAStorage setObject:forKey:completionHandler:];
-[LAStorage setData:forKey:completionHandler:];
-[LAStorage dataForKey:];
-[LAStorage dataForKey:error:];
-[LAStorage instanceId];
-[LAStorage _connectToEndpoint:];
-[LAStorage dictionaryForKey:error:];
-[LAStorage connection];
-[LAStorage setData:forKey:error:];
-[LAStorage dataForKey:completionHandler:];
-[LAStorage description];
-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:];
-[LAStorage numberForKey:];
-[LAStorage _bootstrapServiceWithAuthenticationPolicy:proxyBlock:completionHandler:];
-[LAStorage objectForKey:completionHandler:];
-[LAStorage setObject:forKey:withOptions:error:];
-[LAStorage _resetConnection];
-[LAStorage dictionaryForKey:completionHandler:];
-[LAStorage remoteObjectProxy];
-[LAStorage _class:forKey:completionHandler:];
-[LAStorage numberForKey:error:];
-[LAStorage initWithDomain:authenticationContext:];
```
