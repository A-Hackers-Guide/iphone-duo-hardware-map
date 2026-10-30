# `THThreadNetworkCredentialsActiveDataSetRecord`

- Image: [`/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread`](../userland/System__Library__PrivateFrameworks__CoreThread.framework__CoreThread.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"THThreadNetworkBorderAgent" _borderAgent;
@"THThreadNetworkCredentialsDataSet" _credentialsDataSet;
@"THThreadNetwork" _network;
@"THThreadNetworkCredentials" _credentials;
@"NSUUID" _uniqueIdentifier;
@"NSString" _keychainAccessGroup;
@"NSDate" _creationDate;
@"NSDate" _lastModificationDate;
```

## Properties

```
@property (T@"THThreadNetworkBorderAgent",R,N,V_borderAgent) borderAgent;
@property (T@"THThreadNetworkCredentialsDataSet",R,N,V_credentialsDataSet) credentialsDataSet;
@property (T@"THThreadNetwork",R,N,V_network) network;
@property (T@"THThreadNetworkCredentials",&,N,V_credentials) credentials;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,N,V_keychainAccessGroup) keychainAccessGroup;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
```

## Class methods

```
+[THThreadNetworkCredentialsActiveDataSetRecord supportsSecureCoding];
```

## Instance methods

```
-[THThreadNetworkCredentialsActiveDataSetRecord network];
-[THThreadNetworkCredentialsActiveDataSetRecord creationDate];
-[THThreadNetworkCredentialsActiveDataSetRecord uniqueIdentifier];
-[THThreadNetworkCredentialsActiveDataSetRecord encodeWithCoder:];
-[THThreadNetworkCredentialsActiveDataSetRecord initWithCoder:];
-[THThreadNetworkCredentialsActiveDataSetRecord keychainAccessGroup];
-[THThreadNetworkCredentialsActiveDataSetRecord credentials];
-[THThreadNetworkCredentialsActiveDataSetRecord lastModificationDate];
-[THThreadNetworkCredentialsActiveDataSetRecord setCredentials:];
-[THThreadNetworkCredentialsActiveDataSetRecord borderAgent];
-[THThreadNetworkCredentialsActiveDataSetRecord credentialsDataSet];
-[THThreadNetworkCredentialsActiveDataSetRecord initWithBorderAgent:credentialsDataSet:network:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:];
```
