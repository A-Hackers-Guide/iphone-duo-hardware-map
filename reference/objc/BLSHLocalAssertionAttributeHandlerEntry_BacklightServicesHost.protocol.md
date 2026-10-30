# `BLSHLocalAssertionAttributeHandlerEntry` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BSInvalidatable`
- 0 instance variables, 3 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T@"BLSAttribute",R,W,N) attribute;
@property (T@"<BLSAssertionServiceResponding>",R,W,N) assertion;
@property (T@"<BLSHAssertionAttributeHandlerService>",R,W,N) service;
```

## Class methods

```
+[BLSHLocalAssertionAttributeHandlerEntry activateForAttribute:fromAssertion:forService:attributeHandler:];
```

## Instance methods

```
-[BLSHLocalAssertionAttributeHandlerEntry assertion];
-[BLSHLocalAssertionAttributeHandlerEntry service];
-[BLSHLocalAssertionAttributeHandlerEntry attribute];
-[BLSHLocalAssertionAttributeHandlerEntry reactivateIfPossible];
```
