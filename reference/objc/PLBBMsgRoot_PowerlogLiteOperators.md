# `PLBBMsgRoot`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _msgName;
@"NSNumber" _msgType;
@"NSString" _msgPayload;
@"NSString" _msgProcErr;
@"NSDate" _msgDate;
@"NSDictionary" _msgEntry;
@"NSDictionary" _msgKVPairs;
@"PLAgent" _agent;
```

## Properties

```
@property (T@"NSString",&,N,V_msgName) msgName;
@property (T@"NSNumber",&,N,V_msgType) msgType;
@property (T@"NSString",&,N,V_msgPayload) msgPayload;
@property (T@"NSString",&,N,V_msgProcErr) msgProcErr;
@property (T@"NSDate",&,N,V_msgDate) msgDate;
@property (T@"NSDictionary",&,N,V_msgEntry) msgEntry;
@property (T@"NSDictionary",&,N,V_msgKVPairs) msgKVPairs;
@property (T@"PLAgent",&,N,V_agent) agent;
```

## Instance methods

```
-[PLBBMsgRoot init];
-[PLBBMsgRoot agent];
-[PLBBMsgRoot setAgent:];
-[PLBBMsgRoot msgName];
-[PLBBMsgRoot msgType];
-[PLBBMsgRoot msgDate];
-[PLBBMsgRoot appendToMsgProcError:];
-[PLBBMsgRoot msgEntry];
-[PLBBMsgRoot msgKVPairs];
-[PLBBMsgRoot msgPayload];
-[PLBBMsgRoot msgProcErr];
-[PLBBMsgRoot sendAndLogPLEntry:andOverride:];
-[PLBBMsgRoot setMsgDate:];
-[PLBBMsgRoot setMsgEntry:];
-[PLBBMsgRoot setMsgKVPairs:];
-[PLBBMsgRoot setMsgName:];
-[PLBBMsgRoot setMsgPayload:];
-[PLBBMsgRoot setMsgProcErr:];
-[PLBBMsgRoot setMsgType:];
```
