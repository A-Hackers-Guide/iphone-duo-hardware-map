# `THThreadNetworkCredentials`

- Image: [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](../userland/System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 21 instance methods, 1 class methods

## Instance variables

```
C _channel;
B _isActiveDevice;
@"NSData" _masterKey;
@"NSString" _passPhrase;
@"NSData" _PSKc;
@"NSData" _PANID;
@"NSString" _userInfo;
@"THThreadNetworkCredentialsDataSet" _credentialsDataSet;
```

## Properties

```
@property (T@"NSData",C,N,V_masterKey) masterKey;
@property (T@"NSString",C,N,V_passPhrase) passPhrase;
@property (T@"NSData",C,N,V_PSKc) PSKc;
@property (TC,N,V_channel) channel;
@property (T@"NSData",C,N,V_PANID) PANID;
@property (T@"NSString",C,N,V_userInfo) userInfo;
@property (T@"THThreadNetworkCredentialsDataSet",&,N,V_credentialsDataSet) credentialsDataSet;
@property (TB,N,V_isActiveDevice) isActiveDevice;
```

## Class methods

```
+[THThreadNetworkCredentials supportsSecureCoding];
```

## Instance methods

```
-[THThreadNetworkCredentials setChannel:];
-[THThreadNetworkCredentials channel];
-[THThreadNetworkCredentials init];
-[THThreadNetworkCredentials userInfo];
-[THThreadNetworkCredentials setUserInfo:];
-[THThreadNetworkCredentials encodeWithCoder:];
-[THThreadNetworkCredentials initWithCoder:];
-[THThreadNetworkCredentials PSKc];
-[THThreadNetworkCredentials PANID];
-[THThreadNetworkCredentials masterKey];
-[THThreadNetworkCredentials passPhrase];
-[THThreadNetworkCredentials setMasterKey:];
-[THThreadNetworkCredentials isActiveDevice];
-[THThreadNetworkCredentials credentialsDataSet];
-[THThreadNetworkCredentials initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:];
-[THThreadNetworkCredentials initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:credentialDataSet:isActiveDevice:];
-[THThreadNetworkCredentials setCredentialsDataSet:];
-[THThreadNetworkCredentials setIsActiveDevice:];
-[THThreadNetworkCredentials setPANID:];
-[THThreadNetworkCredentials setPSKc:];
-[THThreadNetworkCredentials setPassPhrase:];
```
