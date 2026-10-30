# `BLSHCountingAssertionAttributeEntry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHLocalAssertionAttributeHandlerEntry`
- 4 instance variables, 7 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BLSHLocalCountingAssertionAttributeHandler" _attributeHandler;
@"BLSAttribute" _attribute;
@"<BLSAssertionServiceResponding>" _assertion;
@"<BLSHAssertionAttributeHandlerService>" _service;
```

## Properties

```
@property (T@"BLSAttribute",R,W,N,V_attribute) attribute;
@property (T@"<BLSAssertionServiceResponding>",R,W,N,V_assertion) assertion;
@property (T@"<BLSHAssertionAttributeHandlerService>",R,W,N,V_service) service;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHCountingAssertionAttributeEntry activateForAttribute:fromAssertion:forService:attributeHandler:];
```

## Instance methods

```
-[BLSHCountingAssertionAttributeEntry assertion];
-[BLSHCountingAssertionAttributeEntry invalidate];
-[BLSHCountingAssertionAttributeEntry service];
-[BLSHCountingAssertionAttributeEntry description];
-[BLSHCountingAssertionAttributeEntry attribute];
-[BLSHCountingAssertionAttributeEntry initForAttribute:fromAssertion:forService:attributeHandler:];
-[BLSHCountingAssertionAttributeEntry reactivateIfPossible];
```
