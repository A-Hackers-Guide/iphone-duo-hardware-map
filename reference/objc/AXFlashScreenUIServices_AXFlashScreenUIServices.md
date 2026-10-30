# `AXFlashScreenUIServices`

- Image: [`/System/Library/PrivateFrameworks/AXFlashScreenUIServices.framework/AXFlashScreenUIServices`](../userland/System__Library__PrivateFrameworks__AXFlashScreenUIServices.framework__AXFlashScreenUIServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AXUIClientDelegate`
- 1 instance variables, 5 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"AXUIClient" _flashScreenUIClient;
```

## Properties

```
@property (T@"AXUIClient",&,N,V_flashScreenUIClient) flashScreenUIClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AXFlashScreenUIServices sharedInstance];
+[AXFlashScreenUIServices possibleRequiredEntitlementsForProcessingMessageWithIdentifier:];
```

## Instance methods

```
-[AXFlashScreenUIServices hide];
-[AXFlashScreenUIServices dealloc];
-[AXFlashScreenUIServices show];
-[AXFlashScreenUIServices userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:];
-[AXFlashScreenUIServices userInterfaceClient:processMessageFromServer:withIdentifier:error:];
-[AXFlashScreenUIServices flashScreenUIClient];
-[AXFlashScreenUIServices setFlashScreenUIClient:];
-[AXFlashScreenUIServices flashWithDuration:];
```
