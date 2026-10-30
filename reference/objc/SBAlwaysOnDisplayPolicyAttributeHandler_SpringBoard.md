# `SBAlwaysOnDisplayPolicyAttributeHandler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHLocalCountingAssertionAttributeHandler`
- 2 instance variables, 0 properties, 4 instance methods, 3 class methods

## Instance variables

```
@"<SBAlwaysOnDisplayPolicySuspensionProvider>" _provider;
@"NSMutableDictionary" _suspensionAssertions;
```

## Class methods

```
+[SBAlwaysOnDisplayPolicyAttributeHandler attributeBaseClass];
+[SBAlwaysOnDisplayPolicyAttributeHandler attributeClasses];
+[SBAlwaysOnDisplayPolicyAttributeHandler registerHandlerForService:provider:];
```

## Instance methods

```
-[SBAlwaysOnDisplayPolicyAttributeHandler activateWithFirstEntry:];
-[SBAlwaysOnDisplayPolicyAttributeHandler countingTargetForEntry:];
-[SBAlwaysOnDisplayPolicyAttributeHandler deactivateWithFinalEntry:];
-[SBAlwaysOnDisplayPolicyAttributeHandler initWithService:provider:];
```
