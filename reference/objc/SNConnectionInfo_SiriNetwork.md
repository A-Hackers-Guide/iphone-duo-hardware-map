# `SNConnectionInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 24 properties, 49 instance methods, 0 class methods

## Instance variables

```
@"SNConnectionInfoInternal" _underlyingConnectionInfo;
```

## Properties

```
@property (T@"SNConnectionInfoInternal",&,N,V_underlyingConnectionInfo) underlyingConnectionInfo;
@property (Tq,N) connectionProtocolTechnology;
@property (Tq,N) communicationProtocolTechnology;
@property (T@"NSString",C,N) assistantIdentifier;
@property (T@"NSString",C,N) peerAssistantIdentifier;
@property (T@"NSString",C,N) connectionId;
@property (T@"NSString",C,N) aceHost;
@property (T@"NSString",C,N) languageCode;
@property (TB,N) prefersWWAN;
@property (TB,N) skipPeer;
@property (TB,N) useWiFiHint;
@property (T@"NSError",C,N) skipPeerErrorReason;
@property (TB,N) forceReconnect;
@property (Td,N) timeout;
@property (TB,N) imposePolicyBan;
@property (T@"SAConnectionPolicy",C,N) connectionPolicy;
@property (T@"SAConnectionPolicyRoute",C,N) connectionPolicyRoute;
@property (TB,N,GisForceOnDeviceOnlyDictationEnabled) forceOnDeviceOnlyDictation;
@property (T@"NSString",C,N) productTypePrefix;
@property (T@"NSString",C,N) peerType;
@property (T@"NSString",C,N) peerVersion;
@property (TB,N) deviceIsInWalkaboutExperimentGroup;
@property (TB,N) usesProxyConnection;
@property (TB,N) usesPeerManagedSync;
```

## Instance methods

```
-[SNConnectionInfo setConnectionProtocolTechnology:];
-[SNConnectionInfo setPeerVersion:];
-[SNConnectionInfo setForceReconnect:];
-[SNConnectionInfo setSkipPeer:];
-[SNConnectionInfo underlyingConnectionInfo];
-[SNConnectionInfo peerType];
-[SNConnectionInfo setAceHost:];
-[SNConnectionInfo setUsesPeerManagedSync:];
-[SNConnectionInfo assistantIdentifier];
-[SNConnectionInfo init];
-[SNConnectionInfo setPrefersWWAN:];
-[SNConnectionInfo prefersWWAN];
-[SNConnectionInfo setForceOnDeviceOnlyDictation:];
-[SNConnectionInfo setConnectionPolicy:];
-[SNConnectionInfo connectionPolicyRoute];
-[SNConnectionInfo connectionId];
-[SNConnectionInfo setConnectionId:];
-[SNConnectionInfo timeout];
-[SNConnectionInfo languageCode];
-[SNConnectionInfo setUseWiFiHint:];
-[SNConnectionInfo setProductTypePrefix:];
-[SNConnectionInfo setSkipPeerErrorReason:];
-[SNConnectionInfo setTimeout:];
-[SNConnectionInfo forceReconnect];
-[SNConnectionInfo deviceIsInWalkaboutExperimentGroup];
-[SNConnectionInfo setUsesProxyConnection:];
-[SNConnectionInfo setPeerType:];
-[SNConnectionInfo setCommunicationProtocolTechnology:];
-[SNConnectionInfo setDeviceIsInWalkaboutExperimentGroup:];
-[SNConnectionInfo setConnectionPolicyRoute:];
-[SNConnectionInfo productTypePrefix];
-[SNConnectionInfo setUnderlyingConnectionInfo:];
-[SNConnectionInfo peerAssistantIdentifier];
-[SNConnectionInfo setImposePolicyBan:];
-[SNConnectionInfo peerVersion];
-[SNConnectionInfo setPeerAssistantIdentifier:];
-[SNConnectionInfo usesProxyConnection];
-[SNConnectionInfo connectionPolicy];
-[SNConnectionInfo useWiFiHint];
-[SNConnectionInfo imposePolicyBan];
-[SNConnectionInfo isForceOnDeviceOnlyDictationEnabled];
-[SNConnectionInfo usesPeerManagedSync];
-[SNConnectionInfo aceHost];
-[SNConnectionInfo setAssistantIdentifier:];
-[SNConnectionInfo skipPeer];
-[SNConnectionInfo communicationProtocolTechnology];
-[SNConnectionInfo skipPeerErrorReason];
-[SNConnectionInfo setLanguageCode:];
-[SNConnectionInfo connectionProtocolTechnology];
```
