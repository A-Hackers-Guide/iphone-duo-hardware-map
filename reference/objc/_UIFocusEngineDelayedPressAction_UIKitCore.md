# `_UIFocusEngineDelayedPressAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"_UIFocusEventRecognizer" _sender;
q _pressType;
d _timestamp;
```

## Properties

```
@property (T@"_UIFocusEventRecognizer",R,W,N,V_sender) sender;
@property (Tq,R,N,V_pressType) pressType;
@property (Td,R,N,V_timestamp) timestamp;
```

## Class methods

```
+[_UIFocusEngineDelayedPressAction sendDelayedPressWithType:timestamp:sender:];
```

## Instance methods

```
-[_UIFocusEngineDelayedPressAction timestamp];
-[_UIFocusEngineDelayedPressAction sender];
-[_UIFocusEngineDelayedPressAction _sendPressEvent];
-[_UIFocusEngineDelayedPressAction _initWithPressType:timestamp:sender:];
-[_UIFocusEngineDelayedPressAction pressType];
```
