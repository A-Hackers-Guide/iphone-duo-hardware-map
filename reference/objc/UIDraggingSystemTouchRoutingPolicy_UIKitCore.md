# `UIDraggingSystemTouchRoutingPolicy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _hitTestingDisabled;
@"NSDictionary" _contextIDsToAlwaysSendTouchesByDisplayIdentifier;
@"NSArray" _contextIDsToExcludeFromHitTesting;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_contextIDsToAlwaysSendTouchesByDisplayIdentifier) contextIDsToAlwaysSendTouchesByDisplayIdentifier;
@property (T@"NSArray",C,N,V_contextIDsToExcludeFromHitTesting) contextIDsToExcludeFromHitTesting;
@property (TB,N,GisHitTestingDisabled,V_hitTestingDisabled) hitTestingDisabled;
```

## Class methods

```
+[UIDraggingSystemTouchRoutingPolicy supportsSecureCoding];
```

## Instance methods

```
-[UIDraggingSystemTouchRoutingPolicy isHitTestingDisabled];
-[UIDraggingSystemTouchRoutingPolicy setHitTestingDisabled:];
-[UIDraggingSystemTouchRoutingPolicy encodeWithCoder:];
-[UIDraggingSystemTouchRoutingPolicy description];
-[UIDraggingSystemTouchRoutingPolicy initWithCoder:];
-[UIDraggingSystemTouchRoutingPolicy contextIDsToAlwaysSendTouchesByDisplayIdentifier];
-[UIDraggingSystemTouchRoutingPolicy contextIDsToExcludeFromHitTesting];
-[UIDraggingSystemTouchRoutingPolicy setContextIDsToAlwaysSendTouchesByDisplayIdentifier:];
-[UIDraggingSystemTouchRoutingPolicy setContextIDsToExcludeFromHitTesting:];
```
