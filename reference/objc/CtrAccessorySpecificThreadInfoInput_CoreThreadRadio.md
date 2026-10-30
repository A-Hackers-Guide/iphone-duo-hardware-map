# `CtrAccessorySpecificThreadInfoInput`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 18 instance variables, 18 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _isWrite;
B _isLinkFallBack;
@"NSString" _accessoryManufacturer;
@"NSString" _accessoryModel;
@"NSString" _hostName;
@"NSString" _serviceInstanceName;
@"NSString" _ipv6Address;
q _browseStatus;
q _resolveStatus;
q _transactionStatus;
q _communicationProtocol;
q _hapThreadAccessoryCapabilities;
Q _errorCode;
Q _hapCoAPTokenInfo;
Q _matterSessionInfo;
Q _consecutiveFailureCount;
Q _consecutiveSuccessCount;
Q _durationSecondsSinceLastSuccessfulRequest;
```

## Properties

```
@property (T@"NSString",R,V_accessoryManufacturer) accessoryManufacturer;
@property (T@"NSString",R,V_accessoryModel) accessoryModel;
@property (T@"NSString",R,V_hostName) hostName;
@property (T@"NSString",R,V_serviceInstanceName) serviceInstanceName;
@property (T@"NSString",R,V_ipv6Address) ipv6Address;
@property (Tq,R,V_browseStatus) browseStatus;
@property (Tq,R,V_resolveStatus) resolveStatus;
@property (Tq,R,V_transactionStatus) transactionStatus;
@property (TB,R,V_isWrite) isWrite;
@property (TB,R,V_isLinkFallBack) isLinkFallBack;
@property (Tq,R,V_communicationProtocol) communicationProtocol;
@property (Tq,R,V_hapThreadAccessoryCapabilities) hapThreadAccessoryCapabilities;
@property (TQ,R,V_errorCode) errorCode;
@property (TQ,R,V_hapCoAPTokenInfo) hapCoAPTokenInfo;
@property (TQ,R,V_matterSessionInfo) matterSessionInfo;
@property (TQ,R,V_consecutiveFailureCount) consecutiveFailureCount;
@property (TQ,R,V_consecutiveSuccessCount) consecutiveSuccessCount;
@property (TQ,R,V_durationSecondsSinceLastSuccessfulRequest) durationSecondsSinceLastSuccessfulRequest;
```

## Class methods

```
+[CtrAccessorySpecificThreadInfoInput supportsSecureCoding];
```

## Instance methods

```
-[CtrAccessorySpecificThreadInfoInput errorCode];
-[CtrAccessorySpecificThreadInfoInput hostName];
-[CtrAccessorySpecificThreadInfoInput encodeWithCoder:];
-[CtrAccessorySpecificThreadInfoInput initWithCoder:];
-[CtrAccessorySpecificThreadInfoInput isWrite];
-[CtrAccessorySpecificThreadInfoInput transactionStatus];
-[CtrAccessorySpecificThreadInfoInput communicationProtocol];
-[CtrAccessorySpecificThreadInfoInput ipv6Address];
-[CtrAccessorySpecificThreadInfoInput accessoryModel];
-[CtrAccessorySpecificThreadInfoInput consecutiveFailureCount];
-[CtrAccessorySpecificThreadInfoInput accessoryManufacturer];
-[CtrAccessorySpecificThreadInfoInput consecutiveSuccessCount];
-[CtrAccessorySpecificThreadInfoInput browseStatus];
-[CtrAccessorySpecificThreadInfoInput durationSecondsSinceLastSuccessfulRequest];
-[CtrAccessorySpecificThreadInfoInput hapCoAPTokenInfo];
-[CtrAccessorySpecificThreadInfoInput hapThreadAccessoryCapabilities];
-[CtrAccessorySpecificThreadInfoInput initData:accessoryModel:hostName:serviceInstanceName:ipv6Address:browseStatus:resolveStatus:transactionStatus:isWrite:isLinkFallback:communicationProtocol:hapThreadAccessoryCapabilities:errorCode:hapTokenInfo:matterSessionInfo:consecutiveFailureCount:consecutiveSuccessCount:durationSecondsSinceLastSuccessfulRequest:];
-[CtrAccessorySpecificThreadInfoInput isLinkFallBack];
-[CtrAccessorySpecificThreadInfoInput matterSessionInfo];
-[CtrAccessorySpecificThreadInfoInput resolveStatus];
-[CtrAccessorySpecificThreadInfoInput serviceInstanceName];
```
