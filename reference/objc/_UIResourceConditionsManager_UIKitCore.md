# `_UIResourceConditionsManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _systemPrefersReducedResourceUsage;
@"<BSInvalidatable>" _stateCaptureToken;
resourceUsageSystemPreferencePerScene;
```

## Properties

```
@property (TB,N,R) systemPrefersReducedResourceUsage;
@property (TB,N,V_systemPrefersReducedResourceUsage) _systemPrefersReducedResourceUsage;
@property (T@"<BSInvalidatable>",N,&,V_stateCaptureToken) _stateCaptureToken;
@property (T@"NSString",N,R) debugDescription;
```

## Class methods

```
+[_UIResourceConditionsManager sharedManager];
```

## Instance methods

```
-[_UIResourceConditionsManager debugDescription];
-[_UIResourceConditionsManager init];
-[_UIResourceConditionsManager dealloc];
-[_UIResourceConditionsManager set_systemPrefersReducedResourceUsage:];
-[_UIResourceConditionsManager set_stateCaptureToken:];
-[_UIResourceConditionsManager _stateCaptureToken];
-[_UIResourceConditionsManager systemPrefersReducedResourceUsage];
-[_UIResourceConditionsManager removeSceneWithIdentifier:];
-[_UIResourceConditionsManager recomputeAggregateResourceUsageSystemPreference];
-[_UIResourceConditionsManager updateHostResourceUsagePreference:forSceneIdentifier:];
-[_UIResourceConditionsManager _systemPrefersReducedResourceUsage];
```
