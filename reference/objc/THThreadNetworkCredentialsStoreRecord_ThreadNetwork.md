# `THThreadNetworkCredentialsStoreRecord`

- Image: [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](../userland/System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"THThreadNetwork" _network;
@"THThreadNetworkCredentials" _credentials;
@"NSUUID" _uniqueIdentifier;
@"NSString" _keychainAccessGroup;
@"NSDate" _creationDate;
@"NSDate" _lastModificationDate;
```

## Properties

```
@property (T@"THThreadNetwork",R,N,V_network) network;
@property (T@"THThreadNetworkCredentials",R,N,V_credentials) credentials;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,N,V_keychainAccessGroup) keychainAccessGroup;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
```

## Class methods

```
+[THThreadNetworkCredentialsStoreRecord supportsSecureCoding];
```

## Instance methods

```
-[THThreadNetworkCredentialsStoreRecord network];
-[THThreadNetworkCredentialsStoreRecord creationDate];
-[THThreadNetworkCredentialsStoreRecord uniqueIdentifier];
-[THThreadNetworkCredentialsStoreRecord encodeWithCoder:];
-[THThreadNetworkCredentialsStoreRecord initWithCoder:];
-[THThreadNetworkCredentialsStoreRecord keychainAccessGroup];
-[THThreadNetworkCredentialsStoreRecord credentials];
-[THThreadNetworkCredentialsStoreRecord lastModificationDate];
-[THThreadNetworkCredentialsStoreRecord initWithNetwork:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:];
```
