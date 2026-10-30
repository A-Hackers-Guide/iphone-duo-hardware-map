# `SBCommunicationPolicyManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _policiesByBundleIdentifier;
@"DMFCommunicationPolicyMonitor" _communicationPolicyMonitor;
```

## Class methods

```
+[SBCommunicationPolicyManager sharedInstance];
```

## Instance methods

```
-[SBCommunicationPolicyManager observeValueForKeyPath:ofObject:change:context:];
-[SBCommunicationPolicyManager init];
-[SBCommunicationPolicyManager dealloc];
-[SBCommunicationPolicyManager shouldScreenTimeSuppressNotificationsForBundleIdentifier:];
```
