# `WiFiUsageWatchdogDetails`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
i _unavailableReason;
i _unavailableSubreason;
i _availableReason;
i _availableSubreason;
Q _flags;
@"NSString" _unavailableReasonString;
@"NSString" _availableReasonString;
@"WiFiUsageBssDetails" _connectedBss;
@"NSDate" _createdAt;
@"NSString" _interfaceName;
```

## Properties

```
@property (T@"NSString",&,N,V_interfaceName) interfaceName;
@property (T@"WiFiUsageBssDetails",&,N,V_connectedBss) connectedBss;
@property (T@"NSDate",&,N,V_createdAt) createdAt;
@property (TQ,N,V_flags) flags;
@property (Ti,N,V_unavailableReason) unavailableReason;
@property (Ti,N,V_unavailableSubreason) unavailableSubreason;
@property (T@"NSString",&,N,V_unavailableReasonString) unavailableReasonString;
@property (Ti,N,V_availableReason) availableReason;
@property (Ti,N,V_availableSubreason) availableSubreason;
@property (T@"NSString",&,N,V_availableReasonString) availableReasonString;
```

## Instance methods

```
-[WiFiUsageWatchdogDetails setFlags:];
-[WiFiUsageWatchdogDetails flags];
-[WiFiUsageWatchdogDetails connectedBss];
-[WiFiUsageWatchdogDetails setInterfaceName:];
-[WiFiUsageWatchdogDetails interfaceName];
-[WiFiUsageWatchdogDetails setConnectedBss:];
-[WiFiUsageWatchdogDetails setCreatedAt:];
-[WiFiUsageWatchdogDetails createdAt];
-[WiFiUsageWatchdogDetails availableReason];
-[WiFiUsageWatchdogDetails availableReasonString];
-[WiFiUsageWatchdogDetails availableSubreason];
-[WiFiUsageWatchdogDetails initWithInterfaceName:andConnectedBss:];
-[WiFiUsageWatchdogDetails reportedReason];
-[WiFiUsageWatchdogDetails reportedReasonString];
-[WiFiUsageWatchdogDetails reportedSubreason];
-[WiFiUsageWatchdogDetails reportedSubreasonString];
-[WiFiUsageWatchdogDetails setAvailableReason:];
-[WiFiUsageWatchdogDetails setAvailableReasonString:];
-[WiFiUsageWatchdogDetails setAvailableSubreason:];
-[WiFiUsageWatchdogDetails setUnavailableReason:];
-[WiFiUsageWatchdogDetails setUnavailableReasonString:];
-[WiFiUsageWatchdogDetails setUnavailableSubreason:];
-[WiFiUsageWatchdogDetails unavailableReason];
-[WiFiUsageWatchdogDetails unavailableReasonString];
-[WiFiUsageWatchdogDetails unavailableSubreason];
```
