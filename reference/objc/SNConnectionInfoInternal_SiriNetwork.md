# `SNConnectionInfoInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 25 properties, 51 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionConfiguration;
@"SAConnectionPolicy" policy;
@"SAConnectionPolicyRoute" policyRoute;
```

## Properties

```
@property (T@"SAConnectionPolicy",N,&,Vpolicy) policy;
@property (T@"SAConnectionPolicyRoute",N,&,VpolicyRoute) policyRoute;
@property (Tq,N) connectionProtocolTechnology;
@property (Tq,N) communicationProtocolTechnology;
@property (T@"NSString",N,C) assistantIdentifier;
@property (T@"NSString",N,C) peerAssistantIdentifier;
@property (T@"NSString",N,C) connectionId;
@property (T@"NSString",N,C) aceHost;
@property (T@"NSString",N,C) languageCode;
@property (TB,N) prefersWWAN;
@property (TB,N) skipPeer;
@property (TB,N) useWiFiHint;
@property (T@"NSError",N,C) skipPeerErrorReason;
@property (TB,N) forceReconnect;
@property (Td,N) timeout;
@property (TB,N) imposePolicyBan;
@property (T@"SAConnectionPolicy",N,&) connectionPolicy;
@property (T@"SAConnectionPolicyRoute",N,&) connectionPolicyRoute;
@property (TB,N) forceOnDeviceOnlyDictation;
@property (T@"NSString",N,C) productTypePrefix;
@property (T@"NSString",N,C) peerType;
@property (T@"NSString",N,C) peerVersion;
@property (TB,N) deviceIsInWalkaboutExperimentGroup;
@property (TB,N) usesProxyConnection;
@property (TB,N) usesPeerManagedSync;
```

## Instance methods

```
-[SNConnectionInfoInternal setConnectionProtocolTechnology:];
-[SNConnectionInfoInternal setPeerVersion:];
-[SNConnectionInfoInternal forceOnDeviceOnlyDictation];
-[SNConnectionInfoInternal setForceReconnect:];
-[SNConnectionInfoInternal setSkipPeer:];
-[SNConnectionInfoInternal peerType];
-[SNConnectionInfoInternal setAceHost:];
-[SNConnectionInfoInternal setUsesPeerManagedSync:];
-[SNConnectionInfoInternal assistantIdentifier];
-[SNConnectionInfoInternal init];
-[SNConnectionInfoInternal setPrefersWWAN:];
-[SNConnectionInfoInternal prefersWWAN];
-[SNConnectionInfoInternal setForceOnDeviceOnlyDictation:];
-[SNConnectionInfoInternal setConnectionPolicy:];
-[SNConnectionInfoInternal connectionPolicyRoute];
-[SNConnectionInfoInternal connectionId];
-[SNConnectionInfoInternal setConnectionId:];
-[SNConnectionInfoInternal timeout];
-[SNConnectionInfoInternal languageCode];
-[SNConnectionInfoInternal setUseWiFiHint:];
-[SNConnectionInfoInternal setProductTypePrefix:];
-[SNConnectionInfoInternal setSkipPeerErrorReason:];
-[SNConnectionInfoInternal setPolicyRoute:];
-[SNConnectionInfoInternal setTimeout:];
-[SNConnectionInfoInternal forceReconnect];
-[SNConnectionInfoInternal deviceIsInWalkaboutExperimentGroup];
-[SNConnectionInfoInternal setUsesProxyConnection:];
-[SNConnectionInfoInternal setPeerType:];
-[SNConnectionInfoInternal setCommunicationProtocolTechnology:];
-[SNConnectionInfoInternal setDeviceIsInWalkaboutExperimentGroup:];
-[SNConnectionInfoInternal setConnectionPolicyRoute:];
-[SNConnectionInfoInternal productTypePrefix];
-[SNConnectionInfoInternal peerAssistantIdentifier];
-[SNConnectionInfoInternal setImposePolicyBan:];
-[SNConnectionInfoInternal peerVersion];
-[SNConnectionInfoInternal setPeerAssistantIdentifier:];
-[SNConnectionInfoInternal usesProxyConnection];
-[SNConnectionInfoInternal connectionPolicy];
-[SNConnectionInfoInternal useWiFiHint];
-[SNConnectionInfoInternal imposePolicyBan];
-[SNConnectionInfoInternal policyRoute];
-[SNConnectionInfoInternal usesPeerManagedSync];
-[SNConnectionInfoInternal aceHost];
-[SNConnectionInfoInternal setAssistantIdentifier:];
-[SNConnectionInfoInternal skipPeer];
-[SNConnectionInfoInternal setPolicy:];
-[SNConnectionInfoInternal communicationProtocolTechnology];
-[SNConnectionInfoInternal skipPeerErrorReason];
-[SNConnectionInfoInternal policy];
-[SNConnectionInfoInternal setLanguageCode:];
-[SNConnectionInfoInternal connectionProtocolTechnology];
```
