# `SecCTKKey`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _isRegisteredSmartcard;
B _wasAuthenticationContextProvidedBySecCaller;
@"TKClientTokenObject" _tokenObject;
@"NSDictionary" _keychainAttributes;
@"NSDictionary" _sessionParameters;
@"NSData" _tokenOID;
```

## Properties

```
@property (T@"TKClientTokenObject",&,N,V_tokenObject) tokenObject;
@property (T@"NSDictionary",R,N,V_keychainAttributes) keychainAttributes;
@property (T@"NSDictionary",&,N,V_sessionParameters) sessionParameters;
@property (Tq,R,N) algorithmID;
@property (T@"NSData",R,N,V_tokenOID) tokenOID;
@property (TB,N,V_isRegisteredSmartcard) isRegisteredSmartcard;
@property (TB,N,V_wasAuthenticationContextProvidedBySecCaller) wasAuthenticationContextProvidedBySecCaller;
```

## Class methods

```
+[SecCTKKey fromKeyRef:];
```

## Instance methods

```
-[SecCTKKey sessionParameters];
-[SecCTKKey tokenObject];
-[SecCTKKey initWithAttributes:error:];
-[SecCTKKey isRegisteredSmartcard];
-[SecCTKKey setWasAuthenticationContextProvidedBySecCaller:];
-[SecCTKKey tokenOID];
-[SecCTKKey initFromKey:];
-[SecCTKKey wasAuthenticationContextProvidedBySecCaller];
-[SecCTKKey setIsRegisteredSmartcard:];
-[SecCTKKey keychainAttributes];
-[SecCTKKey setSessionParameters:];
-[SecCTKKey setTokenObject:];
-[SecCTKKey copyWithZone:];
-[SecCTKKey ensureTokenObject:];
-[SecCTKKey algorithmID];
-[SecCTKKey isEqual:];
-[SecCTKKey ensureTokenObjectForBlock:error:];
-[SecCTKKey shouldRetryOperationForRegisteredSmartcard:];
```
