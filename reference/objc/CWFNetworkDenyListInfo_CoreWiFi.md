# `CWFNetworkDenyListInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
Q _reason;
q _reasonData;
@"NSString" _reasonString;
d _reasonTimestamp;
d _stateTimestamp;
@"NSString" _BSSID;
Q _state;
@"NSString" _stateString;
```

## Properties

```
@property (TQ,V_reason) reason;
@property (Tq,V_reasonData) reasonData;
@property (T@"NSString",C,V_reasonString) reasonString;
@property (Td,V_reasonTimestamp) reasonTimestamp;
@property (Td,V_stateTimestamp) stateTimestamp;
@property (T@"NSString",C,V_BSSID) BSSID;
@property (TQ,V_state) state;
@property (T@"NSString",C,V_stateString) stateString;
```

## Instance methods

```
-[CWFNetworkDenyListInfo BSSID];
-[CWFNetworkDenyListInfo setState:];
-[CWFNetworkDenyListInfo setBSSID:];
-[CWFNetworkDenyListInfo init];
-[CWFNetworkDenyListInfo setReason:];
-[CWFNetworkDenyListInfo reason];
-[CWFNetworkDenyListInfo stateString];
-[CWFNetworkDenyListInfo state];
-[CWFNetworkDenyListInfo reasonString];
-[CWFNetworkDenyListInfo setReasonString:];
-[CWFNetworkDenyListInfo setStateString:];
-[CWFNetworkDenyListInfo reasonTimestamp];
-[CWFNetworkDenyListInfo reasonData];
-[CWFNetworkDenyListInfo setReasonData:];
-[CWFNetworkDenyListInfo setReasonTimestamp:];
-[CWFNetworkDenyListInfo setStateTimestamp:];
-[CWFNetworkDenyListInfo stateTimestamp];
```
