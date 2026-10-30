# `THPreferredThreadNetwork`

- Image: [`/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread`](../userland/System__Library__PrivateFrameworks__CoreThread.framework__CoreThread.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"THThreadNetwork" _network;
@"THNetworkSignature" _networkSignature;
@"THThreadNetworkCredentialsActiveDataSetRecord" _credentialsDataSetRecord;
@"NSString" _userInfo;
@"NSDate" _creationDate;
@"NSDate" _lastModificationDate;
```

## Properties

```
@property (T@"THThreadNetwork",R,N,V_network) network;
@property (T@"THNetworkSignature",R,N,V_networkSignature) networkSignature;
@property (T@"THThreadNetworkCredentialsActiveDataSetRecord",R,N,V_credentialsDataSetRecord) credentialsDataSetRecord;
@property (T@"NSString",C,N,V_userInfo) userInfo;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
```

## Class methods

```
+[THPreferredThreadNetwork supportsSecureCoding];
```

## Instance methods

```
-[THPreferredThreadNetwork networkSignature];
-[THPreferredThreadNetwork network];
-[THPreferredThreadNetwork userInfo];
-[THPreferredThreadNetwork setUserInfo:];
-[THPreferredThreadNetwork creationDate];
-[THPreferredThreadNetwork encodeWithCoder:];
-[THPreferredThreadNetwork initWithCoder:];
-[THPreferredThreadNetwork updateUserInfo:];
-[THPreferredThreadNetwork lastModificationDate];
-[THPreferredThreadNetwork credentialsDataSetRecord];
-[THPreferredThreadNetwork initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:];
```
