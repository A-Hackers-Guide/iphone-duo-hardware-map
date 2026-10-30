# `LACSecureStorage`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACSecureStorageType`
- 3 instance variables, 6 properties, 24 instance methods, 9 class methods

## Instance variables

```
@"LACStorageValueTransformer" _transformer;
@"<LACSecureStorageDelegate>" delegate;
@"LACSecureStorageConfiguration" _config;
```

## Properties

```
@property (T@"LACSecureStorageConfiguration",R,N,V_config) config;
@property (T@"<LACSecureStorageDelegate>",W,N,Vdelegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACSecureStorage classForKey:];
+[LACSecureStorage isKeyAvailable:];
+[LACSecureStorage policyForKey:operation:value:];
+[LACSecureStorage additionalBoolEntitlementForKey:operation:value:];
+[LACSecureStorage checkKey:supportsOperation:];
+[LACSecureStorage isKeyAvailable:operation:];
+[LACSecureStorage isKeyAvailableForContextData:];
+[LACSecureStorage maxDataLengthForKey:];
+[LACSecureStorage minDataLengthForKey:];
```

## Instance methods

```
-[LACSecureStorage initWithConfig:];
-[LACSecureStorage config];
-[LACSecureStorage setDelegate:];
-[LACSecureStorage delegate];
-[LACSecureStorage _acmContextDataKeyForKey:completionHandler:];
-[LACSecureStorage _acmContextForUUID:error:];
-[LACSecureStorage _acmSEPControlForKey:completionHandler:];
-[LACSecureStorage _acmVariableForKey:completionHandler:];
-[LACSecureStorage _checkEntitlementForRequest:operation:value:failureHandler:];
-[LACSecureStorage _contextDataForKey:contextID:completionHandler:];
-[LACSecureStorage _exchangeObject:request:completionHandler:];
-[LACSecureStorage _rebootErrorForRequest:];
-[LACSecureStorage _securityBootModeForACMVariable:];
-[LACSecureStorage _sepControl:value:request:completionHandler:];
-[LACSecureStorage _setContextData:forKey:contextID:completionHandler:];
-[LACSecureStorage _setSecureBootModeForACMVariable:completionHandler:];
-[LACSecureStorage _setStandardSecureBootModeCompletionHandler:];
-[LACSecureStorage _setVariable:value:request:completionHandler:];
-[LACSecureStorage _storeObject:request:completionHandler:];
-[LACSecureStorage _variable:completionHandler:];
-[LACSecureStorage objectForRequest:completionHandler:];
-[LACSecureStorage processError:forRequest:completionHandler:];
-[LACSecureStorage removeObjectForRequest:completionHandler:];
-[LACSecureStorage setObject:forRequest:completionHandler:];
```
