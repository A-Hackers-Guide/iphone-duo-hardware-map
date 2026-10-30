# `CLGnssDisablementAssertion`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 2 class methods

## Instance variables

```
{unique_ptr<CLGnssDisablementAssertionInternal, std::default_delete<CLGnssDisablementAssertionInternal>>=""{?="__ptr_"^{CLGnssDisablementAssertionInternal}}} fInternal;
```

## Class methods

```
+[CLGnssDisablementAssertion newAssertionForBundle:withReason:callbackQueue:completionHandler:];
+[CLGnssDisablementAssertion newAssertionForBundleIdentifier:withReason:callbackQueue:completionHandler:];
```

## Instance methods

```
-[CLGnssDisablementAssertion dealloc];
-[CLGnssDisablementAssertion invalidate];
-[CLGnssDisablementAssertion initWithRegistrationMessageName:messagePayload:callbackQueue:completionHandler:];
```
