# `SBAlwaysOnPolicy` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisAlwaysOnPolicyActive) alwaysOnPolicyActive;
@property (T@"NSString",R,C,N) analyticsPolicyName;
@property (T@,R,C,N) analyticsPolicyValue;
@property (class, T@"NSString",?,R,C,N) policyIdentifier;
```

## Instance methods

```
-[SBAlwaysOnPolicy activateAlwaysOnPolicy];
-[SBAlwaysOnPolicy analyticsPolicyName];
-[SBAlwaysOnPolicy analyticsPolicyValue];
-[SBAlwaysOnPolicy isAlwaysOnPolicyActive];
-[SBAlwaysOnPolicy acquirePolicySuspensionAssertionForReason:];
```
