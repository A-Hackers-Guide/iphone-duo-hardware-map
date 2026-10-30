# `WFBlacklistStateNode`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _blacklistedState;
@"NSString" _blacklistedStateString;
d _blacklistedStateTimestamp;
Q _blacklistedReason;
q _blacklistedReasonData;
@"NSString" _blacklistedReasonString;
```

## Properties

```
@property (TQ,V_blacklistedState) blacklistedState;
@property (T@"NSString",C,V_blacklistedStateString) blacklistedStateString;
@property (Td,V_blacklistedStateTimestamp) blacklistedStateTimestamp;
@property (TQ,V_blacklistedReason) blacklistedReason;
@property (Tq,V_blacklistedReasonData) blacklistedReasonData;
@property (T@"NSString",C,V_blacklistedReasonString) blacklistedReasonString;
```

## Instance methods

```
-[WFBlacklistStateNode init];
-[WFBlacklistStateNode blacklistedReason];
-[WFBlacklistStateNode blacklistedReasonData];
-[WFBlacklistStateNode blacklistedReasonString];
-[WFBlacklistStateNode blacklistedState];
-[WFBlacklistStateNode blacklistedStateString];
-[WFBlacklistStateNode blacklistedStateTimestamp];
-[WFBlacklistStateNode setBlacklistedReason:];
-[WFBlacklistStateNode setBlacklistedReasonData:];
-[WFBlacklistStateNode setBlacklistedReasonString:];
-[WFBlacklistStateNode setBlacklistedState:];
-[WFBlacklistStateNode setBlacklistedStateString:];
-[WFBlacklistStateNode setBlacklistedStateTimestamp:];
```
