# `UISIntentForwardingActionResponse`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSActionResponse`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"INIntentResponse" _cachedIntentResponse;
@"INIntentForwardingActionResponse" _cachedIntentForwardingActionResponse;
```

## Properties

```
@property (T@"INIntentResponse",R,N) intentResponse;
@property (T@"INIntentForwardingActionResponse",R,N) intentForwardingActionResponse;
```

## Class methods

```
+[UISIntentForwardingActionResponse responseWithIntentForwardingActionResponse:];
+[UISIntentForwardingActionResponse responseWithIntentResponse:];
```

## Instance methods

```
-[UISIntentForwardingActionResponse abortForUsageViolation:];
-[UISIntentForwardingActionResponse keyDescriptionForSetting:];
-[UISIntentForwardingActionResponse intentResponse];
-[UISIntentForwardingActionResponse initWithIntentForwardingActionResponse:];
-[UISIntentForwardingActionResponse initWithIntentResponse:];
-[UISIntentForwardingActionResponse intentForwardingActionResponse];
```
