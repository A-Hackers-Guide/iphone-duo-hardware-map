# `THCredentials`

- Image: [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](../userland/System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
C _channel;
@"NSString" _networkName;
@"NSData" _extendedPANID;
@"NSData" _borderAgentID;
@"NSData" _activeOperationalDataSet;
@"NSData" _networkKey;
@"NSData" _PSKC;
@"NSData" _panID;
@"NSDate" _creationDate;
@"NSDate" _lastModificationDate;
```

## Properties

```
@property (T@"NSString",R,N,V_networkName) networkName;
@property (T@"NSData",R,N,V_extendedPANID) extendedPANID;
@property (T@"NSData",R,N,V_borderAgentID) borderAgentID;
@property (T@"NSData",R,N,V_activeOperationalDataSet) activeOperationalDataSet;
@property (T@"NSData",R,N,V_networkKey) networkKey;
@property (T@"NSData",R,N,V_PSKC) PSKC;
@property (TC,N,V_channel) channel;
@property (T@"NSData",R,N,V_panID) panID;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
```

## Class methods

```
+[THCredentials supportsSecureCoding];
```

## Instance methods

```
-[THCredentials setChannel:];
-[THCredentials channel];
-[THCredentials networkName];
-[THCredentials creationDate];
-[THCredentials encodeWithCoder:];
-[THCredentials initWithCoder:];
-[THCredentials extendedPANID];
-[THCredentials lastModificationDate];
-[THCredentials activeOperationalDataSet];
-[THCredentials panID];
-[THCredentials PSKC];
-[THCredentials networkKey];
-[THCredentials borderAgentID];
-[THCredentials initThreadCredentials:extendedPANID:borderAgentID:activeOperationalDataSet:PSKC:networkKey:channel:panID:creationDate:lastModificationDate:];
-[THCredentials initWithActiveDataSetRecord:];
```
