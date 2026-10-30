# `_UISceneCarPlaySessionTouchpad`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`
- 4 instance variables, 9 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _senderID;
d _sensitivity;
Q _supportedFeedbackTypes;
{CGSize="width"d"height"d} _physicalSize;
```

## Properties

```
@property (TQ,R,N,V_senderID) senderID;
@property (Td,R,N,V_sensitivity) sensitivity;
@property (T{CGSize=dd},R,N,V_physicalSize) physicalSize;
@property (TQ,R,N,V_supportedFeedbackTypes) supportedFeedbackTypes;
@property (TB,R,N) feedbackSupported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneCarPlaySessionTouchpad sensitivity];
-[_UISceneCarPlaySessionTouchpad physicalSize];
-[_UISceneCarPlaySessionTouchpad initWithXPCDictionary:];
-[_UISceneCarPlaySessionTouchpad senderID];
-[_UISceneCarPlaySessionTouchpad encodeWithXPCDictionary:];
-[_UISceneCarPlaySessionTouchpad feedbackSupported];
-[_UISceneCarPlaySessionTouchpad initWithSenderID:sensitivity:physicalSize:supportedFeedbackTypes:];
-[_UISceneCarPlaySessionTouchpad supportedFeedbackTypes];
```
