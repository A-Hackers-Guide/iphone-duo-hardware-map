# `LACDTOServiceXPCClient`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOServiceXPCClient`
- 3 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOServiceXPCEndpointProvider>" _endpointProvider;
@"NSXPCConnection" _connection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOServiceXPCClient dealloc];
-[LACDTOServiceXPCClient _synchronousRemoteObjectProxyWithErrorHandler:];
-[LACDTOServiceXPCClient isFeatureSupported];
-[LACDTOServiceXPCClient isExtendedPolicyProtectionEnabled];
-[LACDTOServiceXPCClient isExtendedPolicyProtectionAvailable];
-[LACDTOServiceXPCClient isFeatureEnabled];
-[LACDTOServiceXPCClient _remoteObjectProxyWithErrorHandler:];
-[LACDTOServiceXPCClient ratchetState];
-[LACDTOServiceXPCClient isFeatureAvailable];
-[LACDTOServiceXPCClient _connectionWithErrorHandler:];
-[LACDTOServiceXPCClient _handleConnectionClose];
-[LACDTOServiceXPCClient isSensorTrusted];
-[LACDTOServiceXPCClient checkCanEnableFeatureWithCompletion:];
-[LACDTOServiceXPCClient disableExtendedPolicyProtectionWithContext:completion:];
-[LACDTOServiceXPCClient disableFeatureStrictModeWithContext:completion:];
-[LACDTOServiceXPCClient disableFeatureWithContext:completion:];
-[LACDTOServiceXPCClient enableExtendedPolicyProtectionWithCompletion:];
-[LACDTOServiceXPCClient enableFeatureStrictModeWithCompletion:];
-[LACDTOServiceXPCClient isAutoEnablementAllowed:];
-[LACDTOServiceXPCClient isFeatureStrictModeEnabled];
-[LACDTOServiceXPCClient resetRatchetWithReason:completion:];
-[LACDTOServiceXPCClient cancelPendingEvaluationWithRatchetIdentifier:reason:completion:];
-[LACDTOServiceXPCClient checkIsAutoEnablementAllowedWithCompletion:];
-[LACDTOServiceXPCClient checkIsExtendedPolicyProtectionAvailableWithCompletion:];
-[LACDTOServiceXPCClient checkIsExtendedPolicyProtectionEnabledWithCompletion:];
-[LACDTOServiceXPCClient checkIsFeatureAvailableWithCompletion:];
-[LACDTOServiceXPCClient checkIsFeatureEnabledWithCompletion:];
-[LACDTOServiceXPCClient checkIsFeatureStrictModeEnabledWithCompletion:];
-[LACDTOServiceXPCClient checkIsFeatureSupportedWithCompletion:];
-[LACDTOServiceXPCClient checkIsSensorTrustedWithCompletion:];
-[LACDTOServiceXPCClient enableFeatureWithOptions:completion:];
-[LACDTOServiceXPCClient initWithEndpointProvider:];
-[LACDTOServiceXPCClient ratchetStateCompositeWithCompletion:];
-[LACDTOServiceXPCClient ratchetStateWithCompletion:];
```
