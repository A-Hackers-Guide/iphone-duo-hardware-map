# `CLGNSSStateQueryAssertionResponse`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 2 class methods

## Instance variables

```
{unique_ptr<CLGNSSStateQueryAssertionResponseInternal, std::default_delete<CLGNSSStateQueryAssertionResponseInternal>>=""{?="__ptr_"^{CLGNSSStateQueryAssertionResponseInternal}}} fInternal;
```

## Class methods

```
+[CLGNSSStateQueryAssertionResponse newAssertionForBundle:withReason:callbackQueue:completionHandler:];
+[CLGNSSStateQueryAssertionResponse newAssertionForBundleIdentifier:withReason:callbackQueue:completionHandler:];
```

## Instance methods

```
-[CLGNSSStateQueryAssertionResponse dealloc];
-[CLGNSSStateQueryAssertionResponse invalidate];
-[CLGNSSStateQueryAssertionResponse initWithRegistrationMessageName:messagePayload:callbackQueue:completionHandler:];
```
